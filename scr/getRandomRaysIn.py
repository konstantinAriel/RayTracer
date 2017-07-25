import plotly as py
import numpy as np
from numpy import nan

import pandas as pd
import random
import plotly.tools as tls
import plotly.graph_objs  as go
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

class RandomRin:
    def __init__(self):
        self.F1 = 200
        self.F2 = 450
        self.rTline = 125
        self.xMax =  self.F1/self.F2*(self.rTline-10)
        self.Kmax = self.xMax/self.F1

       
    def getRandomVectorX(self):
        i = True
        i1 = 0
        # xInArray = np.zeros((3400,2))
        RInArray = np.zeros((3400,4))
        xin = np.zeros((3400, 1))
        zin = np.zeros((3400, 1))
        k1  = np.zeros((3400, 1))
        k2  = np.zeros((3400, 1))
        # print('xInArray = ')
        # print(xInArray)
        while i1 < 3400:
            randomx1, randomx2 =  self.getRandomX(self.xMax)
            randomK1, randomK2 =  self.getRandomX(self.Kmax)
            inElipsXZ = ((randomx1/self.xMax)**2 +
                         (randomx2/self.xMax)**2 +
                         (randomK1/self.Kmax) ** 2 +
                         (randomK2/self.Kmax) ** 2)-1
            # inElipsXKx = ((randomx1/self.xMax)**2 + (randomK2/self.Kmax)**2)-1
            # inElipszKz = ((randomx1/self.xMax)**2 + (randomK2/self.Kmax)**2)-1
            # print('inElips = ')
            # print(inElips)
            if inElipsXZ >= 0:
                pass
            else:
                xinNew = [randomx1, randomK1, randomx2, randomK2]
                RInArray[i1] = xinNew
                xin[i1] = randomx1
                zin[i1] = randomx2
                k1[i1] = randomK1
                k2[i1] = randomK2
                # print('i1 = ')
                # print(i1)
                # print('xInArray = ')
                # print(xInArray)
                i1+=1
            # print('len(xInArray) = ')
            # print(len(RInArray))
        return xin, zin, k1, k2

    def getRandomVectorK(self):
        i1 = 0
        KInArray = np.zeros((3400,2))
        # print('xInArray = ')
        # print(KInArray)
        while i1 < 3400:
            randomK1, randomK2 = self.getRandomX(self.Kmax)
            inElips = ((randomK1 / self.xMax) ** 2 + (randomK2 / self.xMax) ** 2) - 1
            # print('inElips = ')
            # print(inElips)
            if inElips > 0:
                pass
            else:
                kinNew = [randomK1, randomK2]
                KInArray[i1] = kinNew
                # print('xInArray = ')
                # print(KInArray)
                i1+=1
        return KInArray

    def getRandomX(self, xMax):
          randomx1 =  random.uniform(-xMax, xMax)
          randomx2 =  random.uniform(-xMax, xMax)
          return  randomx1, randomx2

    def setRaysDataFrame(self, x1, x2, k1,k2):
        # print('EinArray',EinArray)
        zerosV =  np.zeros((3400, 1))
        onesV = np.ones((3400,1))
        raysDF = pd.DataFrame({'Xin':  x1[:, 0],
                               'Yin':  zerosV[:,0],
                               'Zin':  x2[:, 0],
                               'Kxin': k1[:, 0],
                               'Kyin': onesV[:, 0],
                               'Kzin': k2[:,0],
                               'Exin': zerosV[:, 0],
                               'Eyin': zerosV[:, 0],
                               'Ezin': zerosV[:, 0],
                               'Ain':  zerosV[:, 0],
                               })
        return raysDF

    def saveRays2Execel(self, fileName, raysDF):
        raysDF.to_excel(fileName)


rInObj = RandomRin()
xm = rInObj.xMax
km =rInObj.Kmax

# xInVector = rInObj.getRandomVectorX()
x1, x2, k1, k2 = rInObj.getRandomVectorX()
# KInVector = rInObj.getRandomVectorK()
# print('xInVector = ')
# pr11int(xInVector)
# print('KInVector = ')
# print(x1)
# np.zeros((3400, 1))
# np.ones((3400, 1))
rInDF = rInObj.setRaysDataFrame(x1, x2, k1,k2)
fileName =  '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/ray4test3Point_sysParam_1.xls'
rInObj.saveRays2Execel(fileName, rInDF)

# data = [trace]
# py.offline.plot(data, filename='111.html')
