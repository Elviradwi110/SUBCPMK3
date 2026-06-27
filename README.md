# Case-Based Reasoning (CBR) untuk Putusan Pengadilan Hubungan Industrial (PHI)

## Deskripsi Project

Project ini merupakan implementasi **Case-Based Reasoning (CBR)** untuk melakukan pencarian dan prediksi putusan Pengadilan Hubungan Industrial (PHI) berdasarkan kasus-kasus sebelumnya yang diperoleh dari Direktori Putusan Mahkamah Agung Republik Indonesia.

Dataset terdiri dari **33 putusan PHI** yang diekstraksi dari file PDF, diproses menjadi teks, direpresentasikan menjadi metadata, kemudian digunakan untuk proses retrieval, prediction, evaluation, dan visualisasi hasil evaluasi.

---

# Struktur Repository

```text
SUBCPMK3
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── 01_casebase.py
│   ├── 02_representation.py
│   ├── 02_labeling.py
│   ├── 03_retrieval.py
│   ├── 04_predict.py
│   ├── 05_evaluation.py
│   └── 06_visualization.py
│
├── data/
│   ├── pdf/
│   ├── raw/
│   ├── processed/
│   │   ├── cases.csv
│   │   └── cases_labeled.csv
│   │
│   ├── result/
│   │   └── predictions.csv
│   │
│   └── eval/
│       ├── queries.json
│       ├── retrieval_metrics.csv
│       ├── prediction_metrics.csv
│       └── evaluation_chart.png
```

---

# Dataset

**Domain:** Pengadilan Hubungan Industrial (PHI)

**Sumber Data:** Direktori Putusan Mahkamah Agung Republik Indonesia

**Jumlah Putusan:** 33 Putusan PHI

**Label Putusan:**

* dikabulkan
* dikabulkan_sebagian
* ditolak
* tidak_diterima

---

# Requirements

Install seluruh dependency menggunakan:

```bash
python -m pip install -r requirements.txt
```

Isi file `requirements.txt`:

* pdfplumber
* pandas
* numpy
* scikit-learn
* matplotlib
* jupyter
* notebook

---

# Tahapan CBR

## 1. Case Base Construction

File:

```text
01_casebase.py
```

Output:

```text
data/raw/
```

---

## 2. Case Representation

File:

```text
02_representation.py
02_labeling.py
```

Output:

```text
data/processed/cases.csv
data/processed/cases_labeled.csv
```

---

## 3. Case Retrieval

Metode:

* TF-IDF
* Cosine Similarity

File:

```text
03_retrieval.py
```

Output:

```text
Top-K Similar Cases
```

---

## 4. Case Solution Reuse

File:

```text
04_predict.py
```

Output:

```text
data/result/predictions.csv
```

---

## 5. Model Evaluation

Metode evaluasi:

* Accuracy
* Precision
* Recall
* F1-Score

File:

```text
05_evaluation.py
```

Output:

```text
data/eval/retrieval_metrics.csv
data/eval/prediction_metrics.csv
```

---

## 6. Visualization

File:

```text
06_visualization.py
```

Output:

```text
data/eval/evaluation_chart.png
```

Visualisasi berupa bar chart yang menampilkan nilai Accuracy, Precision, Recall, dan F1-Score.

---

# Cara Menjalankan Project

Install dependency:

```bash
python -m pip install -r requirements.txt
```

Jalankan file secara berurutan:

```text
01_casebase.py
↓
02_representation.py
↓
02_labeling.py
↓
03_retrieval.py
↓
04_predict.py
↓
05_evaluation.py
↓
06_visualization.py
```

---

# Hasil Evaluasi

| Metric    | Value |
| --------- | ----: |
| Accuracy  |  0.43 |
| Precision |  0.52 |
| Recall    |  0.43 |
| F1-Score  |  0.36 |

## Analisis

Model memperoleh akurasi sebesar **43%**. Nilai ini dipengaruhi oleh jumlah data yang relatif sedikit (33 putusan) dan distribusi label yang belum seimbang. Performa model dapat ditingkatkan dengan menambah jumlah data, memperbaiki proses preprocessing, serta menggunakan metode representasi teks yang lebih baik seperti transformer (misalnya IndoBERT).

---

# Author

**Nama:** Elvira Dwi Irianty Woretma

**NIM:** 202310370311456

**Program Studi:** Teknik Informatika

**Mata Kuliah:** Penalaran Komputer B

**Universitas:** Universitas Muhammadiyah Malang

---

# Repository

Repository GitHub:

https://github.com/Elviradwi110/SUBCPMK3
