import urllib.request
import urllib
import re

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

    def run(self,req):
        self.query = req.replace(' ', '+')
        request_url = 'https://www.bing.com/images/async?q=' + self.query \
                      + '&qft=' + 'filterui:photo-photo'
        request = urllib.request.Request(request_url, None, headers=self.headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf8')
        link = re.findall('murl&quot;:&quot;(.*?)&quot;', html)
        return link[0]
