import sympy as sp
from numpy import sin, cos, pi
from sympy import init_printing, pprint
import numpy as np
import pandas as pd
import scipy as sy


class Rays:
    def __init__(self, mirrorDF, rayinDF):
        self.mirrorDF = self.getMirrorDF(mirrorDF)
        self.rayInDF = self.getRaysInDF(rayinDF)
        self.EinHeaders = 7
        self.RaysDFnormal =  self.rInNormalise()

    def rInNormalise(self):
        RaysHeads = self.rayInDF.columns
        RayCount = 0
        numberOfRays = len(self.rayInDF.Kxin)
        KinNormalArray2D, XinArray2D, EinArray2D = self.initArrasy2D(numberOfRays)
        for RinIndex in self.rayInDF.index:
            # print(RinIndex)
            KinArray = self.getKinArray(RinIndex, )
            KinNormal = self.normalVector(KinArray)
            KinNormalArray2D[RinIndex, :] = KinNormal

            XinArray2D[RinIndex, :] = self.getXinArray(RinIndex)

            Eyin = self.getEy(RinIndex)

            EinArray2D[RinIndex, :] = self.getEinArray(RinIndex, Eyin)

            RayCount += 1

        raysDF = self.setRaysDataFrame(XinArray2D, KinNormalArray2D, EinArray2D)
        return raysDF

    def getMirrorDF(self, mirrorDF):
        return mirrorDF

    def getRaysInDF(self, rayinDF):
        return rayinDF

    def getKinArray(self, RinIndex, ):
        return np.array([self.rayInDF.Kxin[RinIndex],
                         self.rayInDF.Kyin[RinIndex],
                         self.rayInDF.Kzin[RinIndex]
                         ])

    def getXinArray(self, RinIndex):
        return np.array([self.rayInDF.Xin[RinIndex],
                         self.rayInDF.Yin[RinIndex],
                         self.rayInDF.Zin[RinIndex]
                         ])

    def getEy(self, RinIndex):
        return -(self.rayInDF.Exin[RinIndex] * self.rayInDF.Kxin[RinIndex] +
                 self.rayInDF.Ezin[RinIndex] * self.rayInDF.Kzin[RinIndex]) / self.rayInDF.Kyin[RinIndex]

    def getEinArray(self, RinIndex, Eyin):
        return np.array([self.rayInDF.Exin[RinIndex],
                         Eyin,
                         self.rayInDF.Ezin[RinIndex],
                         self.rayInDF.Ex[RinIndex],
                         self.rayInDF.Ey[RinIndex],
                         self.rayInDF.Ez[RinIndex],
                         self.rayInDF.Ain[RinIndex],
                         ])

    def normalVector(self, inArray):
        return inArray / ((np.dot(inArray, inArray.T))) ** 0.5

    def setRaysDataFrame(self, XinArray, KinNormalArray, EinArray):
        raysDF = pd.DataFrame({'Xin': XinArray[:, 0],
                               'Yin': XinArray[:, 1],
                               'Zin': XinArray[:, 2],
                               'Kxin': KinNormalArray[:, 0],
                               'Kyin': KinNormalArray[:, 1],
                               'Kzin': KinNormalArray[:, 2],
                               'Exin': EinArray[:, 0],
                               'Eyin': EinArray[:, 1],
                               'Ezin': EinArray[:, 2],
                               'Xe': EinArray[:, 3],
                               'Ye': EinArray[:, 4],
                               'Ze': EinArray[:, 5],
                               'Ain': EinArray[:, 6],
                               })
        return raysDF

    def initArrasy2D(self, numberOfRays):
        KinNormalArray2D = np.zeros((numberOfRays, 3))
        XinArray2D = np.zeros((numberOfRays, 3))
        EinArray2D = np.zeros((numberOfRays, self.EinHeaders))
        return KinNormalArray2D, XinArray2D, EinArray2D

    def getReflectedRays(self):
        L = 100
        fName = path[1]
        pathReflctedRay = path[0] + fName[1] + path[2]
        pathNormalRay = path[0] + fName[2] + path[2]

        # print('pathReflctedRay', pathReflctedRay)
        # print('pathNormalRay', pathNormalRay)

        x1, x2, x3, a11, a22, a3, x01Ray, x02Ray, x03Ray, k1, k2, k3, v1, v2, v3, t = sp.symbols(
            'x1 x2 x3 a11 a22 a3 x01Ray x02Ray x03Ray k1 k2 k3 v1 v2 v3 t')

        x1R, x2R, x3R, dx1R, dx2R, dx3R = sp.symbols('x1R x2R x3R dx1R dx2R dx3R')
        #  Mirror Parameters
        xDegree = Mirror.Direction[0]
        yDegree = Mirror.Direction[1]
        zDegree = Mirror.Direction[2]

        a11 = 1 / (4 * Mirror.Focus[0])
        a22 = 1 / (4 * Mirror.Focus[2])
        a3 = 1
        v1 = Mirror.Vertex[0]
        v2 = Mirror.Vertex[1]
        v3 = Mirror.Vertex[2]
        # print(a11, a22, a3)
        # print(v1, v2, v3)


        Mr = self.getRotateMatrix(xDegree, yDegree, zDegree)
        xRayCrossArray2D = np.zeros((len(raysDataFrame.index), 3))
        nNormallArray2D = np.zeros((len(raysDataFrame.index), 3))
        eCrossArray2D = np.zeros((len(raysDataFrame.index), 7))

        xDetectorlArray2D = np.zeros((len(raysDataFrame.index), 3))
        kReflectedArray2D = np.zeros((len(raysDataFrame.index), 3))
        eDetectorArray2D = np.zeros((len(raysDataFrame.index), 7))

        # Loop for all Rays
        for RinIndex in raysDataFrame.index:
            print('===========********************   Ray Loop  ***************************** ==============', RinIndex)
            #  RayIn parmetrs

            x0RayAray = np.array([raysDataFrame.Xin[RinIndex] + Mirror.Source[0],
                                  raysDataFrame.Yin[RinIndex] + Mirror.Source[1],
                                  raysDataFrame.Zin[RinIndex] + Mirror.Source[2]
                                  ])

            kinArray = np.array([raysDataFrame.Kxin[RinIndex],
                                 raysDataFrame.Kyin[RinIndex],
                                 raysDataFrame.Kzin[RinIndex]
                                 ])
            eInArray = np.array([raysDataFrame.Exin[RinIndex],
                                 raysDataFrame.Eyin[RinIndex],
                                 raysDataFrame.Ezin[RinIndex]]
                                )

            x1RaySym = x01Ray + k1 * t
            x2RaySym = x02Ray + k2 * t
            x3RaySym = x03Ray + k3 * t

            x1R = (x1 - v1) * Mr[0, 0] + (x2 - v2) * Mr[0, 1] + (x3 - v3) * Mr[0, 2]
            x2R = (x1 - v1) * Mr[1, 0] + (x2 - v2) * Mr[1, 1] + (x3 - v3) * Mr[1, 2]
            x3R = (x1 - v1) * Mr[2, 0] + (x2 - v2) * Mr[2, 1] + (x3 - v3) * Mr[2, 2]

            # print('x1R = ', x1R)
            # print('x2R = ', x2R)
            # print('x3R = ', x3R)

            Expr_A11 = x1R ** 2
            Expr_A22 = x2R ** 2
            Expr_A3 = x3R

            x1RayNum = x0RayAray[0] + kinArray[0] * t
            x2RayNum = x0RayAray[1] + kinArray[1] * t
            x3RayNum = x0RayAray[2] + kinArray[2] * t

            mainExpr = a11 * Expr_A11 + a22 * Expr_A22 - a3 * Expr_A3
            mainExprSubs = mainExpr.subs(x1, x1RaySym)
            mainExprSubsN = mainExpr.subs(x1, x1RayNum)
            mainExprSubs = mainExprSubs.subs(x2, x2RaySym)
            mainExprSubsN = mainExprSubsN.subs(x2, x2RayNum)
            mainExprSubs = mainExprSubs.subs(x3, x3RaySym)
            mainExprSubsN = mainExprSubsN.subs(x3, x3RayNum)
            mainExprExpanded = sp.expand(mainExprSubs)
            mainExprExpandedN = sp.expand(mainExprSubsN)
            mainExprCollctedSym = sp.collect(mainExprExpanded, t)
            mainExprCollctedN = sp.collect(mainExprExpandedN, t)
            A = mainExprCollctedN.coeff(t, 2)
            B = mainExprCollctedN.coeff(t, 1)
            C = mainExprCollctedN.coeff(t, 0)

            # print('mainExpr = ')
            # pprint(mainExpr)
            # print('mainExprSubs = ')
            # pprint(mainExprSubs)
            # print('mainExprExpanded = ')
            # pprint(mainExprExpanded)
            # print('Expr Collected = ')
            # pprint(mainExprCollctedSym)
            # print('mainExprCollctedN = ')
            # pprint(mainExprCollctedN)
            # print('A = ', A)
            # print('B = ', B)
            # print('C = ', C)
            tSolverList = []
            if abs(A) < 1e-6:
                tSolver = -C / B
                tSolverList.append(tSolver)
            else:
                D = (B ** 2 - (4 * A * C))
                if D == 0:
                    tSolver = -B / (2 * A)
                    tSolverList.append(tSolver)
                else:
                    if D > 0:
                        # print('D = ', D)
                        tSolver1 = (-B + (D ** 0.5)) / (2 * A)
                        tSolver2 = (-B - (D ** 0.5)) / (2 * A)
                        tSolverList.append(tSolver1)
                        tSolverList.append(tSolver2)
                    elif D < 0:
                        print('NO SOLITIONS FOR THIS RAYS In REAEL WORD !!!!')
            # print('--------------------  Befor getXRayCrossArray ------------------------ ')
            # print('kinArray = ')
            # print(kinArray)
            # print('x0RayAray = ')
            # print(x0RayAray)
            # print('tSolverList = ')
            # print(tSolverList)
            xRayCrossArray = self.getXRayCrossArray(tSolverList, kinArray, x0RayAray)
            # print('xRayCrossArray = ')
            # print(xRayCrossArray)

            # Differentional of MirrorSurf
            # self.pprintSymbol(N1sym, N2sym, N3sym, N1, N2,N3, mainExpr, mainExprCollctedSym, mainExprSubs, nArray, nNormalArray, xNormal)
            N1symdiff = sp.diff(mainExpr, x1)
            N2symdiff = sp.diff(mainExpr, x2)
            N3symdiff = sp.diff(mainExpr, x3)

            N1sym = N1symdiff.subs(x1, xRayCrossArray[0])
            N2symx2 = N2symdiff.subs(x2, xRayCrossArray[1])
            N2symx3 = N2symx2.subs(x3, xRayCrossArray[2])
            N3symx2 = N3symdiff.subs(x2, xRayCrossArray[1])
            N3symx3 = N3symx2.subs(x3, xRayCrossArray[2])

            nArray = np.array([N1sym,
                               N2symx3,
                               N3symx3
                               ])

            nNormalArray = self.normalVector(nArray)

            kReflectedNormalArray = self.getKreflected(kinArray, nNormalArray)

            xRayDetectorArray = self.getXDetector(Mirror,
                                                  kReflectedNormalArray,
                                                  xRayCrossArray)

            Exin = raysDataFrame.Exin[RinIndex]
            Ezin = raysDataFrame.Ezin[RinIndex]
            Eyin = raysDataFrame.Eyin[RinIndex]
            Ampl = raysDataFrame.Ain[RinIndex]

            ##############################
            eRef = np.zeros((1, 3))
            # r1 = self.rotor(nNormalArray, eInArray)
            # r2 = self.rotor(r1, nNormalArray)

            N1 = (eInArray.dot(nNormalArray.T)) * nNormalArray
            Er1 = self.rotor(nNormalArray, eInArray)
            Er2 = self.rotor(Er1, nNormalArray)
            absN = ((nNormalArray.dot(nNormalArray.T)) ** 0.5)
            eRef = (N1 - Er2) / absN
            # kRef = np.array([N1 -r2])
            ErefNormalArraay = self.normalVector(eRef)
            ErefNormalArraayAbs = abs(ErefNormalArraay)
            eRefMaxIndex = ErefNormalArraayAbs.argmax(0)
            Ain = 100
            if eRefMaxIndex == 0:
                xERef = raysDataFrame.Xe[RinIndex]
                tRef = (xERef - xRayCrossArray[0]) / ErefNormalArraay[0]
                yERef = (xRayCrossArray[1] + ErefNormalArraay[1] * tRef) - Mirror.Offset[1]
                zERef = (xRayCrossArray[2] + ErefNormalArraay[2] * tRef) - Mirror.Offset[2]
            elif eRefMaxIndex == 1:
                yERef = raysDataFrame.Ye[RinIndex]
                tRef = (yERef - xRayCrossArray[1]) / ErefNormalArraay[1]
                xERef = (xRayCrossArray[0] + ErefNormalArraay[0] * tRef) - Mirror.Offset[0]
                zERef = (xRayCrossArray[2] + ErefNormalArraay[2] * tRef) - Mirror.Offset[2]
            elif eRefMaxIndex == 2:
                zERef = raysDataFrame.Ze[RinIndex]
                tRef = (zERef - xRayCrossArray[2]) / ErefNormalArraay[2]
                yERef = (xRayCrossArray[1] + ErefNormalArraay[1] * tRef) - Mirror.Offset[1]
                xERef = (xRayCrossArray[0] + ErefNormalArraay[0] * tRef) - Mirror.Offset[0]
            else:
                zERef = 0
                yERef = 0
                xERef = 0
            eXRefArray = np.array(
                [ErefNormalArraay[0], ErefNormalArraay[1], ErefNormalArraay[2], xERef, yERef, zERef, Ain])

            # xRayCrossArray2D = np.zeros((len(raysDataFrame.index), 3))
            # nNormallArray2D = np.zeros((len(raysDataFrame.index), 3))
            # eCrossArray2D = np.zeros((len(raysDataFrame.index), 7))
            # kReflectedArray2D = np.zeros((len(raysDataFrame.index), 3))

            ##############################

            # print ('xRayDetectorArray = ', xRayDetectorArray)
            xRayCrossArray2D[RinIndex, :] = xRayCrossArray
            nNormallArray2D[RinIndex, :] = nNormalArray
            eCrossArray2D[RinIndex, :] = eXRefArray

            xDetectorlArray2D[RinIndex, :] = xRayDetectorArray
            kReflectedArray2D[RinIndex, :] = kReflectedNormalArray
            eDetectorArray2D[RinIndex, :] = eXRefArray

        # print('xRayCrossArray = ', xRayCrossArray2D)
        # print('nNormallArray2D', nNormallArray2D)
        # print('eCrossArray2D', eCrossArray2D)
        print('***********************************************************************        End Ray Loop', RinIndex)
        NormalRaysDataFrame = self.setRaysDataFrame(xRayCrossArray2D,
                                                    nNormallArray2D,
                                                    eCrossArray2D)
        ReflectedRaysDataFrame = self.setRaysDataFrame(xDetectorlArray2D,
                                                       kReflectedArray2D,
                                                       eDetectorArray2D)
        self.saveRays2Execel(pathNormalRay,
                             NormalRaysDataFrame)
        self.saveRays2Execel(pathReflctedRay,
                             ReflectedRaysDataFrame)