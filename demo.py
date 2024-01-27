# Project scraping the the all time winter olymics medal table
from requests_html import HTMLSession
import pandas as pd

# Get the HTMLSession object
session = HTMLSession()
# Get the web page url
url = 'https://en.wikipedia.org/wiki/winter_Olympic_Games'
headers = {'User-Agent' : 'Mozilla/5.0'}

# Getting the http response
response = session.get(url, headers = headers)
print(response.status_code)
# Getting the page html of the web page
page_html = response.html
# finding the tables on the html page
tables = page_html.find('.wikitable')
for num, table in enumerate(tables):
    print(f'Table {num}:', table.find('tr', first = True).text.replace('\n', ' '))

table_medals = tables[1]
table_medals_df = pd.read_html(table_medals.html)[0]
print(table_medals_df)
