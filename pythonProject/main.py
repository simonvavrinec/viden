import requests
from bs4 import BeautifulSoup

url = 'https://www.coingecko.com/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

crypto_table = soup.find('table', class_='sort table mb-0 text-sm text-lg-normal table-scrollable')

for currency in crypto_table.find_all('tbody'):
    rows = currency.find_all('tr')

    for row in rows:
        crypto_name = row.find('span', class_='lg:tw-flex font-bold tw-items-center tw-justify-between').text
        crypto_price = row.find('span', class_='no-wrap').text
        print(crypto_name + crypto_price)
