import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

print("📍 Directorio actual:", os.getcwd())

# Asegurar que exista la carpeta data
os.makedirs("data", exist_ok=True)

url = "https://blog.python.org/"
response = requests.get(url)

print("🌐 Estado de la petición:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", class_="date-outer")
print("📝 Posts encontrados:", len(posts))

data = []

for post in posts:
    title_tag = post.find("h3", class_="post-title")
    date_tag = post.find("h2", class_="date-header")

    if title_tag and date_tag:
        title = title_tag.get_text(strip=True)
        link = title_tag.find("a")["href"]
        date = date_tag.get_text(strip=True)

        data.append({
            "title": title,
            "date": date,
            "link": link
        })

df = pd.DataFrame(data).head(20)

print("📊 Filas a guardar:", len(df))

df.to_csv("data/raw.csv", index=False)

print("✅ raw.csv creado en la carpeta data/")
