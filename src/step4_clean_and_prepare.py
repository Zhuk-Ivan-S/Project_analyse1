import pandas as pd
import numpy as np
# Reed a csv file and convert in DataFrame
df = pd.read_csv('../data/raw/books.csv')
#chek and show first 5 rows of dataframe
print(df.head(5))

#now i want to clean and prapare all rows (example price wothout 'Â£' and in int, rating from 'str' to 'int')
print(df.duplicated()) #- check for duplicated data
print(df.size)
#print(df.dtypes) #- all types are object i want to change it for statistic ( check )
df['price'] = df['price'].str.replace('Â£','').astype(float)

#change rating from str to int
rating_map = {'One':1, 'Two':2,'Three':3,'Four':4,'Five':5}
df['rating'] = df['rating'].map(rating_map)
# delete some spaces in title of books
df['title'] = df['title'].str.strip()

#now see standart statistic
print(df.describe())
print(df.info())
#save cleaned data
df.to_csv('../data/clean/books_clean.csv')
print('Data ready for analyze and saved to "../data/clean/books_clean.csv"')

