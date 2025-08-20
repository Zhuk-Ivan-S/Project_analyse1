from bs4 import BeautifulSoup

# Read saved HTML file
with open('../data/raw/book_S.html', 'r', encoding='utf-8') as file:
    html = file.read()

#Create object BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Name of the Book
title = soup.find('h1').text
#Price
price = soup.find('p', class_ = 'price_color').text
#Rating
rating_tag = soup.find('p', class_ = 'star-rating')
rating = rating_tag['class'][1]

print('Name:', title)
print('Price:', price)
print('Rating:', rating)