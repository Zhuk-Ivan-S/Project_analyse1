import requests

# URL for one book from Books tor scrape (all is legal)
url = 'https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'

# Send request
response = requests.get(url)

# Check for request status
print('Status code:' , response.status_code)

# Lets see first 300 sumbols

print(response.text[:300])

#and save this part in data
with open('../data/raw/book_S.html', 'w' , encoding='utf-8') as file:
    file.write(response.text)
print(('HTML saved in raw data'))