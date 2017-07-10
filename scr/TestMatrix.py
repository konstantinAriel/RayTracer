
import numpy as np
import pandas as pd
from numpy import nan
from numpy.linalg import inv
from scr.MainParam import Parametrs


class TestMatrix:
    def __init__(self,  mirrorList):
        self.rayInDict, self.rayReflectedDict = self.setRays4Plot()
        self.rInList = ['Xin', 'Kxin', 'Zin', 'Kzin']
        self.aList = ['a44', 'a444', 'a4444']
        self.rOutList = ['Xout', 'Kxout', 'Zout', 'Kzout']
        self.xMax = 50
        self.kMax = 0.02
        self.nanArray = np.array([[nan, nan, nan, nan],
                                  [nan, nan, nan, nan],
                                  [nan, nan, nan, nan],
                                  [nan, nan, nan, nan]])
        self.numberOfPoints = 3
        self.numberOfRays = (4 + 6 + 4) * self.numberOfPoints
        self.pointArray = np.array([[1], [-1], [0.5]])
        self.RaysZeroDF = self.setZeroRaysDataFrame(self.numberOfRays)

        if mirrorList == None:
            pass
        else:
            self.pathTotestMatrix = []
            self.mirrorList = mirrorList

    def setRays4Plot(self):

        #print(mirrorDataSheet)

        xRayInData = []
        yRayInData = []
        zRayInData = []

        xRayReflectedData = []
        yRayReflectedData = []
        zRayReflectedData = []

        xRayNormalData = []
        yRayNormalData = []
        zRayNormalData = []
        #Construct List of pairs of Rays



        rayInDict = dict(x=xRayInData, y=yRayInData, z=zRayInData)
        rayReflectedDict = dict(x=xRayReflectedData, y=yRayReflectedData, z=zRayReflectedData)


        return rayInDict, rayReflectedDict

    def getThirdStepMatrix(self, RayReflectedDF, countMirror, mainRinDF, rInList, rOutList, startMirror, testMatrixDF):
        for i1 in range(0, 2):
            keyNameI1 = rInList[i1]
            keynameA11ps = 'A1' + '_' + keyNameI1  # x=
            keynameA211ps = 'A2' + keyNameI1 + '_' + keyNameI1  # x^2=
            keynameA3111ps = 'A3' + keyNameI1 + keyNameI1 + '_' + keyNameI1  # x^3

            for i2 in range((i1 + 1), 3):
                keyNameI2 = rInList[i2]

                keynameA12ps = 'A1' + '_' + keyNameI2  # k=
                keynameA222ps = 'A2' + keyNameI2 + '_' + keyNameI2  # kx^2=
                keynameA3222ps = 'A3' + keyNameI2 + keyNameI2 + '_' + keyNameI2  # kx^3=
                keynameA212ps = 'A2' + keyNameI1 + '_' + keyNameI2  # k*x=
                keynameA3221ps = 'A3' + keyNameI2 + keyNameI2 + '_' + keyNameI1  # k^2*x=
                keynameA3112ps = 'A3' + keyNameI1 + keyNameI1 + '_' + keyNameI2  # x^2*k=

                for i3 in range((i2 + 1), 4):
                    keyNameI3 = rInList[i3]

                    keynameA13ps = 'A1' + '_' + keyNameI3  # z=
                    keynameA233ps = 'A2' + keyNameI3 + '_' + keyNameI3  # z^2=
                    keynameA3333ps = 'A3' + keyNameI3 + keyNameI3 + '_' + keyNameI3  # z^3=
                    keynameA213ps = 'A2' + keyNameI1 + '_' + keyNameI3  # x*z=
                    keynameA223ps = 'A2' + keyNameI2 + '_' + keyNameI3  # k*z=
                    keynameA3113ps = 'A3' + keyNameI1 + keyNameI1 + '_' + keyNameI3  # x^2*z=
                    keynameA3223ps = 'A3' + keyNameI2 + keyNameI2 + '_' + keyNameI3  # k^2*z=
                    keynameA3331ps = 'A3' + keyNameI3 + keyNameI3 + '_' + keyNameI1  # z^2*x=
                    keynameA3332ps = 'A3' + keyNameI3 + keyNameI3 + '_' + keyNameI2  # z^2*k=

                    # print('***************** list of Headers ********************************')
                    # print(keynameA11ps)
                    # print(keynameA211ps)
                    # print(keynameA3111ps)
                    # print(keynameA12ps)
                    # print(keynameA222ps)
                    # print(keynameA3222ps)
                    # print(keynameA13ps)
                    # print(keynameA233ps)
                    # print(keynameA3333ps)
                    # print(keynameA212ps)
                    # print(keynameA213ps)
                    # print(keynameA223ps)
                    # print(keynameA223ps)
                    # print(keynameA3112ps)
                    # print(keynameA3113ps)
                    # print(keynameA3221ps)
                    # print(keynameA3223ps)
                    # print(keynameA3331ps)
                    # print(keynameA3332ps)

                    rayIn1x3 = mainRinDF[(mainRinDF.Mode == (keyNameI1 + '_' + keyNameI2 + '_' + keyNameI3))]
                    index = min(rayIn1x3.index)
                    rin11 = rayIn1x3.loc[index, keyNameI1]
                    rin21 = rayIn1x3.loc[index, keyNameI2]
                    rin31 = rayIn1x3.loc[index, keyNameI3]

                    for rOutElement in rOutList:
                        rOut = RayReflectedDF.loc[index, rOutElement]

                        A11ps = (testMatrixDF.loc[rOutElement, keynameA11ps] * rin11) + \
                                (testMatrixDF.loc[rOutElement, keynameA211ps] * (rin11 ** 2)) + \
                                (testMatrixDF.loc[rOutElement, keynameA3111ps] * (rin11 ** 3))

                        A22ps = (testMatrixDF.loc[rOutElement, keynameA12ps] * rin21) + \
                                (testMatrixDF.loc[rOutElement, keynameA222ps] * (rin21 ** 2)) + \
                                (testMatrixDF.loc[rOutElement, keynameA3222ps] * (rin21 ** 3))

                        A33ps = (testMatrixDF.loc[rOutElement, keynameA13ps] * rin31) + \
                                (testMatrixDF.loc[rOutElement, keynameA233ps] * (rin31 ** 2)) + \
                                (testMatrixDF.loc[rOutElement, keynameA3333ps] * (rin31 ** 3))
                        ######################################################
                        A12ps = (testMatrixDF.loc[rOutElement, keynameA212ps] * rin11 * rin21) + \
                                (testMatrixDF.loc[rOutElement, keynameA3112ps] * ((rin11 ** 2) * rin21)) + \
                                (testMatrixDF.loc[rOutElement, keynameA3221ps] * ((rin21 ** 2) * rin11))

                        A13ps = (testMatrixDF.loc[rOutElement, keynameA213ps] * rin11 * rin31) + \
                                (testMatrixDF.loc[rOutElement, keynameA3112ps] * ((rin11 ** 2) * rin31)) + \
                                (testMatrixDF.loc[rOutElement, keynameA3221ps] * ((rin31 ** 2) * rin11))

                        A23ps = (testMatrixDF.loc[rOutElement, keynameA223ps] * rin21 * rin31) + \
                                (testMatrixDF.loc[rOutElement, keynameA3223ps] * ((rin21 ** 2) * rin31)) + \
                                (testMatrixDF.loc[rOutElement, keynameA3332ps] * ((rin31 ** 2) * rin21))
                        ########################################################
                        AtotalPS = A11ps + A22ps + A33ps + A12ps + A13ps + A23ps
                        Rin = (rin11 * rin21 * rin31)
                        a = (rOut - AtotalPS) / Rin
                        header123 = 'A3' + keyNameI1 + keyNameI2 + '_' + keyNameI3
                        header132 = 'A3' + keyNameI1 + keyNameI3 + '_' + keyNameI2
                        header213 = 'A3' + keyNameI2 + keyNameI1 + '_' + keyNameI3
                        header231 = 'A3' + keyNameI2 + keyNameI3 + '_' + keyNameI1
                        header312 = 'A3' + keyNameI3 + keyNameI1 + '_' + keyNameI2
                        header321 = 'A3' + keyNameI3 + keyNameI2 + '_' + keyNameI1
                        testMatrixDF.loc[rOutElement, header123] = a
                        testMatrixDF.loc[rOutElement, header132] = a
                        testMatrixDF.loc[rOutElement, header213] = a
                        testMatrixDF.loc[rOutElement, header231] = a
                        testMatrixDF.loc[rOutElement, header312] = a
                        testMatrixDF.loc[rOutElement, header321] = a
        testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)
        testMatrixDF.to_excel('/home/konstantin/PycharmProjects/RayTracer/result/' +
                              str(testMatrixFName) +
                              '.xls', na_rep='nan')
        self.pathTotestMatrix.append('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls')

    def getSeconStepMatrix(self, RayReflectedDF, countMirror, mainRinDF, rInList, rOutList, startMirror, testMatrixDF):
        for rin1 in range(0, 3):
            for rin2 in range(rin1 + 1, 4):
                rInelement1 = rInList[rin1]
                rInelement2 = rInList[rin2]

                if rInelement1 == rInelement2:
                    pass
                else:
                    keynameA11ps = 'A1' + '_' + rInelement1
                    keynameA12pS = 'A2' + rInelement1 + '_' + rInelement1
                    keynameA13pS = 'A3' + rInelement1 + rInelement1 + '_' + rInelement1
                    keynameA21pS = 'A1' + '_' + rInelement2
                    keynameA22pS = 'A2' + rInelement2 + '_' + rInelement2
                    keynameA23pS = 'A3' + rInelement2 + rInelement2 + '_' + rInelement2

                    keynameA2 = 'A2' + rInelement1 + '_' + rInelement2
                    keynameA2inv = 'A2' + rInelement2 + '_' + rInelement1
                    keynameA31 = 'A3' + rInelement1 + rInelement1 + '_' + rInelement2
                    keynameA31inv11 = 'A3' + rInelement1 + rInelement2 + '_' + rInelement1
                    keynameA31inv12 = 'A3' + rInelement2 + rInelement1 + '_' + rInelement1
                    keynameA32 = 'A3' + rInelement2 + rInelement2 + '_' + rInelement1
                    keynameA32inv11 = 'A3' + rInelement2 + rInelement1 + '_' + rInelement2
                    keynameA32inv12 = 'A3' + rInelement1 + rInelement2 + '_' + rInelement2

                    rayInArray = mainRinDF[(mainRinDF.Mode == (rInelement1 + '_' + rInelement2))]
                    index = min(rayInArray.index)
                    indexMax = max(rayInArray.index)
                    # print('rayInArray = ')
                    # print(rayInArray)
                    # print('indexMax', indexMax)
                    # print('indexMin', indexMin)

                    rin11 = rayInArray.loc[index, rInelement1]
                    rin12 = rayInArray.loc[index + 1, rInelement1]
                    rin13 = rayInArray.loc[indexMax, rInelement1]
                    rin21 = rayInArray.loc[index, rInelement2]
                    rin22 = rayInArray.loc[index + 1, rInelement2]
                    rin23 = rayInArray.loc[indexMax, rInelement2]
                    a11 = rin11 * rin21
                    a12 = (rin11 ** 2) * rin21
                    a13 = rin11 * (rin21 ** 2)

                    a21 = rin12 * rin22
                    a22 = (rin12 ** 2) * rin22
                    a23 = rin12 * (rin22 ** 2)

                    a31 = rin13 * rin23
                    a32 = (rin13 ** 2) * rin23
                    a33 = rin13 * (rin23 ** 2)

                    rInMatrix33 = np.array([
                        [a11, a12, a13],
                        [a21, a22, a23],
                        [a31, a32, a33]
                    ])

                    detrInMatrix33 = a11 * a22 * a33 + a31 * a12 * a23 + a21 * a32 * a13 - a31 * a22 * a13 - a11 * a32 * a23 - a21 * a12 * a33
                    # print('detrInMatrix33')
                    # print(detrInMatrix33)
                    if detrInMatrix33 == 0:
                        # print('Matrix is not Inverted')
                        rInMatrixInv33 = rInMatrix33
                    else:
                        rInMatrixInv33 = inv(rInMatrix33)

                    c11 = rInMatrixInv33[0, 0]
                    c12 = rInMatrixInv33[0, 1]
                    c13 = rInMatrixInv33[0, 2]
                    c21 = rInMatrixInv33[1, 0]
                    c22 = rInMatrixInv33[1, 1]
                    c23 = rInMatrixInv33[1, 2]
                    c31 = rInMatrixInv33[2, 0]
                    c32 = rInMatrixInv33[2, 1]
                    c33 = rInMatrixInv33[2, 2]

                    for rayOutElement in rOutList:
                        A11 = testMatrixDF.loc[rayOutElement, keynameA11ps]
                        A12 = testMatrixDF.loc[rayOutElement, keynameA12pS]
                        A13 = testMatrixDF.loc[rayOutElement, keynameA13pS]
                        A21 = testMatrixDF.loc[rayOutElement, keynameA21pS]
                        A22 = testMatrixDF.loc[rayOutElement, keynameA22pS]
                        A23 = testMatrixDF.loc[rayOutElement, keynameA23pS]

                        rOutArray = RayReflectedDF.loc[index:indexMax, rayOutElement]
                        # print('rOutArray = ')
                        # print(rOutArray)
                        rout1 = rOutArray[index]
                        rout2 = rOutArray[index+1]
                        rout3 = rOutArray[indexMax]
                        rOutColumn31 = np.array([[rout1 -
                                                  (A11 * rin11 + A12 * (rin11 ** 2) + A13 * (rin11 ** 3) +
                                                   A21 * rin21 + A22 * (rin21 ** 2) + A23 * (rin21 ** 3))],
                                                   [rout2 -
                                                  (A11 * rin12 + A12 * (rin12 ** 2) + A13 * (rin12 ** 3) +
                                                   A21 * rin22 + A22 * (rin22 ** 2) + A23 * (rin22 ** 3))],
                                                  [rout3 -
                                                  (A11 * rin13 + A12 * (rin13 ** 2) + A13 * (rin13 ** 3) +
                                                   A21 * rin23 + A22 * (rin23 ** 2) + A23 * (rin23 ** 3))]
                                                 ])

                        # aTemp = rInMatrixInv33.dot(rOutColumn31)
                        aTemp1 = c11 * rOutColumn31[0] + c12 * rOutColumn31[1] + c13 * rOutColumn31[2]
                        aTemp2 = c21 * rOutColumn31[0] + c22 * rOutColumn31[1] + c23 * rOutColumn31[2]
                        aTemp3 = c31 * rOutColumn31[0] + c32 * rOutColumn31[1] + c33 * rOutColumn31[2]

                        testMatrixDF.loc[rayOutElement, keynameA2]       = aTemp1
                        testMatrixDF.loc[rayOutElement, keynameA2inv]    = aTemp1
                        testMatrixDF.loc[rayOutElement, keynameA31]      = aTemp2
                        testMatrixDF.loc[rayOutElement, keynameA31inv11] = aTemp2
                        testMatrixDF.loc[rayOutElement, keynameA31inv12] = aTemp2
                        testMatrixDF.loc[rayOutElement, keynameA32]      = aTemp3
                        testMatrixDF.loc[rayOutElement, keynameA32inv12] = aTemp3
                        testMatrixDF.loc[rayOutElement, keynameA32inv11] = aTemp3
        testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)
        testMatrixDF.to_excel('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls',
                              na_rep='nan')
        # self.pathTotestMatrix.append('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls')

    def getFirsttStepMatrix(self, RayReflectedDF, countMirror, mainRinDF, rInList, rOutList, startMirror, testMatrixDF):
        for rInelement in rInList:
            keynameA1 = 'A1' + '_' + rInelement

            # print('*********************   Rin =  ********  ', rInelement,'   ******************')
            rayInArray = mainRinDF[(mainRinDF.Mode == rInelement)]
            index = min(rayInArray.index)
            indexMax = max(rayInArray.index)
            # print('rayInArray = ')
            # print(rayInArray)
            # print('indexMax', indexMax)
            # print('indexMin', indexMin)
            ## Calilus For a11 a22 a33 a44

            a11 = rayInArray.loc[index, rInelement]
            a12 = a11 ** 2
            a13 = a11 ** 3
            a21 = rayInArray.loc[index + 1, rInelement]
            a22 = a21 ** 2
            a23 = a21 ** 3
            a31 = rayInArray.loc[indexMax, rInelement]
            a32 = a31 ** 2
            a33 = a31 ** 3
            rInMatrix33 = np.array([
                [a11, a12, a13],
                [a21, a22, a23],
                [a31, a32, a33]
            ])
            keynameA2 = 'A2' + rInelement + '_' + rInelement
            keynameA3 = 'A3' + rInelement + rInelement + '_' + rInelement

            for rayOutElement in rOutList:
                rOutArray = RayReflectedDF.loc[index:indexMax, rayOutElement]
                rOutColumn31 = np.array([[rOutArray[index]],
                                         [rOutArray[index + 1]],
                                         [rOutArray[indexMax]]])
                # print('rInMatrix33 = ')
                # print(rInMatrix33)
                detrInMatrix33 = a11*a22*a33 + a31*a12*a23 + a21*a32*a13 - a31*a22*a13 - a11*a32*a23 - a21*a12*a33
                # print('detrInMatrix33')
                # print(detrInMatrix33)
                if detrInMatrix33 == 0:
                    # print('Matrix is not Inverted')
                    rInMatrixInv33 = rInMatrix33
                else:
                    rInMatrixInv33 = inv(rInMatrix33)
                # aTemp = rInMatrixInv33.dot(rOutColumn31)
                c11 = rInMatrixInv33[0,0]
                c12 = rInMatrixInv33[0,1]
                c13 = rInMatrixInv33[0,2]
                c21 = rInMatrixInv33[1,0]
                c22 = rInMatrixInv33[1,1]
                c23 = rInMatrixInv33[1,2]
                c31 = rInMatrixInv33[2,0]
                c32 = rInMatrixInv33[2,1]
                c33 = rInMatrixInv33[2,2]

                rout1 = rOutColumn31[0]
                rout2 = rOutColumn31[1]
                rout3 = rOutColumn31[2]

                aTemp1 =  c11*rout1 + c12*rout2 + c13*rout3
                aTemp2 =  c21*rout1 + c22*rout2 + c23*rout3
                aTemp3 =  c31*rout1 + c32*rout2 + c33*rout3

                # print('A_TEMP[0] =                       ********************************<<<<<<<<<<')
                # print(aTemp)
                # print('testMatrixDF.koc[rayOutElement, keynameA1] = ')
                # print(testMatrixDF.loc[rayOutElement, keynameA1])
                # print('testMatrixDF.koc[rayOutElement, keynameA2] = ')
                # print(testMatrixDF.loc[rayOutElement, keynameA2])
                # print('testMatrixDF.koc[rayOutElement, keynameA3] = ')
                # print(testMatrixDF.loc[rayOutElement, keynameA3])

                testMatrixDF.loc[rayOutElement, keynameA1] = aTemp1
                testMatrixDF.loc[rayOutElement, keynameA2] = aTemp2
                testMatrixDF.loc[rayOutElement, keynameA3] = aTemp3

                # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                # print('testMatrixDF.loc[rayOutElement, keynameA1] =     ')
                # print(testMatrixDF.loc[rayOutElement, keynameA1])
                # print('testMatrixDF.loc[rayOutElement, keynameA2] = ')
                # print(testMatrixDF.loc[rayOutElement, keynameA2])
                # print('testMatrixDF.loc[rayOutElement, keynameA3] = ')
                # print(testMatrixDF.loc[rayOutElement, keynameA3])
        testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)
        # writer = pd.ExcelWriter('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls')
        # print('testMatrixDF.loc[rayOutElement, keynameA1] =     ')
        # print(testMatrixDF)
        testMatrixDF.to_excel('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls',
                              na_rep='nan')
        # self.pathTotestMatrix.append('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls')

    def setZeroRaysDataFrame(self, numberOfRays):
        raysZeroDF = pd.DataFrame({'Xin': np.zeros((numberOfRays), dtype='float32'),
                               'Yin': np.zeros((numberOfRays), dtype='float32'),
                               'Zin': np.zeros((numberOfRays), dtype='float32'),
                               'Kxin':np.zeros((numberOfRays), dtype='float32'),
                               'Kyin':np.zeros((numberOfRays), dtype='float32'),
                               'Kzin':np.zeros((numberOfRays), dtype='float32'),
                               'Exin':np.zeros((numberOfRays), dtype='float32'),
                               'Eyin':np.zeros((numberOfRays), dtype='float32'),
                               'Ezin':np.zeros((numberOfRays), dtype='float32'),
                               'Ain': np.zeros((numberOfRays), dtype='float32'),
                               'Mode': np.zeros((numberOfRays))
                             })
        return raysZeroDF

    def raysTestGenerator(self):

    # KinArray2D = np.zeros((self.numberOfRays, 3))
        # XinArray2D = np.zeros((self.numberOfRays, 3))
        # EinArray2D = np.zeros((self.numberOfRays, 4))
        # rIinIndex = 0
        i0 = 0
        # Loop for X X^2 X^3
        for rIn in self.rInList:
            for point in self.pointArray:
                self.RaysZeroDF.loc[i0, rIn] = point
                self.RaysZeroDF.loc[i0, 'Mode'] = rIn
                i0+=1
        # Loop for XZ  X^2*Z  Z^2*X
        for rin1 in  range(0, 3):
            for rin2 in range(rin1+1, 4):
                if rin2 == rin1:
                    pass
                else:
                    # print(self.rInList[rin1], self.rInList[rin2])
                    for point in self.pointArray:
                        # print('point = ', point)
                        self.RaysZeroDF.loc[i0, self.rInList[rin1]] = point
                        self.RaysZeroDF.loc[i0, self.rInList[rin2]] = point
                        self.RaysZeroDF.loc[i0, 'Mode'] = self.rInList[rin1] + '_' + rInList[rin2]
                        i0+=1
        # Loop for XYZ:
        for rin1 in  range(0, 2):
            for rin2 in range(rin1+1, 3):
                for rin3 in range (rin2+1,4):
                        # print(self.rInList[rin1], self.rInList[rin2],self.rInList[rin3])
                        for point in self.pointArray:
                            # print('point = ', point)
                            self.RaysZeroDF.loc[i0, self.rInList[rin1]] = point
                            self.RaysZeroDF.loc[i0, self.rInList[rin2]] = point
                            self.RaysZeroDF.loc[i0, self.rInList[rin3]] = point
                            self.RaysZeroDF.loc[i0, 'Mode'] = self.rInList[rin1] + '_' + \
                                                         self.rInList[rin2] + '_' + \
                                                         self.rInList[rin3]
                            i0+=1
        self.RaysZeroDF.loc[:, 'Xin'] = self.RaysZeroDF.Xin * self.xMax
        self.RaysZeroDF.loc[:, 'Zin'] = self.RaysZeroDF.Zin * self.xMax
        self.RaysZeroDF.loc[:, 'Kxin'] = self.RaysZeroDF.Kxin * self.kMax
        self.RaysZeroDF.loc[:, 'Kzin'] = self.RaysZeroDF.Kzin * self.kMax
        self.RaysZeroDF.loc[:, 'Kyin'] = 1

    def getNANarray(self):
        tempNANarray21X4 = np.array(
            [[nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],

             [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],

             [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],

             [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
              nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]
             ])
        return tempNANarray21X4

    def setZeroDict(self, rOutList, startMirror, countMirror):
        testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)

        tempNANarray84X4 = self.getNANarray()

        headerName = []
        for rInTemp1 in self.rInList:
            keynameA1 = 'A1' + '_' + rInTemp1
            headerName.append(keynameA1)

            for rInTemp2 in self.rInList:
                keynameA2 = 'A2' + rInTemp1 + '_' + rInTemp2
                headerName.append(keynameA2)
                for rInTemp3 in self.rInList:
                    keynameA3 = 'A3' + rInTemp1 + rInTemp2 + '_' + rInTemp3
                    headerName.append(keynameA3)

        testMatrixDF = pd.DataFrame(tempNANarray84X4, index=rOutList, columns=headerName)

        writer = pd.ExcelWriter('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls',
                                na_rep='nan')

        testMatrixDF.to_excel(writer, na_rep='nan', sheet_name='sheet1')
        writer.save()
        writer.close()
        # print('headerName')
        # print(headerName)
        # print('testMatrixDF')
        # print(testMatrixDF)
        # print('*************  After setZeroFunction')

        return testMatrixDF, writer