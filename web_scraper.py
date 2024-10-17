import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

book_list = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text.strip()
    availability = book.find('p', class_='instock availability').text.strip()
    book_list.append({'Title': title, 'Price': price, 'Availability': availability})

df = pd.DataFrame(book_list)

df.to_csv('books.csv', index=False)

print('Data has been scraped and saved to books.csv')