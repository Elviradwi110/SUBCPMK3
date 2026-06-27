import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# Load data
df = pd.read_csv(
    "data/processed/cases_labeled.csv"
)

# TF-IDF
vectorizer = TfidfVectorizer(
    max_features=5000
)

X = vectorizer.fit_transform(
    df["text_full"]
)

y = df["label"]

# Split 80:20
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# SVM
model = SVC(
    kernel="linear"
)

model.fit(
    X_train,
    y_train
)

y_pred = model.predict(
    X_test
)

# Evaluasi
print("Accuracy :", accuracy_score(y_test,y_pred))

print(
    "Precision :",
    precision_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )
)

print(
    "Recall :",
    recall_score(
        y_test,
        y_pred,
        average="weighted"
    )
)

print(
    "F1 :",
    f1_score(
        y_test,
        y_pred,
        average="weighted"
    )
)

print("\n")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)