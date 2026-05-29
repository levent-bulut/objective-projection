"""
apply_rules.py — Objective Projection dataset v7 update
Adds `applied_rules` field to each scene based on 6 Golden Rules detection.
Rule-based, transparent, deterministic, bilingual (TR+EN).
Preserves all existing fields. Only ADDS one new top-level field.
"""

import json
import re

# ============================================================
# 6 GOLDEN RULES — bilingual detection
# ============================================================

# 1. DUYGU AMBARGOSU (Emotion Embargo)
# target_output'ta doğrudan duygu etiketi olmamalı
EMOTION_LABELS_TR = [
    # temel duygular
    r'\büzgün', r'\bmutlu', r'\bkorku', r'\böfke', r'\bsevin',
    r'\bkızgın', r'\bheyecan', r'\bumut', r'\bumutsuz', r'\bçaresiz',
    r'\bpişman', r'\bgururlu', r'\butan', r'\bkıskan', r'\bnefret',
    r'\bsevg', r'\başk', r'\bhüzün', r'\bkeder', r'\byalnız',
    r'\bdehşet', r'\bşok', r'\bpanik', r'\bendişe', r'\bkaygı',
    r'\btedirgin', r'\brahat', r'\bhuzur', r'\bmemnun', r'\bmutsuz',
    r'\bcoşku', r'\bnostalji', r'\bözlem', r'\bözledi', r'\bözlüyor',
    r'\bhissetti', r'\bhissediyor', r'\bhissediyordu',
    r'\bduygulan', r'\bağladı', r'\bağlıyor',
    # klişe metaforlar
    r'kalbi paramparça', r'kalbi kırıl', r'dünyası yıkıl',
    r'dünyası karar', r'içi parçalan', r'içi sızl',
    r'kalbi çarp', r'kalbi yerinden', r'nefes alamı',
    r'dayanam', r'çaresizce', r'mutlulukla', r'sevinçle',
    r'üzgünce', r'kederle', r'öfkeyle', r'korkuyla',
]

EMOTION_LABELS_EN = [
    r'\bsad\b', r'\bsadly\b', r'\bsadness\b', r'\bunhappy\b',
    r'\bhappy\b', r'\bhappily\b', r'\bhappiness\b', r'\bjoy', r'\bjoyful',
    r'\bafraid\b', r'\bfear', r'\bterrif', r'\bscared\b', r'\bpanic',
    r'\bangr', r'\bangry\b', r'\bfurious\b', r'\brage\b', r'\bmad\b',
    r'\bexcited?\b', r'\bexcitement\b', r'\bthrill',
    r'\bhopeful\b', r'\bhopeless\b', r'\bdespair',
    r'\bashamed\b', r'\bshame\b', r'\bguilt', r'\bregret',
    r'\bjealous', r'\benv(y|ious)\b', r'\bhate\b', r'\bhated\b',
    r'\blove\b', r'\bloved\b', r'\bloving\b', r'\bromantic\b',
    r'\bmelanchol', r'\blonel(y|iness)\b', r'\bgrief\b', r'\bgrieving\b',
    r'\bshocked\b', r'\bdevastated\b', r'\bbroken\b', r'\bdistraught\b',
    r'\bworried\b', r'\banxious\b', r'\banxiety\b', r'\bnervous\b',
    r'\brelieved\b', r'\bcontent\b', r'\bpeaceful\b', r'\bcalm\b',
    r'\bnostalgic\b', r'\blonging\b', r'\bmissed?\b(?! the)',  # avoid "missed the bus"
    # 'felt' tek başına fiziksel his olabilir; sadece duygu nesneli yasak
    r'\bfelt (sad|happy|angry|scared|afraid|lonely|empty|broken|relieved|guilty|ashamed|hopeless|lost|alive|free|safe|loved|hated|terrified|excited|nervous|anxious|worried)\b',
    r'\bfeeling (sad|happy|angry|scared|afraid|lonely|empty|broken|relieved|guilty|ashamed|hopeless|nervous|anxious)\b',
    r'\bheart (broke|pounded|raced|sank)',
    r'\bworld (collapsed|shattered|ended)',
    r'\beyes filled with tears\b', r'\btears streamed\b',
    r'\bfrozen with\b', r'\boverwhelmed (with|by)\b',
]

# 2. BENZETME YASAĞI (Simile Prohibition)
SIMILES_TR = [r'\bgibi\b', r'\bsanki\b', r'\badeta\b', r'\büzere\b(?= olm)']
SIMILES_EN = [r'\blike a\b', r'\blike an\b', r'\blike the\b',
              r'\bas if\b', r'\bas though\b', r'\bseemed (like|to)\b',
              r'\bappeared to be\b']

# 3. MADDELEŞEN METAFORLAR — soyut→somut dönüşüm
# Heuristik: physical_matrix'teki somut öğeler target_output'ta geçiyor mu?
# Bu fiziksel parametreler yazıya yansımış mı?

# 4. MİKRO ODAK (Ng nesnesi) — dar nesnel odaklanma
# Heuristik: küçük somut nesne adı + sayısal ölçü
MICRO_FOCUS_TR_HINTS = [
    r'\bparmak', r'\btırnak', r'\bkirpik', r'\bcam\b', r'\biplik',
    r'\btoz', r'\bkar tanesi', r'\bdamla', r'\bkavanoz', r'\banahtar',
    r'\bçatal', r'\bkaşık', r'\bdüğme', r'\bnokta\b', r'\bçizgi',
    r'\bkıvrım', r'\bçatlak', r'\bleke', r'\bgöz teması', r'\bnefes',
]
MICRO_FOCUS_EN_HINTS = [
    r'\bfinger', r'\bnail\b', r'\beyelash', r'\bglass\b', r'\bthread',
    r'\bdust', r'\bsnowflake', r'\bdrop\b', r'\bjar\b', r'\bkey\b',
    r'\bfork\b', r'\bspoon\b', r'\bbutton', r'\bdot\b', r'\bline\b',
    r'\bcrease', r'\bcrack', r'\bstain', r'\beye contact\b', r'\bbreath',
    r'\bknuckle', r'\bwrist', r'\bcuff',
]

# 5. ZAMANSAL ÇAPA — somut zaman/süre işareti
TEMPORAL_PATTERNS = [
    r'\b\d{1,2}[:.]\d{2}\b',                # 06:42, 11.30
    r'\b\d+\s*(saniye|sn|dakika|dk|saat)\b', # 3 saniye, 12 dk
    r'\b\d+\s*(seconds?|minutes?|hours?|metres?|meters?)\b',
    r'\b\d+(\.\d+)?\s*°C\b',                # 14°C
    r'\b\d+\s*(cm|mm|m|km|kg|g|W|Hz|dB|centimetres?|centimeters?|metres?|meters?)\b',
    r'\b(bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|on bir|on iki|on üç|on dört|on beş)\s+(saniye|sn|dakika|dk|saat|gün|yaş|adım|metre|santim|cm)\b',
    r'\b(altı|yedi|sekiz|dokuz|on|on bir|on iki)\s+(kırk|otuz|yirmi|on|elli|on beş)',  # saat: altı kırk iki
    r'\b(üç|beş|yedi|on|on iki)\s+(saniye|dakika|gün|saat|hafta|yaş|adım|metre)',
    r'\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty)[\s-](seconds?|minutes?|hours?|days?|weeks?|months?|years?|steps?|metres?|meters?|centimetres?)',
    r'\b(twenty-two|twenty-three|forty-five)\s+(minutes?|seconds?|years?)',
    r'\bsabah\s*\d', r'\böğle', r'\bgece yarısı',
    r'\bin the morning\b', r'\bat noon\b', r'\bmidnight\b',
    r'\b(önce|sonra)\s+\d',
    r'\b\d+\s+(yıl|ay|gün|yaş)',
    r'\b\d+\s+(year|month|day)s?\s+(ago|old|later)',
]

# 6. ATMOSFER ÇELİŞKİSİ — beklenmeyen detay/karşıtlık
# Heuristik: physical_matrix'te zıt parametreler veya target'ta beklenmeyen tekil olay
CONTRADICTION_HINTS_TR = [
    r'\bama\b', r'\byine de\b', r'\boysa\b', r'\bbuna rağmen\b',
    r'\baltında\s+\w+\s+(eridi|donmadı)',
    r'\bgülümse', r'(kedi|köpek)\s+(durmadı|izlemedi|umursamadı)',
    r'\bilgisiz', r'\bumursamadan',
]
CONTRADICTION_HINTS_EN = [
    r'\byet\b', r'\bstill\b(?=,)', r'\bnevertheless\b', r'\bhowever',
    r'\bdespite\b', r'\bin spite of\b',
    r'\bdid not (move|react|turn)\b',
    r'\bunbothered\b', r'\bindifferent\b',
]


def detect_emotion_embargo(text, lang):
    """Returns True if NO direct emotion labels found (rule respected)."""
    patterns = EMOTION_LABELS_TR if lang == 'tr' else EMOTION_LABELS_EN
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return False
    return True


def detect_simile_prohibition(text, lang):
    """Returns True if NO similes found."""
    patterns = SIMILES_TR if lang == 'tr' else SIMILES_EN
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return False
    return True


def detect_materialized_metaphor(text, physical_matrix):
    """
    Heuristic: physical_matrix'teki en az 2 somut element target'ta belirmeli.
    Yani fiziksel parametreler 'yazıya inmiş' mi?
    """
    if not isinstance(physical_matrix, dict):
        return False
    text_lower = text.lower()
    hits = 0
    for k, v in physical_matrix.items():
        if not isinstance(v, str):
            continue
        # parametre değerinden somut anahtar kelimeleri çıkar
        # sayılar + birim VEYA somut isim
        tokens = re.findall(r'\d+\s*(?:°C|cm|mm|m|km|kg|Hz|dB|W|sn|dk|saniye|dakika|saat)', v, re.IGNORECASE)
        for tok in tokens:
            # tam eşleşme veya yakın
            num_part = re.search(r'\d+', tok)
            if num_part and num_part.group() in text:
                hits += 1
                break
        # somut isim eşleşmesi (uzun kelimeler)
        nouns = [w for w in re.findall(r'\b[a-zçğıöşüA-ZÇĞİÖŞÜ]{5,}\b', v) if w.lower() not in
                 ('ambient', 'overhead', 'baseline', 'sharp', 'corridor', 'enclosed', 'sıcaklık', 'mesafe')]
        for n in nouns[:3]:
            if n.lower() in text_lower:
                hits += 1
                break
    return hits >= 2


def detect_micro_focus(text, lang, physical_matrix):
    """
    Mikro odak: dar somut nesneye yoğunlaşma.
    Ng nesnesi physical_matrix'te varsa target'ta da geçmeli.
    Veya genel mikro odak hint'leri.
    """
    text_lower = text.lower()
    # Ng nesnesi varsa onu öncelikle kontrol et
    if isinstance(physical_matrix, dict):
        ng = physical_matrix.get('Ng') or physical_matrix.get('ng')
        if ng and isinstance(ng, str):
            ng_words = [w for w in re.findall(r'\b\w{4,}\b', ng.lower()) if w not in
                        ('için', 'gibi', 'olan')]
            for w in ng_words:
                if w in text_lower:
                    return True
    # Genel hint'ler
    hints = MICRO_FOCUS_TR_HINTS if lang == 'tr' else MICRO_FOCUS_EN_HINTS
    for p in hints:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False


def detect_temporal_anchor(text):
    """Somut zaman işareti var mı?"""
    for p in TEMPORAL_PATTERNS:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False


def detect_atmosphere_contradiction(text, lang, physical_matrix):
    """
    Beklenmedik detay / karşıtlık var mı?
    Heuristik: atmospheric kontrast kelimesi VEYA physical_matrix'te
    sıcak-soğuk gibi karşıt değerler.
    """
    hints = CONTRADICTION_HINTS_TR if lang == 'tr' else CONTRADICTION_HINTS_EN
    for p in hints:
        if re.search(p, text, re.IGNORECASE):
            return True
    # physical_matrix'te birden fazla farklı parametre + farklı yön
    if isinstance(physical_matrix, dict):
        v_str = ' '.join(str(v) for v in physical_matrix.values()).lower()
        warm = bool(re.search(r'\b(sıcak|warm|hot|\d{2,}°C)\b', v_str))
        cold = bool(re.search(r'\b(soğuk|cold|cool|chill|donmuş|frozen|4°C|3°C|2°C|1°C|0°C|-)\b', v_str))
        if warm and cold:
            return True
    return False


def compute_applied_rules(scene):
    """Tek bir scene için applied_rules sözlüğü üret."""
    target = scene.get('target_output', '')
    lang = scene.get('language', 'en')
    pm = scene.get('physical_matrix', {})

    rules = {
        'duygu_ambargosu': detect_emotion_embargo(target, lang),
        'benzetme_yasagi': detect_simile_prohibition(target, lang),
        'maddelesen_metaforlar': detect_materialized_metaphor(target, pm),
        'mikro_odak': detect_micro_focus(target, lang, pm),
        'zamansal_capa': detect_temporal_anchor(target),
        'atmosfer_celiskisi': detect_atmosphere_contradiction(target, lang, pm),
    }

    active = [k for k, v in rules.items() if v]
    rules['active_count'] = len(active)
    rules['primary_rule'] = active[0] if active else None
    rules['detection_method'] = 'rule_based_v2_bilingual_heuristic'
    rules['doctrine_version'] = 'v3.0_May2026'

    return rules


def process_file(in_path, out_path, dry_run_lines=None):
    """Mevcut JSONL'i oku, applied_rules ekle, yeni dosyaya yaz."""
    count = 0
    with open(in_path, 'r', encoding='utf-8') as fin, \
         open(out_path, 'w', encoding='utf-8') as fout:
        for line in fin:
            line = line.rstrip('\n')
            if not line.strip():
                continue
            scene = json.loads(line)
            # MEVCUT ALANLARI HİÇ DEĞİŞTİRME — sadece ekle
            scene['applied_rules'] = compute_applied_rules(scene)
            fout.write(json.dumps(scene, ensure_ascii=False) + '\n')
            count += 1
            if dry_run_lines and count >= dry_run_lines:
                break
    return count


if __name__ == '__main__':
    import sys
    in_path = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads/sft_complete_500_annotated.jsonl'
    out_path = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/dry_run_10.jsonl'
    dry = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    n = process_file(in_path, out_path, dry_run_lines=dry)
    print(f"İşlendi: {n} sahne → {out_path}")
