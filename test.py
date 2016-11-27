# from bs4 import BeautifulSoup
import cgi

from bs4 import BeautifulSoup

import IsSpider
import urllib

testfile = urllib.URLopener()


url = 'index.html'
page = open(url)
soup = BeautifulSoup(page.read(), 'html.parser')
tag = soup.p


# output = soup.find_all('p')
# print(soup.prettify())

html = soup.prettify("utf-8")
with open("index.html", "wb") as file:
    file.write(html)

# dodgy bit (no local host):
form = cgi.FieldStorage()
while True:
    link =  form.getvalue('text')
    if link:
        print "link found"
        break

# tempImg = urllib.request.urlretrieve(link,'temp.jpg')
tempImg = testfile.retrieve(link,'temp.jpg')
output = IsSpider.isSpider('./temp.jpg') ###############################################################<<<-------- result of program

if output==1:
    text = 'Beware! There is a spider in the picture.'
elif output ==0:
    text = "No need to worry! There isn't a spider in the picture."
else:
    test = "Issue with the image/url"

tag.string = text
print(link)
