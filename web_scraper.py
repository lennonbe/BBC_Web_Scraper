from bs4 import BeautifulSoup as bs
import cv2
from PIL import Image, ImageDraw
import os
import requests
import discord
import qrcode
import numpy as np
import pandas as pd
import json
import time

def scrape_articles():
    cmc = requests.get('https://www.bbc.co.uk/news/technology')
    soup = bs(cmc.content, 'html.parser')

    articles = soup.find_all('div', class_='gs-c-promo-body gs-u-mt@xxs gs-u-mt@m gs-c-promo-body--flex gs-u-mt@xs gs-u-mt0@xs gs-u-mt@m gel-1/2@xs gel-1/1@s')
    links = []

    for article in articles:
        links.append("https://www.bbc.co.uk" + str(article.a.get('href')))

    string = ""
    count = 1
    for e in links:
        string += (str(e))
        string += '\n'

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(str(e))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('Images\Image' + str(count) + '.png')
        count += 1

    f = open("Links.txt", "w")
    f.write(string)
    f.close()
    print('Sucessful scraping. Process sleeping\n')

if __name__ == '__main__':
    while True:
        scrape_articles()
        time_wait = 0.5
        time.sleep(time_wait * 60)