#!/usr/bin/env/python

import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('p')[0].get_text()

print results
