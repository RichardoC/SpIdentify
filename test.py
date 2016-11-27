from bs4 import BeautifulSoup
import cgi
import IsSpider
import urllib

testfile = urllib.URLopener()
testfile.retrieve("http://randomsite.com/file.gz", "file.gz")

url = 'index.html'
page = open(url)
soup = BeautifulSoup(page.read(), 'lxml')
tag = soup.p


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

tempImg = urllib.request.urlretrieve(link,'temp.jpg')

output = IsSpider.isSpider('./temp.jpg') ###############################################################<<<-------- result of program

if output==1:
	text = 'Beware! There is a spider in the picture.'
elif output ==0:
    text = "No need to worry! There isn't a spider in the picture."
else:
	test = "Issue with the image/url"

tag.string = text
print(link)
