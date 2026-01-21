import pandas as pd
import re
from collections import Counter
import os

# Asegurar carpeta data
os.makedirs("data", exist_ok=True)

# Leer raw
df = pd.read_csv("data/raw.csv")

print("📊 Filas originales:", len(df))

# Limpieza básica
df = df.dropna()
df = df[["date", "title", "link"]]

df.to_csv("data/clean.csv", index=False)
print("✅ clean.csv creado")

# ---- SUMMARY ----
all_titles = " ".join(df["title"]).lower()
words = re.findall(r"\b[a-z]{4,}\b", all_titles)

top_words = Counter(words).most_common(5)

summary_rows = [
    {"metric": "Total de posts", "value": len(df)}
]

for word, count in top_words:
    summary_rows.append({
        "metric": f"Top palabra: {word}",
        "value": count
    })

summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv("data/summary.csv", index=False)

print("✅ summary.csv creado")
