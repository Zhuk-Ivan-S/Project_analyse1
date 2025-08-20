import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# take data
df = pd.read_csv('../data/clean/books_clean.csv')
#i want to create something lige dashboard and use subplot
fig, axes = plt.subplots(2,2,figsize=(13,10))
# lets see price distribution through a bar chart

sns.histplot(df['price'], bins = 15, kde= True, ax = axes[0,0])
axes[0,0].set_title('Books price distribution')
axes[0,0].set_xlabel('Price (£)')
axes[0,0].set_ylabel('Count of Books')

# analyze for rating of Books throught a bar chart
sns.histplot(df['rating'], bins=15, kde=True, ax = axes[0,1], color = 'red')
axes[0,1].set_title('Rating of Books on Website')
axes[0,1].set_xlabel('Rating from 1 to 5 stars')
axes[0,1].set_ylabel('Count of Books')

# lets make scatter plot for understanding correlation between price and rating of books
sns.regplot(x='rating', y = 'price',data = df, ax = axes[1,0], color = 'green')
axes[1,0].set_title('Correlation between rating and price')
axes[1,0].set_xlabel('Rating')
axes[1,0].set_ylabel('Price (£)')
# lets make box plot for understanding correlation between price and rating of books
sns.boxplot(x='rating', y = 'price',data = df, ax = axes[1,1], color ='yellow')
axes[1,1].set_title('Correlation between rating and price')
axes[1,1].set_xlabel('Rating')
axes[1,1].set_ylabel('Price (£)')

plt.tight_layout()
plt.show()
