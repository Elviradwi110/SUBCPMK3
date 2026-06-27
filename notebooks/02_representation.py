import os
import pandas as pd

raw_folder = "data/raw"

cases = []

files = sorted(os.listdir(raw_folder))

for file in files:

    path = os.path.join(raw_folder, file)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    cases.append({
        "case_id": file,
        "text_full": text,
        "length": len(text.split())
    })

df = pd.DataFrame(cases)

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/cases.csv",
    index=False
)

print(df.head())
print("\nJumlah Kasus:", len(df))
