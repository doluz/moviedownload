import moviedown
import urllib.request as ur
import json
import urllib.parse as up
import re
import os
from bs4 import BeautifulSoup
import sys
yurl = 'https://yts.ag/'
yreq = ur.Request(yurl,headers={'User-Agent':'Mozilla/5.0'})
ydata = ur.urlopen(yreq)

soup = BeautifulSoup(ydata,'lxml')

titles = soup.find_all('a', class_='browse-movie-title')

i = 0;
print('\n\n')
for title in titles:
	print(i,title.string)
	i+=1

n = int(input('\nEnter movie number to download:- '))

moviedown.downloadmovie(titles[n].string.lower())


