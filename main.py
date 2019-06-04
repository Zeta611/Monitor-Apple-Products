#!/usr/bin/env python

import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from getpass import getpass


def send_email(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(from_addr, password)
    server.send_message(msg)
    server.close()


if __name__ == "__main__":
    url = "https://www.apple.com/kr/shop/buy-mac/macbook-pro/15형"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)"
                             "AppleWebKit/605.1.15 (KHTML, like Gecko)"
                             "Version/12.1.1 Safari/605.1.15"}
    password = getpass("Type my Gmail password: ")

    while True:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        if str(soup).count("In Stock") <= 4:
            print(f"[{datetime.now()}] New Macbook Pro unavailable!")
            time.sleep(60)
            continue
        else:
            try:
                from_addr = "jaeho.jay.lee@gmail.com"
                to_addr = "tomtommy611@iCloud.com"
                subject = "맥북프로 2019년형 판매 알림"
                link = "https://www.apple.com/kr/shop/buy-mac/macbook-pro/15형"
                body = f"링크: {link}"
                send_email(from_addr, to_addr, subject, body)
                break
            except Exception as exception:
                print(f"Exception: {exception}\n")
