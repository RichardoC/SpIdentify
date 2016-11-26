import  sklearn as sk
import glob
import numpy as np
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from sklearn.neural_network import MLPClassifier

spiders = glob.glob('./Spider/*')
non_spiders = glob.glob('./NonSpider/*')

SPimg = []
for sp in spiders:
    img = Image.open(sp).convert('L')
    width,height = img.size
    # if((width>=100) and (height>=100)):
    resized = scipy.misc.imresize(img,[20,20])
    SPimg.append(resized)

NSPimg = []
for sp in non_spiders:
    img = Image.open(sp)
    resized = scipy.misc.imresize(img,[100,100])
    NSPimg.append(resized)

testSize = int(0.75*len(SPimg)) + int(0.75*len(NSPimg))
trainSpid = int(0.75*len(SPimg))
trainNSpid = int(0.75*len(NSPimg))
checkSpid = int(0.25*len(SPimg))
checkNSpid = int(0.25*len(NSPimg))
testLabs = np.zeros(testSize)

testImgs = SPimg[0:trainSpid]
for i in range(0,trainSpid):
    testLabs[i] = 1
# testLabs = np.ones(int(0.75*len(SPimg)))

testImgs[trainSpid:testSize-1] = SPimg[0:trainNSpid]
# toAloc = -1*np.ones(trainNSpid)

for i in range(trainSpid,testSize):
    testLabs[i] = -1

testImgsA = np.array(testImgs)
TwoDim_dataset = testImgsA.reshape(testSize,-1)

#Now for a single layer perceptron with 3 nodes in the hidden layer
SLPClass = MLPClassifier(hidden_layer_sizes=(40,30))
SLPClass.fit(TwoDim_dataset,testLabs)

print SLPClass.loss_
toAdd = 23
testSP = SPimg[215:215+toAdd]
print spiders[215+toAdd]
testSPA = np.array(testSP,ndmin=4) #.tolist()
# testSP = np.array(testSP)
TwoDtestSP = testSPA.reshape(toAdd,-1)
# TwoDtestSP = TwoDtestSP.reshape(int(0.75*len(SPimg)),-1)
# testSPLabs = np.ones(np.shape(TwoDtestSP)[0])
checkSpidOnes = np.ones(toAdd)
testSLPSPScore = SLPClass.score(TwoDtestSP,checkSpidOnes)
# testSLPSPScore = SLPClass.score(TwoDim_dataset,testLabs)
print "Testing the SLP on spiders " , testSLPSPScore
#
testNSP = NSPimg[trainNSpid+1:]
TwoDtestNSP = np.array(testNSP).reshape(checkNSpid,-1)

minusOnes = []
minusOnes= np.zeros(checkNSpid)-np.ones(checkNSpid);
#
# for i in range(0,checkNSpid):
#     minusOnes[i] = -1

minusOnes = np.array(minusOnes)
#
testNSLPSPScore = SLPClass.score(TwoDtestNSP,minusOnes)
print "Testing the SLP on non-spiders " , testNSLPSPScore