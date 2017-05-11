import urllib.request as ur
import json
import urllib.parse as up
import re
import os
from bs4 import BeautifulSoup
import sys
def downloadmovie(n):
	omdb_url = 'http://www.omdbapi.com/?t='
#n = sys.argv[1].lower()
	movie_name = up.quote_plus(n)
	req = omdb_url+movie_name

	#print('\n\n',req,'\n\n')

	data = ur.urlopen(req).read().decode('utf8')

	jdata = json.loads(data)
	yr = jdata['Year']


	yts_url = "https://yts.ag/movie/"

	mname = re.sub(r'[^\w\s]','',n)
	mname = mname.replace(" ","-")
	mname = mname + '-' + str(yr)

	yurl = yts_url+mname

	print('\n\n',yurl,'\n\n')

	yreq = ur.Request(yurl,headers={'User-Agent': 'Mozilla/5.0'})
	ydata = ur.urlopen(yreq)


	soup = BeautifulSoup(ydata,'lxml')
	magurls = [link["href"] for link in soup.find_all("a",href=True) if link['href'].startswith('magnet')]

	os.startfile(magurls[0])