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
px = 20
py = 10
for sp in spiders:
    img = Image.open(sp).convert('L')
    width,height = img.size
    if((width>=px) and (height>=py)):
        resized = scipy.misc.imresize(img,[px,py])
        SPimg.append(resized)
    else:
        print sp

NSPimg = []
for sp in non_spiders:
    img = Image.open(sp).convert('L')
    if((width>=px) and (height>=py)):
        resized = scipy.misc.imresize(img,[px,py])
        NSPimg.append(resized)
    else:
        print sp

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

# for i in range(trainSpid,testSize):
    # testLabs[i] = -1

testImgsA = np.array(testImgs)
TwoDim_dataset = testImgsA.reshape(testSize,-1)

result_array = []

for x in range(10,501,50):
    print "x = ",x
    for y in range (10,501,50):
        for z in range (10,501,50):
            # print
            # print "x = ",x," y = ",y," z = ",z
            # print

            #Now for a single layer perceptron with 3 nodes in the hidden layer
            SLPClass = MLPClassifier(hidden_layer_sizes=(x,y,z))
            SLPClass.fit(TwoDim_dataset,testLabs)

            # print SLPClass.loss_
            # toAdd = 23
            testSP = SPimg[trainSpid+1:]
            # print spiders[215+toAdd]
            testSPA = np.array(testSP) #.tolist()
            # testSP = np.array(testSP)
            TwoDtestSP = testSPA.reshape(checkSpid,-1)
            # TwoDtestSP = TwoDtestSP.reshape(int(0.75*len(SPimg)),-1)
            # testSPLabs = np.ones(np.shape(TwoDtestSP)[0])
            checkSpidOnes = np.ones(checkSpid)
            testSLPSPScore = SLPClass.score(TwoDtestSP,checkSpidOnes)
            # testSLPSPScore = SLPClass.score(TwoDim_dataset,testLabs)
            # print "Testing the SLP on spiders " , testSLPSPScore
            #
            testNSP = NSPimg[trainNSpid+1:]
            TwoDtestNSP = np.array(testNSP).reshape(checkNSpid,-1)

            # minusOnes = []
            # minusOnes= np.zeros(checkNSpid)#-np.ones(checkNSpid);
            #
            # for i in range(0,checkNSpid):
            #     minusOnes[i] = -1

            # minusOnes = np.array(minusOnes)
            #
            testNSLPSPScore = SLPClass.score(TwoDtestNSP,np.zeros(checkNSpid))
            # print "Testing the SLP on non-spiders " , testNSLPSPScore
            result_array.append([x,y,z,SLPClass.loss_,testSLPSPScore,testNSLPSPScore])

maximum_non_spiders = -1
maximum_non_spiders_result = []
for res in result_array:
    if res[-1]>maximum_non_spiders:
       maximum_non_spiders = res[-1]
       maximum_non_spiders_result = res


print res