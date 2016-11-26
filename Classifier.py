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
    img = Image.open(sp)
    resized = scipy. misc.imresize(img,[100,100])
    SPimg.append(resized)

NSPimg = []
for sp in non_spiders:
    img = Image.open(sp)
    resized = scipy.misc.imresize(img,[100,100])
    NSPimg.append(resized)

testSize = int(0.75*len(SPimg)) + int(0.75*len(NSPimg))
checkSpid = int(0.25*len(SPimg))
checkNSpid = int(0.25*len(NSPimg))
testLabs = np.zeros(testSize)

testImgs = SPimg[0:int(0.75*len(SPimg))]
for i in range(0,int(0.75*len(NSPimg))):
    testLabs[i] = 1
# testLabs = np.ones(int(0.75*len(SPimg)))

testImgs[len(testImgs):(len(testImgs)+(int)(0.75*len(NSPimg)))] = SPimg[0:(int)(0.75*len(NSPimg))]
toAloc = -1*np.ones(int(0.75*len(NSPimg)))

for i in range(int(0.75*len(NSPimg)),(len(testImgs)-2)):
    testLabs[i] = -1

testImgs = np.array(testImgs)
TwoDim_dataset = testImgs.reshape(testSize,-1)

#Now for a single layer perceptron with 3 nodes in the hidden layer
SLPClass = MLPClassifier(hidden_layer_sizes=(3,))
SLPClass.fit(TwoDim_dataset,testLabs)

print SLPClass.loss_
testSP = np.array(SPimg[(int)(0.75*len(SPimg))+1:-1])
testSP = testSP.reshape(checkSpid,-1)
testSLPSPScore = SLPClass.score(testSP,np.ones(len(testSP)))
print "Testing the SLP on spiders " , testSLPSPScore
#
# testNSP = NSPimg[(int)(0.75*len(NSPimg))+1:-1]
#
# # testNSLPSPScore = SLPClass.score(testNSP,np.ones(len(testNSP)))
# print "Testing the SLP on non-spiders " , testNSLPSPScore