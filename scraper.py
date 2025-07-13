import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "http://books.toscrape.com/"
page_url = "catalogue/page-1.html"
all_books = []

while page_url:
    print(f"Scraping: {page_url}")
    response = requests.get(base_url + page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        availability = book.find("p", class_="instock availability").text.strip()
        rating_class = book.find("p")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "Not Rated"

        # Get detail page URL
        detail_partial_url = book.h3.a["href"]
        detail_url = base_url + "catalogue/" + detail_partial_url.replace('../../../', '')

        # Request detail page
        detail_resp = requests.get(detail_url)
        detail_soup = BeautifulSoup(detail_resp.text, "html.parser")

        # Description
        desc_tag = detail_soup.find("meta", {"name": "description"})
        description = desc_tag["content"].strip() if desc_tag else "No description"

        # Category
        category = detail_soup.select_one("ul.breadcrumb li:nth-of-type(3) a").text.strip()

        # Product info table
        table = detail_soup.find("table", class_="table table-striped")
        rows = {row.th.text.strip(): row.td.text.strip() for row in table.find_all("tr")}
        upc = rows.get("UPC", "")
        num_reviews = rows.get("Number of reviews", "")

        all_books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "category": category,
            "description": description,
            "UPC": upc,
            "num_reviews": num_reviews
        })

    # Pagination
    next_btn = soup.find("li", class_="next")
    if next_btn:
        next_page = next_btn.a["href"]
        page_url = "catalogue/" + next_page
        time.sleep(1)  # be polite
    else:
        page_url = None

# Save data
df = pd.DataFrame(all_books)
df.to_csv("data/books_detailed.csv", index=False)
print(f"Scraped {len(all_books)} books with details.")