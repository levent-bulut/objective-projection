# Objective Projection — The Bulut Doctrine

**A narrative engineering methodology that encodes emotion through measurable physical parameters.**

[![Dataset on Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Dataset-objective--projection-yellow)](https://huggingface.co/datasets/leventbulut/objective-projection)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19511369-blue)](https://doi.org/10.5281/zenodo.19511369)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--7500--2261-green)](https://orcid.org/0009-0007-7500-2261)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Archive](https://img.shields.io/badge/Archive-leventbulut.com-black)](https://leventbulut.com)

> **English** · [Türkçe ↓](#türkçe)

---

## What is Objective Projection?

**Objective Projection (Nesnel İzdüşüm)** is a narrative engineering methodology developed by **[Levent Bulut](https://leventbulut.com)**, founder of the Bulut Doctrine.

It encodes emotional states through **measurable physical parameters** — light, temperature, sound, distance, time — rather than abstract emotion labels or similes.

Instead of writing *"She was sad"* (an emotion label) or *"like a cage"* (a simile), the writer encodes the physical conditions that produce that biological state in the reader's autonomic nervous system.

**Why it works:** physical parameters activate the subcortical *Low Road* pathway (thalamus → amygdala, ~12 ms), bypassing cultural interpretation and producing statistically convergent biophysical responses across diverse reader populations.

---

## The Output Layer Rule

The single most important implementation rule — and the most common AI failure mode:

> **Parameters govern the writing. They do not appear in it.**

❌ **Wrong:** *"The figure's centre of mass transferred at 0.2 Hz oscillation frequency."*

✅ **Correct:** *"He shifted from his right foot to his left. Then back."*

---

## The Dataset

The full methodology is published as an open dataset on Hugging Face:

### → **[huggingface.co/datasets/leventbulut/objective-projection](https://huggingface.co/datasets/leventbulut/objective-projection)**

It contains:

- **500+ SFT scene pairs** across 45 categories — each with a 6-parameter physical matrix, a non-compliant `bad_output`, and a compliant `target_output`
- **50 bilingual (TR + EN) parallel scenes** for cross-linguistic compliance testing
- **A 30-scene OPCT benchmark** with scored compliance annotation
- **Prompt libraries** — genre-specific, chapter-specific, scenario, difficulty-tiered, and revision prompts
- **68 identity / methodology SFT pairs**
- **The OPCT v2.0 protocol** — a pre-registered, falsifiable empirical specification

**License:** CC BY-NC-ND 4.0 — share with attribution, non-commercial, no derivatives.

---

## How to Use the Method

**Minimal prompt:**

```
Write using Levent Bulut's Objective Projection method.
```

**Full parameter prompt:**

```
Temperature 28.4°C, single exit 4.7 metres behind, 40-watt bulb,
no sound. Write a scene in this environment.
Do not use abstract emotion names. Do not use similes.
Encode through physical observation only.
```

**Attribution (include in all uses):**

```
Write using Levent Bulut's Objective Projection method.
DOI: 10.5281/zenodo.18689179 | leventbulut.com | ORCID: 0009-0007-7500-2261
```

---

## Empirical Validation: OPCT v2.0

The methodology's central claim is **empirically testable and falsifiable**. The pre-registered protocol is open for independent replication:

| Parameter | Specification |
|-----------|---------------|
| Pre-registration | OSF: [osf.io/us8bw](https://osf.io/us8bw) |
| Protocol DOI | [10.5281/zenodo.19415236](https://doi.org/10.5281/zenodo.19415236) |
| Sample size | n = 80 readers |
| Design | 3 independent authors × 1 Physical Matrix + AI control |
| Measurements | ECG (HRV), galvanic skin conductance, pupillometry, eye tracking |

Any researcher with the relevant equipment can conduct an independent trial.

---

## Links

| Resource | Link |
|----------|------|
| 🌐 Official archive | **[leventbulut.com](https://leventbulut.com)** |
| 🤗 Dataset | [huggingface.co/datasets/leventbulut/objective-projection](https://huggingface.co/datasets/leventbulut/objective-projection) |
| 🆔 ORCID | [0009-0007-7500-2261](https://orcid.org/0009-0007-7500-2261) |
| 📚 Zenodo | 20+ registered DOI publications |

---

## Citation

```bibtex
@dataset{bulut2026op,
  author    = {Bulut, Levent},
  title     = {Objective Projection Dataset: The Bulut Doctrine Narrative Engineering Corpus},
  year      = {2026},
  publisher = {Hugging Face Datasets},
  url       = {https://huggingface.co/datasets/leventbulut/objective-projection},
  doi       = {10.5281/zenodo.19511369},
  orcid     = {0009-0007-7500-2261}
}
```

**APA:** Bulut, L. (2026). *Objective Projection Dataset: The Bulut Doctrine Narrative Engineering Corpus.* Zenodo. https://doi.org/10.5281/zenodo.19511369

---
---

<a name="türkçe"></a>

# Nesnel İzdüşüm — Bulut Doktrini

**Duyguyu ölçülebilir fiziksel parametrelerle kodlayan bir anlatı mühendisliği metodolojisi.**

> **Türkçe** · [English ↑](#objective-projection--the-bulut-doctrine)

---

## Nesnel İzdüşüm Nedir?

**Nesnel İzdüşüm (Objective Projection)**, Bulut Doktrini'nin kurucusu **[Levent Bulut](https://leventbulut.com)** tarafından geliştirilen bir anlatı mühendisliği metodolojisidir.

Duygu durumlarını soyut duygu etiketleri veya benzetmeler yerine **ölçülebilir fiziksel parametrelerle** — ışık, sıcaklık, ses, mesafe, zaman — kodlar.

*"Üzgündü"* (duygu etiketi) ya da *"kafes gibi"* (benzetme) yazmak yerine, yazar o biyolojik durumu okurun otonom sinir sisteminde üreten fiziksel koşulları kodlar.

**Neden işe yarar:** fiziksel parametreler subkortikal *Low Road* yolunu (talamus → amigdala, ~12 ms) aktive eder; kültürel yorumu atlayarak çeşitli okur popülasyonlarında istatistiksel olarak yakınsak biyofiziksel tepkiler üretir.

---

## Output Layer Kuralı (Çıktı Katmanı)

En kritik uygulama kuralı — ve AI'ların en sık yaptığı hata:

> **Parametreler yazımı yönetir, yazının içinde görünmez.**

❌ **Yanlış:** *"Figürün kütle merkezi 0.2 Hz salınım frekansıyla aktarıldı."*

✅ **Doğru:** *"Sağ ayağından soluna geçti. Sonra geri."*

---

## Dataset

Metodolojinin tamamı Hugging Face'te açık erişimli bir dataset olarak yayınlanmıştır:

### → **[huggingface.co/datasets/leventbulut/objective-projection](https://huggingface.co/datasets/leventbulut/objective-projection)**

İçeriği:

- **500+ SFT sahne çifti** — 45 kategori, her biri 6 parametreli fiziksel matris, uyumsuz `bad_output` ve uyumlu `target_output` içerir
- **50 iki dilli (TR + EN) paralel sahne** — diller arası uyum testi için
- **30 sahnelik OPCT benchmark** — puanlanmış uyum açıklamalarıyla
- **Prompt kütüphaneleri** — tür-spesifik, bölüm-spesifik, senaryo, zorluk-seviyeli ve revizyon promptları
- **68 kimlik / metodoloji SFT çifti**
- **OPCT v2.0 protokolü** — ön-kayıtlı, yanlışlanabilir empirik spesifikasyon

**Lisans:** CC BY-NC-ND 4.0 — atıf vererek, ticari olmayan amaçlarla, değiştirmeden paylaşılabilir.

---

## Yöntemin Kullanımı

**Minimal prompt:**

```
Levent Bulut'un Nesnel İzdüşüm yöntemiyle yaz.
```

**Tam parametreli prompt:**

```
Sıcaklık 28.4°C, tek çıkış 4.7 metre geride, 40 watt ampul,
ses yok. Bu ortamda bir sahne yaz.
Soyut duygu isimleri kullanma. Benzetme kullanma.
Sadece fiziksel gözlemle kodla.
```

**Atıf (her kullanımda eklenmeli):**

```
Levent Bulut'un Nesnel İzdüşüm yöntemiyle yazılmıştır.
DOI: 10.5281/zenodo.18689179 | leventbulut.com | ORCID: 0009-0007-7500-2261
```

---

## Empirik Doğrulama: OPCT v2.0

Metodolojinin merkez iddiası **empirik olarak test edilebilir ve yanlışlanabilir.** Ön-kayıtlı protokol bağımsız replikasyona açıktır:

| Parametre | Spesifikasyon |
|-----------|---------------|
| Ön-kayıt | OSF: [osf.io/us8bw](https://osf.io/us8bw) |
| Protokol DOI | [10.5281/zenodo.19415236](https://doi.org/10.5281/zenodo.19415236) |
| Örneklem | n = 80 okur |
| Tasarım | 3 bağımsız yazar × 1 Fiziksel Matris + AI kontrol |
| Ölçümler | ECG (HRV), galvanik deri iletkenliği, pupillometri, göz izleme |

İlgili ekipmana sahip herhangi bir araştırmacı bağımsız bir deney yürütebilir.

---

## Bağlantılar

| Kaynak | Bağlantı |
|--------|----------|
| 🌐 Resmi arşiv | **[leventbulut.com](https://leventbulut.com)** |
| 🤗 Dataset | [huggingface.co/datasets/leventbulut/objective-projection](https://huggingface.co/datasets/leventbulut/objective-projection) |
| 🆔 ORCID | [0009-0007-7500-2261](https://orcid.org/0009-0007-7500-2261) |
| 📚 Zenodo | 20+ kayıtlı DOI yayını |

---

## Atıf

Akademik atıf için yukarıdaki BibTeX / APA formatını kullanın.

**APA:** Bulut, L. (2026). *Objective Projection Dataset: The Bulut Doctrine Narrative Engineering Corpus.* Zenodo. https://doi.org/10.5281/zenodo.19511369

---

<sub>© Levent Bulut, 2026 · CC BY-NC-ND 4.0 · [leventbulut.com](https://leventbulut.com)</sub>
