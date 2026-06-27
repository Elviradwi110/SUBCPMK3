# Case-Based Reasoning (CBR) untuk Putusan Pengadilan Hubungan Industrial (PHI)

## Deskripsi Project

Project ini merupakan implementasi metode **Case-Based Reasoning (CBR)** untuk melakukan pencarian dan prediksi putusan Pengadilan Hubungan Industrial (PHI) berdasarkan kasus-kasus sebelumnya yang diperoleh dari Direktori Putusan Mahkamah Agung Republik Indonesia.

Dataset terdiri dari **33 putusan PHI** yang diekstraksi dari PDF, dibersihkan, direpresentasikan dalam bentuk terstruktur, kemudian digunakan untuk proses retrieval, prediction, dan evaluation.

---

# Struktur Repository

```text
CBR_PHI
│
├── README.md
│
├── notebooks/
│   ├── 01_casebase.ipynb
│   ├── 02_representation.ipynb
│   ├── 02_labeling.ipynb
│   ├── 03_retrieval.ipynb
│   ├── 04_predict.ipynb
│   └── 05_evaluation.ipynb
│
├── data/
│   ├── pdf/
│   ├── raw/
│   ├── processed/
│   │   ├── cases.csv
│   │   └── cases_labeled.csv
│   │
│   ├── eval/
│   │   ├── queries.json
│   │   ├── retrieval_metrics.csv
│   │   └── prediction_metrics.csv
│   │
│   └── result/
│       └── predictions.csv
│
└── putusan_phi.zip
```

---

# Dataset

**Domain:** Pengadilan Hubungan Industrial (PHI)

**Sumber Data:**
Direktori Putusan Mahkamah Agung Republik Indonesia

**Jumlah Putusan:**
33 Putusan PHI

**Label Putusan:**

- dikabulkan
- dikabulkan_sebagian
- ditolak
- tidak_diterima

---

# Requirements

Install library berikut:

```bash
pip install pdfplumber pandas numpy scikit-learn matplotlib
```

Versi yang digunakan:

- Python 3.13
- pdfplumber
- pandas
- numpy
- scikit-learn
- matplotlib

---

# Tahapan CBR

## 1. Case Base Construction

Tujuan:

- Mengumpulkan putusan PHI
- Ekstraksi PDF ke TXT
- Membersihkan teks

Notebook:

```text
01_casebase.ipynb
```

Output:

```text
data/raw/*.txt
```

---

## 2. Case Representation

Tujuan:

- Merepresentasikan kasus dalam bentuk terstruktur
- Membuat metadata dan fitur kasus

Notebook:

```text`
02_representation.ipynb
02_labeling.ipynb
```

Output:

```text
data/processed/cases.csv
data/processed/cases_labeled.csv
```

---

## 3. Case Retrieval

Metode:

- TF-IDF Vectorization
- Cosine Similarity

Notebook:

```text
03_retrieval.ipynb
```

Output:

```text
Top-K kasus yang paling mirip
```

---

## 4. Case Solution Reuse

Metode:

- Menggunakan hasil retrieval untuk memprediksi putusan kasus baru

Notebook:

```text
04_predict.ipynb
```

Output:

```text
data/result/predictions.csv
```

---

## 5. Model Evaluation

Metode:

- Support Vector Machine (SVM)
- Accuracy
- Precision
- Recall
- F1-Score

Notebook:

```text
05_evaluation.ipynb
```

Output:

```text
data/eval/retrieval_metrics.csv
data/eval/prediction_metrics.csv
```

---

# Cara Menjalankan Project

Buka notebook secara berurutan:

```text
01_casebase.ipynb
↓
02_representation.ipynb
↓
02_labeling.ipynb
↓
03_retrieval.ipynb
↓
04_predict.ipynb
↓
05_evaluation.ipynb
```

Jalankan seluruh cell pada masing-masing notebook hingga menghasilkan output pada folder `data`.

---

# Hasil Evaluasi

| Metric | Nilai |
|----------|----------|
| Accuracy | 42.86% |
| Precision | 52.38% |
| Recall | 42.86% |
| F1-Score | 35.71% |

## Analisis

Model memperoleh akurasi sebesar 42.86%. Hasil ini dipengaruhi oleh jumlah data yang masih terbatas (33 putusan) dan distribusi label yang belum seimbang. Performa model dapat ditingkatkan dengan menambah jumlah putusan, memperbaiki preprocessing, serta menggunakan model berbasis transformer seperti IndoBERT.

---

# Author

**Nama:** Elvira Dwi Irianty Woretma

**Nim:** 202310370311456

**Program Studi:** Teknik Informatika

**Mata Kuliah:** Penalaran Komputer B

**Universitas:** Universitas Muhammadiyah Malang

---

# Repository

Repository GitHub:

https://github.com/Elviradwi110/CBR_PHI