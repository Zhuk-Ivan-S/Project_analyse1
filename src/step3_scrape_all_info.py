import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib3.filepost import writer

URL = 'https://books.toscrape.com/catalogue/page-{}.html'

#Create CSV and save info into csv file
with open('../data/raw/books.csv','w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title','price','rating'])

    # take 50 pages in website and take all books
    for page in range(1,51):
        url = URL.format(page)
        print(f'Download page {page}')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #Find all articles for books
        books = soup.find_all('article', class_ = 'product_pod')
        for book in books:
            # Names of Books (atribut ' title ' in <a>)
            title = book.find('h3').find('a')['title']

            # Price
            price = book.find('p', class_='price_color').text
            #Rating (class = <p>)
            rating = book.find('p', class_='star-rating')['class'][1]

            writer.writerow([title, price, rating])

        # try to make a little pause for website (rest time)
        time.sleep(1)

print('All books are saved in "../data/raw/books.csv')
