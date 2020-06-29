import requests
import smtplib
import time
from bs4 import BeautifulSoup


URL = 'https://www.amazon.com/Wyze-1080p-Indoor-Camera-Vision/dp/B07DGR98VQ/ref=zg_bs_photo_home_1?_encoding=UTF8&psc=' \
      '1&refRID=C5KJYTERGZZN3TM7TH99'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find(id="productTitle").get_text(strip=True)
    # stripped_title = title[0:18]
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:3])

    if converted_price < 39.0:
        send_mail()
    # print(stripped_title)
    print(converted_price)
# check_price()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('(email)', '(2FA token)') #

    subject = "Price has fell down"
    body = 'Wyze Cam Pan 1080p: https://www.amazon.com/Wyze-1080p-Indoor-Camera-Vision/dp/B07DGR98VQ/ref=zg_bs_photo_home_1?_encoding=UTF8&psc=' \
      '1&refRID=C5KJYTERGZZN3TM7TH99'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "(receiver_email)",
        msg
    )
    print("email sent")

    server.quit()

while(True):
    check_price()
    time.sleep(86400) # one day: 86400 secs