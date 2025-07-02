import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "http://books.toscrape.com/"
page_url = "catalogue/page-1.html"
all_books = []

while page_url:
    response = requests.get(base_url + page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        availability = book.find("p", class_="instock availability").text.strip()
        rating_class = book.find("p")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "Not Rated"

        all_books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    # Find next page link
    next_button = soup.find("li", class_="next")
    if next_button:
        next_page = next_button.a["href"]
        page_url = "catalogue/" + next_page
        time.sleep(1)  # polite pause between requests
    else:
        page_url = None

# Save to CSV
df = pd.DataFrame(all_books)
df.to_csv("data/books.csv", index=False)
print(f"Scraped {len(all_books)} books. Saved to data/books.csv")