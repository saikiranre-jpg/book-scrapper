import requests
from bs4 import BeautifulSoup

link = 'https://books.toscrape.com/catalogue/page-1.html'
res = requests.get(link)

soup = BeautifulSoup(res.text, 'html.parser')
data = []

for sp in soup.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3'):
        
    img_link   = 'https://books.toscrape.com/' + sp.find('img').get('src')[3:]
    book_link  = 'https://books.toscrape.com/catalogue/' + sp.find_all('a')[-1].get('href')
    title      = sp.find_all('a')[-1].get('title')
    rating     = sp.find('p').get('class')[-1]
    price      = sp.find('p',class_ = 'price_color').text[2:]
    stock      = sp.find('p', class_ = 'instock availability').text.strip()
    
    
    data.append([title, rating, price, stock, book_link, img_link])
len(data)
data[0]

##Scraping data from multiple pages


import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
data = []

for i in tqdm(range(1,51)):        # Going through each page one by one

    link = 'https://books.toscrape.com/catalogue/page-' + str(i) + '.html'     # Creating link for each page

    res = requests.get(link)                                                   # Sending Request to the link
    soup = BeautifulSoup(res.text, 'html.parser')                              # Creating a soup for that page
    
    
    for sp in soup.find_all('li', class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3'):
    
        img_link   = 'https://books.toscrape.com/' + sp.find('img').get('src')[3:]
        book_link  = 'https://books.toscrape.com/catalogue/' + sp.find_all('a')[-1].get('href')
        title      = sp.find_all('a')[-1].get('title')
        rating     = sp.find('p').get('class')[-1]
        price      = sp.find('p',class_ = 'price_color').text[2:]
        stock      = sp.find('p', class_ = 'instock availability').text.strip()

        data.append([title, rating, price, stock, book_link, img_link])        # Saving scraped data in a list
len(data)
df = pd.DataFrame(data, columns = ['title', 'rating', 'price', 'stock', 'book_link','img_link'])
df.head()
df.to_csv('books.csv', index = False)


import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup

df = pd.read_csv('books.csv')
df.head()
data = []

for link in tqdm(df['book_link']):
    
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    typ = soup.find('ul', class_ = 'breadcrumb').find_all('a')[2].text
    
    temp = soup.find('table', class_ = 'table table-striped').find_all('td')
    
    upc      = temp[0].text
    price_x  = temp[2].text[2:]
    price_i  = temp[3].text[2:]
    tax      = temp[4].text[2:]
    qn       = temp[5].text
    reviews  = temp[6].text
    
    data.append([typ, price_x, price_i, tax, qn, upc, reviews])
df = pd.DataFrame(data, columns = ['category','price_e_tax', 'price_i_tax', 'tax', 'quantity', 'upc', 'reviews'])

df.head()
df.to_csv('data.csv', index = False)


import pandas as pd

df_1 = pd.read_csv('books.csv')
df_2 = pd.read_csv('data.csv')
df_1.head()
df_2.head()
### 1) Creating New DataFrame
df = pd.DataFrame()

df['title']         = df_1['title']
df['upc']           = df_2['upc']
df['category']      = df_2['category']
df['price_e_tax']   = df_2['price_e_tax']
df['price_i_tax']   = df_2['price_i_tax']
df['tax']           = df_2['tax']
df['rating']        = df_1['rating']
df['reviews']       = df_2['reviews']
df['quantity']      = df_2['quantity']
df['stock']         = df_1['stock']

df['book_link']     = df_1['book_link']
df['img_link']      = df_1['img_link']
df.head()
df.to_csv('final.csv', index = False)
