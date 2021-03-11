import requests
import sys
import os
import QWebView
from collections import deque
from bs4 import BeautifulSoup

class Browser:
    def __init__(self, url)
        self.url = url


    def get_page(self):  # creates an url and extracts text from it
        url = f'https://{self.address}'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                     "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        try:
            r = requests.get(url, headers={'User-Agent': user_agent})
        except requests.exceptions.ConnectionError:
            print('Error: Incorrect URL')
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            print(soup)

page = Browser
page.get_page()
