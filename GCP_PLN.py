import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/cena-zlota/"
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')

print('Classes of each table:')
for table in soup.find_all('table'):
    print(table.get('class'))

tables = soup.find_all('table')

table = soup.find('table', class_='table table-hover')

