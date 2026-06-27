import pandas as pd

df = pd.read_csv("data/processed/cases.csv")

def get_label(text):

    text = str(text).lower()

    if "dikabulkan untuk sebagian" in text:
        return "dikabulkan_sebagian"

    elif "mengabulkan gugatan penggugat untuk seluruhnya" in text:
        return "dikabulkan"

    elif "menolak gugatan penggugat" in text:
        return "ditolak"

    elif "tidak dapat diterima" in text:
        return "tidak_diterima"

    else:
        return "lainnya"

df["label"] = df["text_full"].apply(get_label)

df.to_csv(
    "data/processed/cases_labeled.csv",
    index=False
)

print(df["label"].value_counts())