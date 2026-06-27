import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("data/processed/cases.csv")

# TF-IDF
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words=None
)

tfidf_matrix = vectorizer.fit_transform(
    df["text_full"]
)

print("Jumlah Dokumen :", len(df))
print("Shape TF-IDF :", tfidf_matrix.shape)

# Fungsi Retrieval
def retrieve(query, k=5):

    query_vec = vectorizer.transform([query])

    similarity = cosine_similarity(
        query_vec,
        tfidf_matrix
    )

    top_idx = similarity[0].argsort()[-k:][::-1]

    result = df.iloc[top_idx][
        ["case_id"]
    ]

    return result

# Contoh Query
query = """
perselisihan hubungan kerja,
pemutusan hubungan kerja sepihak,
pesangon
"""

hasil = retrieve(query)

print("\nTop 5 Kasus Mirip:")
print(hasil)