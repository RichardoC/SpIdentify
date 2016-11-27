# # Hackkings 3.0 Image extraction from web page

# import urllib.request
# from bs4 import BeautifulSoup

# url, x = 'https://www.google.co.uk/search?q=spider+images&espv=2&biw=1280&bih=615&source=lnms&tbm=isch&sa=X&ved=0ahUKEwizgcWb9sbQAhVDLMAKHZYuBfcQ_AUIBigB#imgrc=_', []
# arrLink = [a for a, b in enumerate(url) if b == '/']
# soup = BeautifulSoup(urllib.request.urlopen(url), 'lxml')
# url = url[:arrLink[-1]]
# count = 0

# fileNo = 1

# for imgtag in soup.find_all('img'):
# 	x.append(imgtag['src'])
# 	print(imgtag['src'])

# for i in x:
# 	fileNo += 1
# 	temp = i.split('/')
# 	for cnt, j in enumerate(temp):
# 		if j != '.' and j != '..': count = cnt
# 	if count == 1: text = '/'.join(temp[1:])
# 	else: text = '/'.join(temp[count-1:])
# 	if temp[0] == '.': count -= 1
# 	indices = [a for a, b in enumerate(i) if b == '/']
# 	output = url[:arrLink[-count]] + '/' + text
# 	print(output)

# 	# urllib.request.urlretrieve(output, 'temp/'+str(fileNo)+'.jpg')

import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.google.co.uk/search?q=pyramid&biw=1280&bih=615&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj369XEgcfQAhWeHsAKHU68AX0Q_AUICCgB'

# page = open('tower.html', 'r').read()
page = requests.get(url).text
fileNo = 100
soup = BeautifulSoup(page, 'lxml')

for raw_img in soup.find_all('img'):
  link = raw_img.get('src')
  if link:
    print(link)
    urllib.request.urlretrieve(link, 'temp/'+str(fileNo)+'.jpg')
    fileNo += 1