# import required modules
import requests
from bs4 import BeautifulSoup
import csv
import time
from pathlib import Path

# 1. Set up a polite User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
}

# 2. Target URL
url = "https://books.toscrape.com/"

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch page: {e}")
    exit()

# 3. Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# 4. Find book containers
books = soup.find_all("article", class_="product_pod")

# Display first 8 book titles
print("First 8 book titles:")
print("-" * 60)
for book in books[:8]:
    print(book.h3.a["title"])

# 5. Combine title and price safely
book_data = []

for book in books:
    title = book.h3.a["title"].strip()
    price = book.find("p", class_="price_color").get_text(strip=True)
    book_data.append([title, price])

# 6. Build directory safely
files_dir = Path.cwd() / "files" / "books"
files_dir.mkdir(parents=True, exist_ok=True)

# 7. Save to CSV
csv_file = files_dir / "books.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    writer.writerows(book_data)

# Inform the user clearly
print("\n✅ Data saved successfully!")
print(f"📁 File location: {csv_file.resolve()}")
print(f"📊 Total books scraped: {len(book_data)}")

