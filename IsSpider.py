import glob

import numpy as np
import scipy
from PIL import Image
import sys

import pickle

# args =  sys.argv

# print args

# fileLoc = "./EditedOutlineImages/Spider/_86087350_028938243-1.jpg"
def isSpider(location):
    fileLoc = location #= "./EditedOutlineImages/NonSpider/1.jpg"

    thresholdLow = 150
    thresholdHigh = 255

    with open('SLPClass.pkl', 'rb') as input:
        SLPClass = pickle.load(input)

    img = Image.open(fileLoc).convert('L')
    OutLineImg = img.point(lambda i: i < thresholdLow and thresholdHigh)

    px = 20
    py = 10

    SPimg = []

    width, height = OutLineImg.size
    if ((width >= px) and (height >= py)):
        resized = scipy.misc.imresize(OutLineImg, [px, py])
        SPimg.append(resized)
    else:
        return 100

    Array = np.array(SPimg)
    Array = Array.reshape(1, -1)

    isSpid = SLPClass.predict(Array)

    return int(isSpid)
print "1 = spider, 0 = non spider"
print "testing on a non spider image",isSpider("./EditedOutlineImages/NonSpider/1.jpg")
print "testing on a spider image ",isSpider("./EditedOutlineImages/Spider/_86087350_028938243-1.jpg")

print "spiderman", isSpider("/Users/richardf/Downloads/spiderman.jpg")