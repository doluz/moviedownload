import urllib.request as ur
import json
import urllib.parse as up
import re
import os
from bs4 import BeautifulSoup

omdb_url = 'http://www.omdbapi.com/?t='
n = input('Enter Movie Name\n')
movie_name = up.quote_plus(n)
req = omdb_url+movie_name

data = ur.urlopen(req).read().decode('utf8')

jdata = json.loads(data)
yr = jdata['Year']


yts_url = "https://yts.ag/movie/"

mname = re.sub(r'[^\w\s]',' ',n)
mname = mname + ' ' + str(yr)
mname = mname.replace(' ','-')
yurl = yts_url+mname

yreq = ur.Request(yurl,headers={'User-Agent': 'Mozilla/5.0'})
ydata = ur.urlopen(yreq)

soup = BeautifulSoup(ydata,'lxml')
magurls = [link["href"] for link in soup.find_all("a",href=True) if link['href'].startswith('magnet')]

os.startfile(magurls[0])