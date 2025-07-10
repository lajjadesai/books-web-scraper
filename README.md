# 📚 Books to Scrape - Web Scraper

This Python web scraper extracts book data from [books.toscrape.com](http://books.toscrape.com), including:

- Title
- Price
- Availability
- Rating

The scraper automatically navigates all pages and saves the data to `data/books.csv`.

## 📦 Tech Stack

- Python
- BeautifulSoup
- Requests
- Pandas

## 🚀 How to Run

1. Clone the repo
2. Install dependencies  
   `pip install -r requirements.txt`
3. Run the scraper  
   `python scraper.py`
   
## 📊 Data Analysis & Visualizations
A detailed exploratory data analysis (EDA) was conducted on the scraped dataset using pandas, matplotlib, and seaborn. The notebook includes:

📉 Price Distribution: Most books are priced under £40, with a few high-priced outliers.

⭐ Ratings Breakdown: The majority of books are rated between 3 and 5 stars.

🗂️ Top Categories: Popular categories include Fiction, Science, and Historical Fiction.

💰 Average Price by Rating: Slight increase in average price for higher-rated books.

You can view the full notebook here:
notebooks/books_analysis.ipynb

## 🗂️ Output

The scraped data is saved to:
