#!/usr/bin/env/python

import requests
from bs4 import BeautifulSoup

imdb = requests.get("http://www.imdb.com/list/ls062249377/")

imdbhtml = BeautifulSoup(imdb.content, 'html.parser')

imdbparser = imdbhtml.find_all("div", attrs={"class":"lister-item-content"})

for i in imdbparser:
   greatmovie = i.find('a').string
   print greatmovie

