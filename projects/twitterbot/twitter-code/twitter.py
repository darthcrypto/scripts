#!/usr/bin/env/python

from TwitterAPI import TwitterAPI
from secrets import *

def main():
  api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
  file = open('/root/scripts/projects/twitterbot/Pictures/south+park/ActiOn_1.jpg', 'rb')
  data = file.read()
  r = api.request('statuses/update_with_media', {'status':'helloworld'}, {'media[]': data})
  print(r.status_code)

if __name__ == "__main__":
  main()

