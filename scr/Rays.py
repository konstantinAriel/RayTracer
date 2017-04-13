import sympy as sp
from numpy import sin, cos, pi
from sympy import init_printing, pprint
import numpy as np
import pandas as pd
import scipy as sy


class Rays:
    def __init__(self):
        pass

    def rInNormalise(self, RinParamTable):
        RaysHeads = RinParamTable.columns
        RayCount = 0
        numberOfRays = len(RinParamTable.KxIn)
        KinArray = np.zeros((0, 3))
        KinNormalArray = np.zeros((numberOfRays, 3))
        XinArray = np.zeros((numberOfRays, 3))
        EinArray = np.zeros((numberOfRays, 4))

        for RinIndex in RinParamTable.index:
            # print(RinIndex)
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
            KinNormal = KinArray / (np.sqrt(np.dot(KinArray, KinArray.T)))
            KinNormalArray[RinIndex, :] = KinNormal
            RayCount += 1
            # print('KinNormalArray : ',KinNormalArray)
            # print('KinArray',KinArray)
            # print('KinNormal',KinNormal)
            # print('=========================')
            # print('XinArray=', XinArray)
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
        # print('*************')
        # print('KinDF = ')
        # print('raysDF', raysDF)
        return raysDF

    def saveRays2Execel(self, FileName, raysDF, RaysSheetName):
        raysDF.to_excel(FileName, sheet_name=RaysSheetName)

    def calcReflectedRays(self, Mirror, raysDF, RaysName):
        print(RaysName)
        x1, x2, x3, a11, a22, a3, x01Ray, x02Ray, x03Ray, k1, k2, k3, v1, v2, v3, t = sp.symbols('x1 x2 x3 a11 a22 a3 x01Ray x02Ray x03Ray k1 k2 k3 v1 v2 v3 t')

        x1R, x2R, x3R, dx1R, dx2R, dx3R = sp.symbols('x1R x2R x3R dx1R dx2R dx3R')

        xDegree = Mirror.direction[0]
        yDegree = Mirror.direction[1]
        zDegree = Mirror.direction[2]

        Mr = self.getRotateMatrix(xDegree, yDegree, zDegree)

        for RinIndex in raysDF.index:  # Loop for all Rays

            print(RinIndex)

            x01Ray = raysDF.Xin[RinIndex]
            x02Ray = raysDF.Yin[RinIndex]
            x03Ray = raysDF.Zin[RinIndex]
            k1 = raysDF.Kxin[RinIndex]
            k2 = raysDF.Kyin[RinIndex]
            k3 = raysDF.Kzin[RinIndex]
            a11 = 1/(4 * Mirror.Focus[0])
            a22 = 1/(4 * Mirror.Focus[2])
            a3 = 1
            v1 = Mirror.Vertex[0]
            v2 = Mirror.Vertex[1]
            v3 = Mirror.Vertex[2]

            # print(a11, a22, a3)
            # print(v1, v2, v3)
            # print('x01 = ', x01Ray)
            # print('x02 = ', x02Ray)
            # print('x03 = ', x03Ray)
            # print('k1 = ', k1)
            # print('k2 = ', k2)
            # print('k3 = ', k3)

            x1Ray = x01Ray + k1 * t
            x2Ray = x02Ray + k2 * t
            x3Ray = x03Ray + k3 * t

            x1R = (x1 - v1) * Mr[0, 0] + (x2 - v2) * Mr[0, 1] + (x3 - v3) * Mr[0, 2]
            x2R = (x1 - v1) * Mr[1, 0] + (x2 - v2) * Mr[1, 1] + (x3 - v3) * Mr[1, 2]
            x3R = (x1 - v1) * Mr[2, 0] + (x2 - v2) * Mr[2, 1] + (x3 - v3) * Mr[2, 2]

            # print('x1R = ', x1R)
            # print('x2R = ', x2R)
            # print('x3R = ', x3R)

            Expr_A11 = x1R ** 2
            Expr_A22 = x2R ** 2
            Expr_A3 = x3R

            # x1 = x1Ray
            # x2 = x2Ray
            # x3 = x3Ray

            mainExpr = a11 * Expr_A11 + a22 * Expr_A22 - a3 * Expr_A3

            # mainExprSubsx1 = mainExpr.subs(x1, x1Ray)
            # mainExprSubsx2 = mainExprSubsx1.subs(x2, x2Ray)
            # mainExprSubsx3 = mainExprSubsx2.subs(x3, x3Ray)
            mainExprSubs = mainExpr.subs(x1, x1Ray)
            mainExprSubs = mainExprSubs.subs(x2, x2Ray)
            mainExprSubs = mainExprSubs.subs(x3, x3Ray)
            mainExprExpanded = sp.expand(mainExprSubs)
            mainExprCollcted = sp.collect(mainExprExpanded, t)
            tSolver = sp.solveset(mainExprCollcted, t)

            # print('mainExpr = ')
            # pprint(mainExpr)
            # print('mainExprSubs = ')
            # pprint(mainExprSubs)
            # print('mainExprExpanded = ')
            # pprint(mainExprExpanded)
            # print('Expr Collected = ')
            # pprint(mainExprCollcted)
            # print('t = ')
            # pprint(tSolver)


            # if len(tSolver) == 2:

            tList= []
            for tindex in tSolver:
                    if tindex > 0:
                        tList.append(tindex)
            tRoot = min(tList)
            print('tRoot = ', (tRoot))

            x1Ray = x01Ray + k1*tRoot
            x2Ray = x02Ray + k2*tRoot
            x3Ray = x03Ray + k3*tRoot
            print('x1Ray = ', x1Ray)
            print('x2Ray = ', x2Ray)
            print('x3Ray = ', x3Ray)

    def degree2Radian(self, alphaDegree):
        return (alphaDegree * pi) / 180

    def cs(self, alphaDegree):
        alphaRadian = self.degree2Radian(alphaDegree)
        if np.abs(cos(alphaRadian)) < 1e-4:
            csAlpha = 0
        else:
            csAlpha = cos(alphaRadian)
        return csAlpha

    def sn(self, alphaDegree):
        alphaRadian = self.degree2Radian(alphaDegree)
        if np.abs(sin(alphaRadian)) < 1e-4:
            snAlpha = 0
        else:
            snAlpha = sin(alphaRadian)
        return snAlpha

    def getRotateMatrix(self, xDegree, yDegree, zDegree):
        csX = self.cs(xDegree)
        csY = self.cs(yDegree)
        csZ = self.cs(zDegree)

        snX = self.sn(xDegree)
        snY = self.sn(yDegree)
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
        Mr = (Rx.dot(Ry)).dot(Rz)
        print('******************************')
        # print(csY)
        # print(snY)
        # print(Rx)
        # print(Ry)
        # print(Rz)
        # print('===================')
        print('Mr = ')
        print(Mr)
        print('*******************************')
        return Mr
