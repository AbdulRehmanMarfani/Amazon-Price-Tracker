import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import os


SMTP_ADDRESS = "smtp.gmail.com"
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")  
url = # Enter The Amazon Item URL Here
target_price = # Enter your required maximum price here

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Opera\";v=\"119\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()  
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("span", id="productTitle")
title = title.text.strip()

price = soup.find("span", class_="a-price-whole")
price = price.text
price += soup.find("span", class_="a-price-fraction").text
price = float(price)

if price < target_price:
    message = f"Price of {title} dropped to {price}!"
    email_msg = EmailMessage()
    email_msg["Subject"] = "🚨🚨🚨 Price Alert!"
    email_msg["From"] = EMAIL_ADDRESS
    email_msg["To"] = EMAIL_ADDRESS
    email_msg.set_content(message)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.send_message(email_msg)
