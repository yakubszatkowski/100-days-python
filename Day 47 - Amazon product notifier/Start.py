import requests
import smtplib
import os
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
price = float(f"{soup.find(name='span', class_='a-price-whole').getText()}{soup.find(name='span', class_='a-price-fraction').getText()}")
product_name = soup.find(name='span', class_='a-size-large product-title-word-break').getText().strip()

if price <= 100.00:
    msg = f'{product_name} is now ${price}!'
    msg = msg.encode("ascii", errors="ignore")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user='rtyrtyqweqwe39@gmail.com', password=os.environ.get('D32_gmail_app_pass'))
        connection.sendmail(
            from_addr='rtyrtyqweqwe39@gmail.com', to_addrs='yakub.szatkowski@gmail.com',
            msg=f'Subject: New Amazon Deal! \n\n {msg} \n{URL}')

