from bs4 import BeautifulSoup
import requests

url = 'https://www.cyoa.com/collections/bestsellers/products/time-travel-inn'

# headers={
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'max-age=0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
# }

response = requests.get(url=url)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
price = soup.find('span', id='price-field')
print(price.find('span', class_='money').text)