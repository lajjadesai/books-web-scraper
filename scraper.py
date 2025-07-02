import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

data = []
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    data.append({"quote": text, "author": author})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("data/quotes.csv", index=False)
print("Scraped and saved to data/quotes.csv")