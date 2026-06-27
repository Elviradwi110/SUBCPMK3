import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("data/processed/cases.csv")

# TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)

tfidf_matrix = vectorizer.fit_transform(
    df["text_full"]
)

# Retrieval
def retrieve(query, k=5):

    query_vec = vectorizer.transform([query])

    sim = cosine_similarity(
        query_vec,
        tfidf_matrix
    )

    top_idx = sim[0].argsort()[-k:][::-1]

    return df.iloc[top_idx]


# Reuse
def predict_outcome(query):

    top_cases = retrieve(query)

    return top_cases["case_id"].tolist()


query = """
pemutusan hubungan kerja sepihak
pesangon tidak dibayar
"""

hasil = predict_outcome(query)

print("Top 5 Case:")
print(hasil)