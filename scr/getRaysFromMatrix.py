import numpy as np
from numpy import nan
from scr.MainParam import Parametrs
from numpy import dot

class RaysFromMatrix:
    def __init__(self, testMatrixDF, rOutIndexList):
        self.testMatrixDF = testMatrixDF
        self.nanArray1 = np.array([[nan, nan, nan, nan],
                                   [nan, nan, nan, nan],
                                   [nan, nan, nan, nan],
                                   [nan, nan, nan, nan]])
        self.rInList = ['Xin', 'Kxin', 'Zin', 'Kzin']
        self.pathToRin = '/home/konstantin/PycharmProjects/RayTracer/result/toCompare/Ray_0_1.xls'
        self.RinObject = Parametrs(self.pathToRin, 'Sheet1')
        self.RinDF = self.RinObject.dataSheet
        # print('self.RinDF = ')
        # print(self.RinDF)
        self.rOutIndexList = rOutIndexList

    def getFirsOderRay(self):
        nanArray1 = np.array([[nan, nan, nan, nan],
                              [nan, nan, nan, nan],
                              [nan, nan, nan, nan],
                              [nan, nan, nan, nan]])
        pathToRin = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/Ray_0_1.xls'

        a11 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A1_Xin']
        a12 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A1_Kxin']
        a13 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A1_Zin']
        a14 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A1_Kzin']

        a21 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A1_Xin']
        a22 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A1_Kxin']
        a23 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A1_Zin']
        a24 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A1_Kzin']

        a31 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A1_Xin']
        a32 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A1_Kxin']
        a33 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A1_Zin']
        a34 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A1_Kzin']

        a41 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A1_Xin']
        a42 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A1_Kxin']
        a43 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A1_Zin']
        a44 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A1_Kzin']

        testMatrixArray1 = np.array([[a11, a12, a13, a14],
                              [a21, a22, a23, a24],
                              [a31, a32, a33, a34],
                              [a41, a42, a43, a44]
                              ])

        rInArray = np.array([[self.RinDF.Xin, self.RinDF.Kxin, self.RinDF.Zin, self.RinDF.Kzin]])
        # print('RinArray 1 = ')
        # print(rInArray)
        rOut1 = testMatrixArray1.dot(rInArray.T)
        print('Rout1 = ')
        print(rOut1)
        return rOut1

    def getSecondOderRay(self):
        testMatrixArray2 = np.array([[nan, nan, nan, nan],
                              [nan, nan, nan, nan],
                              [nan, nan, nan, nan],
                              [nan, nan, nan, nan]])
        rOut2 = np.zeros((4,1))
        r1 = self.RinDF.Xin
        r2 = self.RinDF.Kxin
        r3 = self.RinDF.Zin
        r4 =self.RinDF.Kzin
        RinArray = np.array([r1, r2, r3, r4])
        # print('RinArray 2 = ')
        # print(RinArray)
        # print('RinArray 2 T = ')
        # print(RinArray.T)
        for rInElement in self.rInList:

            a11 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A2' + rInElement + '_Xin']
            a12 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A2' + rInElement + '_Kxin']
            a13 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A2' + rInElement + '_Zin']
            a14 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A2' + rInElement + '_Kzin']

            a21 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A2' + rInElement + '_Xin']
            a22 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A2' + rInElement + '_Kxin']
            a23 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A2' + rInElement + '_Zin']
            a24 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A2' + rInElement + '_Kzin']

            a31 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A2' + rInElement + '_Xin']
            a32 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A2' + rInElement + '_Kxin']
            a33 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A2' + rInElement + '_Zin']
            a34 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A2' + rInElement + '_Kzin']

            a41 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A2' + rInElement + '_Xin']
            a42 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A2' + rInElement + '_Kxin']
            a43 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A2' + rInElement + '_Zin']
            a44 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A2' + rInElement + '_Kzin']

            testMatrixArray2 = np.array([[a11, a12, a13, a14],
                                  [a21, a22, a23, a24],
                                  [a31, a32, a33, a34],
                                  [a41, a42, a43, a44]
                                  ])
            # print('testMatrixArray2  = ')
            # print(testMatrixArray2)
            # print('rOut2 = ')
            # print(rOut2)
            RinDFelement = self.RinDF.loc[0, rInElement]

            # print('RinDFelement[rInElement]  = ')
            # print(RinDFelement)
            rInPowerof2 = (RinArray)*RinDFelement
            # print('rInPowerof2 = ')
            # print(rInPowerof2)
            rOut2 += testMatrixArray2.dot(rInPowerof2)
            # print('Rout2 = ')
            # print(rOut2)
        print('Rout2 = ')
        print(rOut2)
        return rOut2



