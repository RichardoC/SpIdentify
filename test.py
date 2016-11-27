from bs4 import BeautifulSoup
import re
import urllib.request
import cgi

url = 'index.html'
page = open(url)
soup = BeautifulSoup(page.read(), 'lxml')
tag = soup.p

output = False ###############################################################<<<-------- result of program

if output:
	text = 'Beware! There is a spider in the picture.'
else:
	text = "No need to worry! There isn't a spider in the picture."

tag.string = text
# output = soup.find_all('p')
# print(soup.prettify())

html = soup.prettify("utf-8")
with open("index.html", "wb") as file:
    file.write(html)

# dodgy bit (no local host):
while True:
	form = cgi.FieldStorage()
	link =  form.getvalue('text')
	if link: break

print(link)
