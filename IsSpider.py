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

    with open('SLPClass.pkl', 'rb') as input:
        SLPClass = pickle.load(input)

    img = Image.open(fileLoc).convert('L')

    px = 20
    py = 10

    SPimg = []

    width, height = img.size
    if ((width >= px) and (height >= py)):
        resized = scipy.misc.imresize(img, [px, py])
        SPimg.append(resized)
    else:
        return 100

    Array = np.array(SPimg)
    Array = Array.reshape(1, -1)

    isSpid = SLPClass.predict(Array)

    return int(isSpid)

print isSpider("./EditedOutlineImages/NonSpider/1.jpg")