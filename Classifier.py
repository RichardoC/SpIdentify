import glob

import numpy as np
import scipy
from PIL import Image
from sklearn.neural_network import MLPClassifier

spiders = glob.glob('./EditedOutlineImages/Spider/*')
more = glob.glob('./EditedOutlineImages/BigSpiders/*')
spiders[len(spiders):len(spiders)+len(more)] = more
# spiders.append(glob.glob('./Editedtopdown/*'))
more = glob.glob('./EditedOutlineImages/topdown/*')
spiders[len(spiders):len(spiders)+len(more)] = more

non_spiders = glob.glob('./EditedOutlineImages/NonSpider/*')
# more = glob.glob('./EditedOutlineImages/Memes/*')
# non_spiders[len(non_spiders):len(non_spiders)+len(more)] = more

SPimg = []
px = 20
py = 10
for sp in spiders:
    img = Image.open(sp).convert('L')
    width, height = img.size
    if ((width >= px) and (height >= py)):
        resized = scipy.misc.imresize(img, [px, py])
        SPimg.append(resized)
    else:
        print sp

NSPimg = []
for sp in non_spiders:
    img = Image.open(sp).convert('L')
    if ((width >= px) and (height >= py)):
        resized = scipy.misc.imresize(img, [px, py])
        NSPimg.append(resized)
    else:
        print sp

testSize = int(0.75 * len(SPimg)) + int(0.75 * len(NSPimg))
trainSpid = int(0.75 * len(SPimg))
trainNSpid = int(0.75 * len(NSPimg))
checkSpid = int(0.25 * len(SPimg))
checkNSpid = int(0.25 * len(NSPimg))
testLabs = np.zeros(testSize)

testImgs = SPimg[0:trainSpid]
for i in range(0, trainSpid):
    testLabs[i] = 1
# testLabs = np.ones(int(0.75*len(SPimg)))

testImgs[trainSpid:testSize - 1] = SPimg[0:trainNSpid]
# toAloc = -1*np.ones(trainNSpid)

# for i in range(trainSpid,testSize):
# testLabs[i] = -1

testImgsA = np.array(testImgs)
TwoDim_dataset = testImgsA.reshape(testSize, -1)


# for x in range(10,501,50):
#     print "x = ",x

testSLPSPScore = 0
testNSLPSPScore = 0

# print
# print "x = ",x," y = ",y," z = ",z
# print

# print SLPClass.loss_
# toAdd = 23
testSP = SPimg[trainSpid + 1:]
# print spiders[215+toAdd]
testSPA = np.array(testSP)  # .tolist()
# testSP = np.array(testSP)
TwoDtestSP = testSPA.reshape(checkSpid, -1)
# TwoDtestSP = TwoDtestSP.reshape(int(0.75*len(SPimg)),-1)
# testSPLabs = np.ones(np.shape(TwoDtestSP)[0])
checkSpidOnes = np.ones(checkSpid)


# testSLPSPScore = SLPClass.score(TwoDim_dataset,testLabs)
# print "Testing the SLP on spiders " , testSLPSPScore
#
testNSP = NSPimg[trainNSpid + 1:]
TwoDtestNSP = np.array(testNSP).reshape(checkNSpid, -1)

# minusOnes = []
# minusOnes= np.zeros(checkNSpid)#-np.ones(checkNSpid);
#
# for i in range(0,checkNSpid):
#     minusOnes[i] = -1

# minusOnes = np.array(minusOnes)
#

SLPClass = MLPClassifier(hidden_layer_sizes=(160, 80, 10))
i = 0
while((testSLPSPScore+testNSLPSPScore)<1.6) and i<1000:
    # for x in range(1,100):
    i += 1
    # Now for a single layer perceptron with 3 nodes in the hidden layer

    SLPClass.fit(TwoDim_dataset, testLabs)

    testSLPSPScore = SLPClass.score(TwoDtestSP, checkSpidOnes)
    testNSLPSPScore = SLPClass.score(TwoDtestNSP, np.zeros(checkNSpid))

    # print "Testing the SLP on non-spiders " , testNSLPSPScore
    # result_array.put([x, y, z, SLPClass.loss_, testSLPSPScore, testNSLPSPScore])


    print SLPClass.loss_, testSLPSPScore, testNSLPSPScore
    # print "did all loops"
# print
# print SLPClass.intercepts_
# print
# print SLPClass.coefs_
print np.size(SLPClass.intercepts_)
print np.size(SLPClass.coefs_)
for i in range(0,4):
    baseFN = 'bestParamsEva_160_80_10_-'+str(i)
    interFN = baseFN+ '-_intercepts.txt'
    coefFN = baseFN + '-_coeffs.txt'

    np.savetxt(interFN,SLPClass.intercepts_[i])#,fmt='%.15f')
    np.savetxt(coefFN,SLPClass.coefs_[i])#,fmt='%.15f')


# print SLPClass.coefs_
# print
# print SLPClass.intercepts_

# for i in range(total_threads):
#     result.append(out_q.get())
#
#
# # Wait for all worker processes to finish
# for p in procs:
#     print 'waiting on process'
#     p.join()
#
# print result


# maximum_ = -1
# maximum_result = []
# for resArray in result:
#     print "resArray ", resArray
#     # for res in resArray:
#     # print "res",resArray
#     if (resArray[-1] +resArray[-2])> maximum_:
#         maximum_ = (resArray[-1] + resArray[-2])
#         maximum_result = resArray
#
# print maximum_
# print maximum_result