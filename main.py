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
title_tag = soup.find('div', class_='product-header')
title = title_tag.find('h1').text
description_tag = soup.find('div', class_='product-description')
description = description_tag.text

if price <= 10:
    msg = f"""
    Title: {title}
    Description: {description}
    Price: {price}
    Link: {url}
    """
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_USER,
            to_addrs=GMAIL_USER,
            msg=msg
        )