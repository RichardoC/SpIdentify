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


while True:
	form = cgi.FieldStorage()
	link =  form.getvalue('text')
	if link: break

print(link)

































# import html
# import sys
# from subprocess import Popen, PIPE, STDOUT, DEVNULL
# from textwrap import dedent

# from flask import Flask, Response # $ pip install flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     def g():
#         yield "<!doctype html><title>Stream subprocess output</title>"

#         with Popen([sys.executable or 'python', '-u', '-c', dedent("""\
#             from random import randint
#             HT = {0: True, 1: False}
#             print(HT[randint(0,1)])            
#             """)], stdin=DEVNULL, stdout=PIPE, stderr=STDOUT,
#                    bufsize=1, universal_newlines=True) as p:
#             for line in p.stdout:
#                 yield "<code>{}</code>".format(html.escape(line.rstrip("\n")))
#                 yield "<br>\n"
#     return Response(g(), mimetype='text/html')

# if __name__ == "__main__":
#     import webbrowser
#     webbrowser.open('http://localhost:23423') # show the page in browser
#     app.run(host='localhost', port=23423, debug=True) # run the server

# # n = int(input())
# # arrNum, total, boolStart = [], 1, False

# # for i in range(100000):
# # 	arrNum.append(randint(-100,100))

# # for i in range(len(arrNum)-1, -1, -1):
# # 	if not boolStart and arrNum[i] < 0:
# # 		boolStart = True
# # 		total += -arrNum[i]
# # 	elif boolStart and arrNum[i] < 0:
# # 		total += -arrNum[i]
# # 	elif boolStart and arrNum[i] > 0:
# # 		total -= arrNum[i]
# # 		if total < 0:
# # 			total = 1

# # print(total)

# # # filename = 'test.in'
# # # fileWrite = open('test.out','w')

# # # with open(filename) as f:
# # #   content = [x.strip('\n') for x in f.readlines()]

# # # if len(''.join(content[2:])) == 0:
# # #   print('YES', file=fileWrite)
# # #   exit()

# # # m, n = int(content[0]), int(content[1])
# # # arrDislike, dictCheck = [], {}

# # # for i in range(m):
# # #   dictCheck[i] = []

# # # for data in content[2:]:
# # #   x = data.split()
# # #   arrDislike += [[int(i) for i in x]]

# # # arrRooms = [[j for j in range(1, n+1)] for i in range(m)]

# # # for i in range(n):
# # #   for count, room in enumerate(arrRooms):
# # #     if (i+1) in room:
# # #       if list(set(arrDislike[i]).intersection(dictCheck[count])) == []:
# # #         arrRooms[count] = list(set(arrRooms[count])-set(arrDislike[i]))
# # #         dictCheck[count].append(i+1)
# # #         break

# # # arrNums = [item for sublist in list(dictCheck.values()) for item in sublist]

# # # if len(arrNums) == n:
# # #   print('YES', file=fileWrite)
# # # else:
# # #   print('NO', file=fileWrite)

# # # # Hackerrank - task 2
# # # n,k = input().strip().split(' ')
# # # n,k = [int(n),int(k)]
# # # x = [int(x_temp) for x_temp in input().strip().split(' ')]
# # # x.sort()
# # # output, y = 0, x[:]

# # # while y:
# # #   for index, i in enumerate(y):
# # #     if y[0] < i-k:
# # #       break
# # #     temp = index
# # #   output += 1
# # #   upperBound = y[temp]+k
# # #   for i in y[:]:
# # #     if i <= upperBound:
# # #       y.remove(i)
# # #     else:
# # #       break

# # # print(output)

# # # Hackerrank task 3

# # # def cycleThrough(i, arrx):
# # #   extraTime, counter, lenarrx = 0, 0, len(arrx)
# # #   for j in range(lenarrx):
# # #     if arrx[(i+j)%len(arrx)] <= extraTime:
# # #       extraTime += 1
# # #       counter += 1
# # #     else:
# # #       extraTime += 1
# # #   return counter

# # # n = int(input())
# # # x = [int(x_temp) for x_temp in input().strip().split(' ')]

# # # maxChecked = 0

# # # for i in range(len(x)):
# # #   val = cycleThrough(i, x)
# # #   if val > maxChecked:
# # #     arrOutput = []
# # #     maxChecked = val
# # #     arrOutput.append(i+1)
# # #   elif val == maxChecked:
# # #     arrOutput.append(i+1)

# # # print(min(arrOutput))
# # import random
# # # n = int(input())
# # # x = [int(x_temp) for x_temp in input().strip().split(' ')]

# # # n = int(input())
# # n = random.randint(4,10)
# # x = [random.randint(0,n) for _ in range(n)]
# # print('n:', n, x)
# # # highest = 0

# # for i in [0]+list(range(n-1,0,-1)):
# #   a = [((i+j)%n)-num for j, num in enumerate(x)]
# #   counter = sum(x >= 0 for x in a)
# #   # highest = max(highest,counter)
# #   print(counter, a, [(i+j)%n for j in range(n)])

# # # print(highest)
# # # C = [a - b for a, b in zip(A, B)]