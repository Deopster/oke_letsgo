import posixpath
import random
import time
import urllib.request
import urllib
import re
import imghdr
import os
from pathlib import Path
from LOLES import photoshop
class Bing:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko)'
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.3,*;q=0.7',
      'Accept-Encoding': 'none',
      'Accept-Language': 'ru,en;q=0.9',
      'Connection': 'keep-alive'}
        self.download_count = 0

    def save_image(self, link):
        try:
            request = urllib.request.Request(link, None, self.headers)
            image = urllib.request.urlopen(request, timeout=60).read()
            if not imghdr.what(None, image):
                print('[Error]Invalid image, not saving {}\n'.format(link))
                raise ValueError('Invalid image, not saving {}\n'.format(link))
            with open("./files/" + str(self.download_count) + ".jpg", 'wb') as f:
                f.write(image)
            self.download_count += 1
        except Exception as e:
            print('Error 403 bot check for ' + link, e)
    def run(self,req):
        self.query = req.replace(' ', '+').replace('…', '').replace('@', '').replace('(', '').replace(')', '')
        request_url = 'https://www.bing.com/images/async?q=' + self.query \
                      + '&qft=' + 'filterui:photo-photo'
        request = urllib.request.Request(request_url, None, headers=self.headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf8')
        link = re.findall('murl&quot;:&quot;(.*?)&quot;', html)
        while True:
            if self.save_image(link[random.randint(0,len(link)-1)],self.query):
                break

    def save_image(self, link,req):
        try:
            request = urllib.request.Request(link, None, self.headers)
            image = urllib.request.urlopen(request, timeout=2).read()
            if not imghdr.what(None, image):
                print('[Error]Invalid image, not saving {}\n'.format(link))
                raise ValueError('Invalid image, not saving {}\n'.format(link))
            filename="./files/"+str(self.download_count)+".jpg"
            with open(filename, 'wb') as f:
                f.write(image)
            photoshop(str(self.download_count)+".jpg",req.replace("+"," "))
            self.download_count += 1
            return True
        except Exception as e:
            print('Error 403 bot check for '+link, e)
            return False



