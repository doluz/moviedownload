import moviedown
import urllib.request as ur
import json
import urllib.parse as up
import re
import os
from bs4 import BeautifulSoup
import sys

print("Search for movie to download:")
movie = input()
movie = movie.replace(" ","%20")
yurl = 'https://yts.ag/browse-movies/'+movie+'/all/all/0/latest'
#yurl = 'https://yts.ag/'
print(yurl)
yreq = ur.Request(yurl,data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
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


