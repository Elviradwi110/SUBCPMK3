import os
import re
import pdfplumber

# Membuat folder raw jika belum ada
os.makedirs("data/raw", exist_ok=True)

def extract_text(pdf_path):

    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print("Error:", pdf_path, e)

    return text


def clean_text(text):

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    return text.strip()


pdf_folder = "data/pdf"

pdf_files = [
    f for f in os.listdir(pdf_folder)
    if f.endswith(".pdf")
]

for i, file in enumerate(pdf_files):

    pdf_path = os.path.join(pdf_folder, file)

    text = extract_text(pdf_path)

    text = clean_text(text)

    txt_name = f"case_{i+1:03d}.txt"

    with open(
        os.path.join("data/raw", txt_name),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(text)

print("Jumlah PDF :", len(pdf_files))
print("TXT berhasil dibuat")