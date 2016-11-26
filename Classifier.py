import  sklearn as sk
import glob
import numpy as np
import matplotlib.pyplot as plt
import scipy
from PIL import Image


spiders = glob.glob('./Spider/*')
non_spiders = glob.glob('./NonSpider/*')

SPimg = []
for sp in spiders:
    img = Image.open(sp)
    resized = scipy. misc.imresize(img,[100,100])
    SPimg.append(resized)


NSPimg = []

for sp in non_spiders:
    img = Image.open(sp)
    resized = scipy.misc.imresize(img,[100,100])
    NSPimg.append(resized)

testImgs = SPimg[0:int(0.75*len(SPimg))]
testLabs = np.ones(int(0.75*len(SPimg)))

testImgs[len(testImgs):(len(testImgs)+(int)(0.75*len(NSPimg)))] = SPimg[0:(int)(0.75*len(NSPimg))]
testLabs[len(testLabs):(len(testLabs)+(int)(0.75*len(NSPimg)))] = - np.ones(int(0.75*len(NSPimg)))



#Now for a single layer perceptron with 3 nodes in the hidden layer
SLPClass = sk.MLPClassifier(hidden_layer_sizes=(3,))
SLPClass.fit(testImgs,testLabs)

testSP = SPimg[(int)(0.75*len(SPimg))+1:-1]
testSLPSPScore = SLPClass.score(testSP,np.ones(len(testSP)))
print "Testing the SLP on spiders " , testSLPSPScore

testNSP = NSPimg[(int)(0.75*len(NSPimg))+1:-1]
testNSLPSPScore = SLPClass.score(testNSP,np.ones(len(testNSP)))
print "Testing the SLP on non-spiders " , testNSLPSPScore