
import sympy as sp
from numpy import sin, cos,pi
from sympy import init_printing, pprint
import numpy as np
import pandas as pd
import scipy as sy

class Rays:
    def __init__(self):
       pass

    def rInNormalise(self,RinParamTable):
        RaysHeads = RinParamTable.columns
        RayCount = 0
        numberOfRays = len(RinParamTable.KxIn)
        KinArray = np.zeros((0, 3))
        KinNormalArray = np.zeros((numberOfRays, 3))
        XinArray = np.zeros((numberOfRays, 3))
        EinArray = np.zeros((numberOfRays, 4))

        for RinIndex in RinParamTable.index:
            #print(RinIndex)
            KinArray = np.array([RinParamTable.KxIn[RinIndex],
                                 RinParamTable.KyIn[RinIndex],
                                 RinParamTable.KzIn[RinIndex]
                                 ])

            XinArray[RinIndex, :] = np.array([RinParamTable.Xin[RinIndex],
                                              RinParamTable.Yin[RinIndex],
                                              RinParamTable.Zin[RinIndex]
                                              ])
            EinArray[RinIndex, :] = np.array([RinParamTable.ExIn[RinIndex],
                                              RinParamTable.EyIn[RinIndex],
                                              RinParamTable.EzIn[RinIndex],
                                              RinParamTable.Ain[RinIndex]
                                              ])
            KinNormal = KinArray/(np.sqrt(np.dot(KinArray, KinArray.T)))
            KinNormalArray[RinIndex, :] = KinNormal
            print('KinNormalArray : ',KinNormalArray)
            print('KinArray',KinArray)
            print('KinNormal',KinNormal)
            RayCount += 1
            print('=========================')
            print('XinArray=', XinArray)
        raysDF = pd.DataFrame({'Xin': XinArray[:, 0],
                               'Yin': XinArray[:, 1],
                               'Zin': XinArray[:, 2],
                               'Kxin': KinNormalArray[:, 0],
                               'Kyin': KinNormalArray[:, 1],
                               'Kzin': KinNormalArray[:, 2],
                               'Exin': EinArray[:, 0],
                               'Eyin': EinArray[:, 1],
                               'Ezin': EinArray[:, 2],
                               'Ain': EinArray[:, 3]
                              })
        print('*************')
        print('KinDF = ')
        print('raysDF', raysDF)
        return  raysDF

    def saveExecelRin(self,FileName, raysDF,RaysSheetName):
        raysDF.to_excel(FileName, sheet_name=RaysSheetName)

    def calcReflectedRays(self, Mirror,  RaysInDF, RaysName):
        print(RaysName)
        x1, x2, x3, dx1, dx2, dx3, a11, a22, a3, x01Ray, x02Ray, x03Ray, k1, k2, k3, t = sp.symbols('x1 x2 x3 '
                                                                                                    'dx1 dx2 dx3 '
                                                                                                    'a11 a22 a3 '
                                                                                                    'x01Ray x02Ray x03Ray '
                                                                                                    'k1 k2 k3'
                                                                                                    ' t')
        x1R, x2R, x3R, dx1R, dx2R, dx3R = sp.symbols('x1R x2R x3R dx1R dx2R dx3R')

        xDegree = Mirror.direction[0]
        yDegree = Mirror.direction[1]
        zDegree = Mirror.direction[2]

        a11 = 1 / (4 * Mirror.Focus[0])
        a22 = 1 / (4 * Mirror.Focus[1])
        a3 = 1
        print(a11, a22, a3)
        v1 = Mirror.Vertex[0]
        v2 = Mirror.Vertex[1]
        v3 = Mirror.Vertex[2]
        print(v1, v2, v3)

        x01Ray = RaysInDF.Xin
        x02Ray = RaysInDF.Yin
        x03Ray = RaysInDF.Zin
        # k1 = RaysInDF.Kxin
        # k2 = RaysInDF.Kyin
        # k3 = RaysInDF.Kzin

        print(x01Ray, x02Ray, x03Ray)
        print(k1,k2,k3)

        for RinIndex in RaysInDF.index:  # Loop for all Rays

            k1 = RaysInDF.Kxin[RinIndex]
            k2 = RaysInDF.Kyin[RinIndex]
            k3 = RaysInDF.Kzin[RinIndex]
            # print(RinIndex)
            # print('k1 = ', k1)
            # print('k2 = ', k2)
            # print('k3 = ', k3)

    def degree2Radian(self, alphaDegree):
        return (alphaDegree*pi)/180

    def cs(self, alphaDegree):
        alphaRadian = self.degree2Radian(alphaDegree)
        if np.abs(cos(alphaRadian)) < 1e-4:
            csAlpha = 0
        else:
            csAlpha =  cos(alphaRadian)
        return csAlpha

    def sn(self, alphaDegree):
        alphaRadian = self.degree2Radian(self, alphaDegree)
        if np.abs(sin(alphaRadian)) < 1e-4:
                snAlpha = 0
        else:
                snAlpha = sin(alphaRadian)
        return snAlpha

    def getRotateMatrix(self, xDegree,yDegree, zDegree):
        csX = self.cs(xDegree)
        snX = self.sn(xDegree)
        csY = self.cs(yDegree)
        print(csY)
        snY = self.sn(yDegree)
        print(snY)
        csZ = self.cs(zDegree)
        snZ = self.sn(zDegree)
        Rx = np.array([
            [1, 0, 0],
            [0, csX, -snX],
            [0, snX, csX]
        ])
        Ry = np.array([
            [csY, 0, snY],
            [0, 1, 0],
            [-snY, 0, csY]
        ])
        Rz = np.array([
            [csZ, -snZ, 0],
            [snZ, csZ, 0],
            [0, 0, 1]
        ])
        print('******************************')
        Mr = (Rx.dot(Ry)).dot(Rz)
        print(Rx)
        print(Ry)
        print(Rz)
        print('===================')
        print('Mr = ')
        print(Mr)
        print('=======================')
        return  Mr