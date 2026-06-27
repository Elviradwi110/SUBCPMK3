import pandas as pd
import matplotlib.pyplot as plt

# Membaca hasil evaluasi
metrics = pd.read_csv("data/eval/prediction_metrics.csv")

# Membuat bar chart
plt.figure(figsize=(6,4))
plt.bar(metrics["Metric"], metrics["Value"])

plt.title("Model Evaluation Metrics")
plt.xlabel("Evaluation Metric")
plt.ylabel("Score")
plt.ylim(0, 1)

# Menampilkan nilai di atas batang
for i, value in enumerate(metrics["Value"]):
    plt.text(i, value + 0.02, f"{value:.2f}", ha="center")

# Menyimpan gambar
plt.savefig("data/eval/evaluation_chart.png", dpi=300, bbox_inches="tight")

# Menampilkan grafik
plt.show()

print("Visualisasi berhasil disimpan di data/eval/evaluation_chart.png")