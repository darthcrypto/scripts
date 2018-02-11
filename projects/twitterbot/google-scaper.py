#!/usr/bin/env/python

from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')
image_type="ActiOn"
query="south+park"
url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi-6vHa35vZAhXMjVkKHUkNB8gQ_AUICygC&biw=682&bih=596"
print url
DIR="/tmp/southpark"
header={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = get_soup(url,header)

ActualImages=[] 
for a in soup.find_all("div",{"class":"rg_meta"}):
    link, Type=json.loads(a.text)["ou"] ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print "there are total" , len(ActualImages),"images"

if not os.path.exists(DIR):
   os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
      os.mkdir(DIR)

for i , (img , Type) in enumerate( ActualImages[:50]):
    try:
         req = urllib2.Request(img, headers={'User-Agent' : header})
         raw_img = urllib2.urlopen(req).read()

         cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
         print cntr
         if len(Type)==0:
            f = open(os.path.join(DIR + "_" + str(cntr)+".jpg"), 'wb')
         else:
            f = open(os.path.join(DIR + "_"+ str(cntr)+"."+Type), 'wb')
       
         f.write(raw_img)
         f.close()
    except Exception as e:
        print "could not load : "+img
        print e    



#what i be workin wit
#https://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search
