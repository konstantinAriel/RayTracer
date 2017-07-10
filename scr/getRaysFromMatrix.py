import numpy as np
from numpy import nan
from scr.MainParam import Parametrs
from numpy import dot

class RaysFromMatrix:
    def __init__(self,pathToRin, testMatrixDF):
        self.testMatrixDF = testMatrixDF
        self.nanArray1 = np.array([[nan, nan, nan, nan],
                                   [nan, nan, nan, nan],
                                   [nan, nan, nan, nan],
                                   [nan, nan, nan, nan]])
        self.rInList = ['Xin', 'Kxin', 'Zin', 'Kzin']
        self.pathToRin = pathToRin
        # self.pathToRin = '/home/konstantin/PycharmProjects/RayTracer/result/toCompare/Ray_0_1.xls'
        self.RinObject = Parametrs(self.pathToRin, 'Sheet1')
        self.RinDF = self.RinObject.dataSheet
        # print('self.RinDF = ')
        # print(self.RinDF)
        #self.rOutIndexList = rOutIndexList
        self.rOutIndexList = testMatrixDF.index

        self.testMatrixArray1 = self.getTestMatrixArray1()

    def getFirsOderRay(self, indexRay):

        testMatrixArray1 = self.getTestMatrixArray1()
        rInArray = np.array([[self.RinDF.Xin[indexRay], self.RinDF.Kxin[indexRay], self.RinDF.Zin[indexRay], self.RinDF.Kzin[indexRay]]])
        # print('RinArray 1 = ')
        # print(rInArray)
        # rOutTemp1 = a11 * self.RinDF.Xin + a12 * self.RinDF.Kxin + a13 * self.RinDF.Zin + a14 * self.RinDF.Kzin
        # rOutTemp2 = a21 * self.RinDF.Xin + a22 * self.RinDF.Kxin + a23 * self.RinDF.Zin + a24 * self.RinDF.Kzin
        # rOutTemp3 = a31 * self.RinDF.Xin + a32 * self.RinDF.Kxin + a33 * self.RinDF.Zin + a34 * self.RinDF.Kzin
        # rOutTemp4 = a41 * self.RinDF.Xin + a42 * self.RinDF.Kxin + a43 * self.RinDF.Zin + a44 * self.RinDF.Kzin
        rOut1 = testMatrixArray1.dot(rInArray.T)
        # print('Rout1 = ')
        # print(rOut1)
        return rOut1

    def getSecondOderRay(self, indexRay, rIn1):
        rOut2 = np.zeros((4,1))
        r1 = self.RinDF.Xin[indexRay]
        r2 = self.RinDF.Kxin[indexRay]
        r3 = self.RinDF.Zin[indexRay]
        r4 = self.RinDF.Kzin[indexRay]
        RinArray = np.array([[r1], [r2], [r3], [r4]])

        # for rInElement in self.rInList:
        #     testMatrixArray2 = self.getTestMatrixArray2(rInElement)
        #     # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%  getThirdOderRay %%%%%%%%%%%%%%%%%%%%%%%%%%  ' + str(rInElement))
        #     RinDFelement = self.RinDF.loc[0, rInElement]
        #     rInPowerof2 = (RinArray)*RinDFelement
        #     rOut2 += testMatrixArray2.dot(rInPowerof2)



        testMatrixArray2 = self.getTestMatrixArray2(rIn1)
        # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%  getThirdOderRay %%%%%%%%%%%%%%%%%%%%%%%%%%  ' + str(rInElement))
        RinDFelement = self.RinDF.loc[indexRay, rIn1]
        rInPowerof2 = (RinArray)*RinDFelement
        rOut2 = testMatrixArray2.dot(rInPowerof2)
        if rIn1 == 'Kxin':
            print('==========================')
            print('rInElement = ')
            print(rIn1)
            print('testMatrixArray2 = ')
            print(testMatrixArray2)
            print('RinDFelement = ')
            print(RinDFelement)
            print('RinArray = ')
            print(RinArray)
            print('rInPowerof2 = ')
            print(rInPowerof2)
            print('rOut2 = ')
            print(rOut2)
        return rOut2

    def getThirdOderRay(self, indexRay, rIn1, rIn2):
        # print('=============================  getThirdOderRay ========================  IndexRays'  + str(indexRay))
        rOut3 = np.zeros((4, 1))
        r1 = self.RinDF.Xin[indexRay]
        r2 = self.RinDF.Kxin[indexRay]
        r3 = self.RinDF.Zin[indexRay]
        r4 = self.RinDF.Kzin[indexRay]
        RinArray3 = np.array([[r1], [r2], [r3], [r4]])

        # for i in range(4):
        #     rInElement1 = self.rInList[i]
        #     for j in range(i,4):
        #         rInElement2 = self.rInList[j]
        #         testMatrixArray3 = self.getTestMatrixArray3(rInElement1, rInElement2)
        #         # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%  getThirdOderRay %%%%%%%%%%%%%%%%%%%%%%%%%%  ' + str(rInElement2) + '_' + str(rInElement1))
        #
        #         RinDFelement1 = self.RinDF.loc[0, rInElement1]
        #         RinDFelement2 = self.RinDF.loc[0, rInElement1]
        #         rInPowerof3 = (RinArray3)*RinDFelement1*RinDFelement2
        #
        #         rOut3 += testMatrixArray3.dot(rInPowerof3)
        #
        #         # print('************************   END IN LOOP  ***************************')
        # # print('Rout3 = ')
        # # print(rOut3)

        testMatrixArray3 = self.getTestMatrixArray3(rIn1, rIn2)
        # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%  getThirdOderRay %%%%%%%%%%%%%%%%%%%%%%%%%%  ' + str(rInElement2) + '_' + str(rInElement1))

        RinDFelement1 = self.RinDF.loc[indexRay, rIn1]
        RinDFelement2 = self.RinDF.loc[indexRay, rIn2]
        rInPowerof3 = (RinArray3)*RinDFelement1*RinDFelement2

        rOut3 = testMatrixArray3.dot(rInPowerof3)

        # print('************************   END IN LOOP  ***************************')
        # print('Rout3 = ')
        # print(rOut3)
        return rOut3

    def getTestMatrixArray1(self):
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
        return testMatrixArray1

    def getTestMatrixArray2(self, rInElement):
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
        # rOutTemp1 = a11 * self.RinDF.Xin + a12 * self.RinDF.Kxin + a13 * self.RinDF.Zin + a14 * self.RinDF.Kzin
        # rOutTemp2 = a21 * self.RinDF.Xin + a22 * self.RinDF.Kxin + a23 * self.RinDF.Zin + a24 * self.RinDF.Kzin
        # rOutTemp3 = a31 * self.RinDF.Xin + a32 * self.RinDF.Kxin + a33 * self.RinDF.Zin + a34 * self.RinDF.Kzin
        # rOutTemp4 = a41 * self.RinDF.Xin + a42 * self.RinDF.Kxin + a43 * self.RinDF.Zin + a44 * self.RinDF.Kzin
        testMatrixArray2 = np.array([[a11, a12, a13, a14],
                                     [a21, a22, a23, a24],
                                     [a31, a32, a33, a34],
                                     [a41, a42, a43, a44]
                                     ])
        return testMatrixArray2

    def getTestMatrixArray3(self, rInElement1, rInElement2):
        a11 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A3' + 'Xin' + rInElement2 + '_' + rInElement1]
        a12 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A3' + 'Kxin' + rInElement2 + '_' + rInElement1]
        a13 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A3' + 'Zin' + rInElement2 + '_' + rInElement1]
        a14 = self.testMatrixDF.loc[self.rOutIndexList[0], 'A3' + 'Kzin' + rInElement2 + '_' + rInElement1]
        a21 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A3' + 'Xin' + rInElement2 + '_' + rInElement1]
        a22 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A3' + 'Kxin' + rInElement2 + '_' + rInElement1]
        a23 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A3' + 'Zin' + rInElement2 + '_' + rInElement1]
        a24 = self.testMatrixDF.loc[self.rOutIndexList[1], 'A3' + 'Kzin' + rInElement2 + '_' + rInElement1]
        a31 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A3' + 'Xin' + rInElement2 + '_' + rInElement1]
        a32 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A3' + 'Kxin' + rInElement2 + '_' + rInElement1]
        a33 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A3' + 'Zin' + rInElement2 + '_' + rInElement1]
        a34 = self.testMatrixDF.loc[self.rOutIndexList[2], 'A3' + 'Kzin' + rInElement2 + '_' + rInElement1]
        a41 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A3' + 'Xin' + rInElement2 + '_' + rInElement1]
        a42 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A3' + 'Kxin' + rInElement2 + '_' + rInElement1]
        a43 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A3' + 'Zin' + rInElement2 + '_' + rInElement1]
        a44 = self.testMatrixDF.loc[self.rOutIndexList[3], 'A3' + 'Kzin' + rInElement2 + '_' + rInElement1]
        testMatrixArray3 = np.array([[a11, a12, a13, a14],
                                     [a21, a22, a23, a24],
                                     [a31, a32, a33, a34],
                                     [a41, a42, a43, a44]
                                     ])
        return testMatrixArray3


