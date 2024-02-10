from bs4 import BeautifulSoup
import requests
import os
import smtplib

GMAIL_USER = 'mawwabkhank2006@gmail.com'
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
url = 'https://www.cyoa.com/collections/bestsellers/products/time-travel-inn'

response = requests.get(url=url)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
price_tag = soup.find('span', id='price-field')
price = float(price_tag.find('span', class_='money').text.strip('$'))
