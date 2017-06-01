import numpy as np
from numpy import nan
from scr.MainParam import Parametrs
from numpy import dot
from scr.mainTest import pathName


class RaysFromMatrix:
    def __init__(self, pathToTestMatrixList):
        self.fExtend = '.xls'
        self.paramObject = Parametrs(path=None, sheetName="SysParam")
        self.mirrorDictMain = self.paramObject(self.sys.dataSheet)
        self.pathToTestMatrixList = pathToTestMatrixList
        self.nanArray1 = np.array([[nan, nan, nan, nan],
                                   [nan, nan, nan, nan],
                                   [nan, nan, nan, nan],
                                   [nan, nan, nan, nan]])
        self.rInList = ['Xin', 'Kxin', 'Zin', 'Kzin']

    def mirrorLoop(self):
        for mirrorDictSub in self.mirrorDictMain.keys():
            # print(sys.dataSheet.Rin[0])
            countMirror = int(self.paramObject.dataSheet.Rin[0])
            for mirrorList in self.mirrorDictMain.get(mirrorDictSub):
                print(
                    '====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',
                    mirrorList)
                print("Count = ", countMirror)
                # print("Current Mirror = ", mirrorList)

                Mirror = self.paramObject.getParam(self.paramObject,
                                                   mirrorList)  ## mirror List - The name of Sheets in Exel file
                # print('Mirror = ')
                # print(Mirror)

                ################################################################
                raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                             'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                             'normalRay_' + str(countMirror) + '_' + str(countMirror)]
                RaysObject = Parametrs(self.pathToTestMatrixList + raysFName[0] + fExtend, 'Sheet1')
                print(RaysObject.dataSheet)
                path = [self.pathToTestMatrixList, raysFName, self.fExtend]
                print('path = ', path)

                countMirror += 1
                # print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++   END      Mirror Loop         ',  mirrorList)

    def getFirsOderRay(self, ):
        nanArray1 = np.array([[nan, nan, nan, nan],
                              [nan, nan, nan, nan],
                              [nan, nan, nan, nan],
                              [nan, nan, nan, nan]])
        for testMatrix in self.pathToTestMatrixList:
            mainPath = '/home/konstantin/PycharmProjects/RayTracer/result'
            pathToTestMatrix = testMatrix
            pathToRin = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/Ray_0_1.xls'
            RinObject = Parametrs(pathToRin, 'Sheet1')
            RinDF = RinObject.dataSheet
            testMatrixObject = Parametrs(pathToTestMatrix, 'Sheet1')
            testMatrixDF = testMatrixObject.dataSheet
            a11 = testMatrixDF.loc['Xin', 'A1_Xin']
            a12 = testMatrixDF.loc['Xin', 'A1_Kxin']
            a13 = testMatrixDF.loc['Xin', 'A1_Zin']
            a14 = testMatrixDF.loc['Xin', 'A1_Kzin']

            a21 = testMatrixDF.loc['Kxin', 'A1_xin']
            a22 = testMatrixDF.loc['Kxin', 'A1_Kxin']
            a23 = testMatrixDF.loc['Kxin', 'A1_Zin']
            a24 = testMatrixDF.loc['Kxin', 'A1_Kzin']

            a31 = testMatrixDF.loc['Zin', 'A1_Xin']
            a32 = testMatrixDF.loc['Zin', 'A1_Kxin']
            a33 = testMatrixDF.loc['Zin', 'A1_Zin']
            a34 = testMatrixDF.loc['Zin', 'A1_Kzin']

            a41 = testMatrixDF.loc['Kzin', 'A1_xin']
            a42 = testMatrixDF.loc['Kzin', 'A1_Kxin']
            a43 = testMatrixDF.loc['zxin', 'A1_Zin']
            a44 = testMatrixDF.loc['Kzin', 'A1_Kzin']

            print(testMatrixDF)
            nanArray1 = np.array([[a11, a12, a13, a14],
                                  [a21, a22, a23, a24],
                                  [a31, a32, a33, a34],
                                  [a41, a42, a43, a44]
                                  ])

            RinArray = np.array([[RinDF.Xin, RinDF.Kxin, RinDF.Zin, RinDF.Kzin]])
            Rout1 = nanArray1.dot(RinArray.T)
            return Rout1

    def getSecondOderRay(self):
        nanArray1 = np.array([[nan, nan, nan, nan],
                              [nan, nan, nan, nan],
                              [nan, nan, nan, nan],
                              [nan, nan, nan, nan]])
        for testMatrix in self.pathToTestMatrixList:
            mainPath = '/home/konstantin/PycharmProjects/RayTracer/result'
            pathToTestMatrix = testMatrix
            pathToRin = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/Ray_0_1.xls'
            RinObject = Parametrs(pathToRin, 'Sheet1')
            RinDF = RinObject.dataSheet
            testMatrixObject = Parametrs(pathToTestMatrix, 'Sheet1')
            testMatrixDF = testMatrixObject.dataSheet
            rOut2 = np.zeros(0, 3)
            for rInelement in self.rInList:
                a11 = testMatrixDF.loc['Xin', 'A2' + rInelement + '_Xin']
                a12 = testMatrixDF.loc['Xin', 'A2' + rInelement + '_Kxin']
                a13 = testMatrixDF.loc['Xin', 'A2' + rInelement + '_Zin']
                a14 = testMatrixDF.loc['Xin', 'A2' + rInelement + '_Kzin']

                a21 = testMatrixDF.loc['Kxin', 'A2' + rInelement + '_xin']
                a22 = testMatrixDF.loc['Kxin', 'A2' + rInelement + '_Kxin']
                a23 = testMatrixDF.loc['Kxin', 'A2' + rInelement + '_Zin']
                a24 = testMatrixDF.loc['Kxin', 'A2' + rInelement + '_Kzin']

                a31 = testMatrixDF.loc['Zin', 'A2' + rInelement + '_Xin']
                a32 = testMatrixDF.loc['Zin', 'A2' + rInelement + '_Kxin']
                a33 = testMatrixDF.loc['Zin', 'A2' + rInelement + '_Zin']
                a34 = testMatrixDF.loc['Zin', 'A2' + rInelement + '_Kzin']

                a41 = testMatrixDF.loc['Kzin', 'A2' + rInelement + '_xin']
                a42 = testMatrixDF.loc['Kzin', 'A2' + rInelement + '_Kxin']
                a43 = testMatrixDF.loc['zxin', 'A2' + rInelement + '_Zin']
                a44 = testMatrixDF.loc['Kzin', 'A2' + rInelement + '_Kzin']

                print(testMatrixDF)
                nanArray1 = np.array([[a11, a12, a13, a14],
                                      [a21, a22, a23, a24],
                                      [a31, a32, a33, a34],
                                      [a41, a42, a43, a44]
                                      ])
                RinArray = np.array([[RinDF.loc['Xin'], RinDF.loc['Kxin'], RinDF.loc['Zin'], RinDF.loc['Kzin']]])

                rOut2 += nanArray1.dot((RinArray.T) * RinDF.loc[rInelement])
        return rOut2



