from bs4 import BeautifulSoup
import requests

url = 'https://www.cyoa.com/collections/bestsellers/products/time-travel-inn'

response = requests.get(url=url)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
price = soup.find('span', id='price-field')
price = price.find('span', class_='money').text

print(price)