# Lessons: Reasoning, KBA, Sistem Pakar, Uncertainty & Logika Fuzzy

Pembelajaran mandiri persiapan UAS berbasis PDF materi kuliah. Setiap HTML adalah self-contained lesson dengan embedded CSS dan JS quiz interaktif -- tanpa dependensi eksternal, bisa dibuka offline.

## Struktur Belajar

```
PDF 1: Reasoning & KBA
  -> Lesson 1: Propositional Logic & Inference Rules
  -> Lesson 2: First-Order Logic (FOL)
  -> Lesson 3: Wumpus World Case Study (PL + FOL)

PDF 2: Pengenalan Sistem Pakar
  -> Lesson 4: Fundamental Sistem Pakar (arsitektur, aktor, DNA, akuisisi)
  -> Lesson 5: Representasi Pengetahuan (IF-THEN, Semantic Net, Frames)
  -> Lesson 6: Inferensi & Anomali Logika (FC, BC, CF, 6 anomali, studi kasus hewan)

PDF 3: Expert System Uncertainty Logic
  -> Lesson 7: Certainty Factor Deep Dive (MB/MD, CF gabungan, resolusi konflik, FORECAST)
  -> Lesson 8: Probabilitas Bayes (Teorema, multi-evidence, iterasi 3 hipotesis)

PDF 4: Logika Fuzzy
  -> Lesson 9:  Himpunan Fuzzy & Terminologi (Crisp vs Fuzzy, 4 istilah fondasi)
  -> Lesson 10: 7 Fungsi Keanggotaan (Linear, Segitiga, Trapesium, Bahu, Diskret, Non-Linear)
  -> Lesson 11: Operator Zadeh (AND/OR/NOT) + Fungsi Implikasi (MIN vs DOT)
  -> Lesson 12: Sistem Inferensi Fuzzy Mamdani (4-langkah FIS + studi kasus produksi)
```

## Daftar Lesson

| # | File | Topik |
|---|------|-------|
| 1 | `0001-propositional-logic-inference.html` | Propositional logic, truth tables, 5 inference rules, Horn Form, CNF Resolution |
| 2 | `0002-first-order-logic.html` | FOL syntax, quantifiers, unification, Generalized Modus Ponens |
| 3 | `0003-wumpus-world-lengkap.html` | Wumpus World 8-step agent journey, KB construction PL+FOL, 7-step UAS method |
| 4 | `0004-sistem-pakar-fundamental.html` | ES definition, 4-component architecture, 4 actors, DNA, feasibility, knowledge acquisition |
| 5 | `0005-representasi-pengetahuan.html` | IF-THEN Rules, Semantic Networks (IS-A), Frames (slots), comparison matrix |
| 6 | `0006-inferensi-dan-anomali.html` | Forward/Backward Chaining, CF basics, Why/How, 6 anomalies, animal classification |
| 7 | `0007-cf-deep-dive.html` | CF = MB - MD, MB/MD formulas, linguistic-to-numeric, CF gabungan, resolusi konflik, FORECAST |
| 8 | `0008-probabilitas-bayes.html` | Teorema Bayes, prior/conditional/posterior, mutually exclusive, conditional independence, iterasi 3 hipotesis |
| 9 | `0009-himpunan-fuzzy-fundamental.html` | Crisp vs Fuzzy, Zadeh 1965, 4 istilah (variabel/himpunan/semesta/domain), 35 tahun problem |
| 10 | `0010-fungsi-keanggotaan.html` | 7 jenis: Linear Naik/Turun, Segitiga, Trapesium, Bahu Kiri/Kanan, Diskret, Non-Linear |
| 11 | `0011-operator-implikasi.html` | AND=MIN, OR=MAX, NOT=1-x; implikasi MIN (truncation) vs DOT (scaling); α-predikat |
| 12 | `0012-mamdani-fis.html` | FIS 4-langkah (Fuzzifikasi → Implikasi → Agregasi → Defuzzifikasi Centroid) + studi kasus produksi lengkap |

## Cara Pakai

Buka langsung file `.html` di browser:

```bash
# Dari terminal
xdg-open 0001-propositional-logic-inference.html

# Atau double-click di file manager
```

## Sumber

| PDF | Topik |
|-----|-------|
| `1. Reasoning - KBA-a.pdf` | Wumpus World, Propositional Logic, FOL |
| `2. Pengenalan Sistem Pakar.pdf` | Arsitektur, Representasi, Inferensi, Anomali |
| `3. Expert_System_Uncertainty_Logic.pdf` | Certainty Factor, Probabilitas Bayes |
| `4. Logika Fuzzy.pdf` | Crisp vs Fuzzy, Fungsi Keanggotaan, Operator Zadeh, Mamdani FIS |

Referensi pustaka: Zadeh (1965), Mamdani & Assilian (1975), Giarratano (2007), Sutojo et al. (2018), Negnevitsky (2011), Russel & Norvig (2010).

## Cheatsheet

Gabungan semua materi ada di `master-cheatsheet.html` -- format compact grid, print-friendly, mencakup 10 bagian: KBA (1-3) + SP (4-7) + CF (8) + Bayes (9) + Logika Fuzzy (10).
