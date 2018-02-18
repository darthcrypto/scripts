#!/usr/bin/env/python

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.brainyquote.com/quote_of_the_day")
quotehtml = BeautifulSoup(page.content, 'html.parser')

quoteparser1 = quotehtml.find("a", attrs={"class":"b-qt qt_122774 oncl_q"}).text
quoteparser2 = quotehtml.find("a", attrs={"class":"bq-aut qa_122774 oncl_a"}).text

quote_of_the_day = '"'+quoteparser1+'"'+" \n -"+quoteparser2

print quote_of_the_day

###
#logic for manipulating quote ***VERIFIED THIS WORKS***
#quote = open("/root/scripts/projects/twitterbot/twitter-code/quote.txt","w")
#quote.write("Hello World")
#quote.close

