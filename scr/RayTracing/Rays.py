import sympy as sp
from numpy import sin, cos, pi
import numpy as np
import pandas as pd

class Rays:
    def __init__(self, mirrorDF, rayinDF, getRefRay):
            self.mirrorDF = self.getMirrorDF(mirrorDF)
            self.rayInDF = self.getRaysInDF(rayinDF)
            # print('rayinDF =  IN RAYS CLASS')
            # print(rayinDF)
            self.EinHeaders = 3
            self.L =100
            if getRefRay == 1:
                self.NormalRayDF, self.ReflectedRayDF, self.xPleneLineRaysDF = self.getReflectedRays()
            elif getRefRay == 0:
                self.RaysDFnormal =  self.rInNormalise()

    # def rInNormalise(self):
    #     #RaysHeads = self.rayInDF.columns
    #     RayCount = 0
    #     numberOfRays = len(self.rayInDF.Kx)
    #     KinNormalArray2D, XinArray2D, EinArray2D = self.initArrasy2D(numberOfRays)
    #     for RinIndex in self.rayInDF.index:
    #         # print(RinIndex)
    #         KinArray = self.getKinArray(RinIndex)
    #         KinNormal = self.normalVector(KinArray)
    #         KinNormalArray2D[RinIndex, :] = KinNormal
    #
    #         XinArray2D[RinIndex, :] = self.getXinArray(RinIndex)
    #
    #         # Ey = self.getEy(RinIndex)
    #
    #         EinArray2D[RinIndex, :] = self.getEinArray(RinIndex)
    #
    #         RayCount += 1
    #
    #     raysDF = self.setRaysDataFrame(XinArray2D, KinNormalArray2D, EinArray2D)
    #     return raysDF
    def rInNormalise(self):
        #RaysHeads = self.rayInDF.columns
        RayCount = 0
        numberOfRays = len(self.rayInDF.Kx)
        KinNormalArray2D, XinArray2D, EinArray2D = self.initArrasy2D(numberOfRays)
        for RinIndex in self.rayInDF.index:
            # print(RinIndex)
            KinArray = self.getKinArray(RinIndex)
            KinNormal = self.normalVector(KinArray)
            KinNormalArray2D[RinIndex, :] = KinNormal

            XinArray2D[RinIndex, :] = self.getXinArray(RinIndex)

            # Ey = self.getEy(RinIndex)

            EinArray2D[RinIndex, :] = self.getEinArray(RinIndex)

            RayCount += 1

        raysDF = self.setRaysDataFrame(XinArray2D, KinNormalArray2D, EinArray2D)
        return raysDF
    def getMirrorDF(self, mirrorDF):
        return mirrorDF

    def getRaysInDF(self, rayinDF):
        return rayinDF

    def getKinArray(self, RinIndex, ):
        return np.array([self.rayInDF.Kx[RinIndex],
                         self.rayInDF.Ky[RinIndex],
                         self.rayInDF.Kz[RinIndex]
                         ])

    def getXinArray(self, RinIndex):
        return np.array([self.rayInDF.X[RinIndex],
                         self.rayInDF.Y[RinIndex],
                         self.rayInDF.Z[RinIndex]
                         ])

    def getEy(self, RinIndex):
        return  np.array([self.rayInDF.Ex[RinIndex],
                         self.rayInDF.Ey[RinIndex],
                         self.rayInDF.Ez[RinIndex]
                         ])

    def getEinArray(self, RinIndex):
        return np.array([self.rayInDF.Ex[RinIndex],
                         self.rayInDF.Ey[RinIndex],
                         self.rayInDF.Ez[RinIndex]
                         ])
    # def normalVector(self, inArray):
    #     return inArray / ((np.dot(inArray, inArray.T))) ** 0.5

    def normalVector(self, inArray):
        return inArray

    def setRaysDataFrame(self, XinArray, KinNormalArray, EinArray):
        raysDF = pd.DataFrame({'X': XinArray[:, 0],
                               'Y': XinArray[:, 1],
                               'Z': XinArray[:, 2],
                               'Kx': KinNormalArray[:, 0],
                               'Ky': KinNormalArray[:, 1],
                               'Kz': KinNormalArray[:, 2],
                               'Ex': EinArray[:, 0],
                               'Ey': EinArray[:, 1],
                               'Ez': EinArray[:, 2],
                               })
        return raysDF

    def initArrasy2D(self, numberOfRays):
        KinNormalArray2D = np.zeros((numberOfRays, 3))
        XinArray2D = np.zeros((numberOfRays, 3))
        EinArray2D = np.zeros((numberOfRays, self.EinHeaders))
        return KinNormalArray2D, XinArray2D, EinArray2D

    def getReflectedRays(self):

        x1, x2, x3, a11, a22, a3, x01Ray, x02Ray, x03Ray, k1, k2, k3, v1, v2, v3, t = sp.symbols(
            'x1 x2 x3 a11 a22 a3 x01Ray x02Ray x03Ray k1 k2 k3 v1 v2 v3 t')

        x1R, x2R, x3R, dx1R, dx2R, dx3R = sp.symbols('x1R x2R x3R dx1R dx2R dx3R')
        #  Mirror Parameters

        ## SET INIT VALUE ***********************************
        Mr, a11, a22, a3, \
        eCrossArray2D, eDetectorArray2D, kReflectedArray2D, nNormallArray2D, eInArraay2D, \
        v1, v2, v3, \
        xDetectorlArray2D, xRayCrossArray2D,xPlaneCrossArray2D, Kin2DArray  = self.setInitValue(
                                                                a11, a22, a3, v1, v2, v3)
        #***********************************************
        # Loop for all Rays
        print('===========********************   Ray Loop  ***************************** ==============')
        for RinIndex in self.rayInDF.index:
            #print('===========********************   Ray Loop  ***************************** ==============', RinIndex)
            #  RayIn parmetrs

            eInArray, kinArray, x0RayAray = self.getInArray(RinIndex)

            x1Plane, x2Plane, x3Plane = self.getPlaneLinePoint(kinArray, x0RayAray, -200)

            xPlaneCrossArray2D[RinIndex,0] = x1Plane
            xPlaneCrossArray2D[RinIndex,1] = x2Plane
            xPlaneCrossArray2D[RinIndex,2] = x3Plane

            x1RaySym = x01Ray + k1 * t
            x2RaySym = x02Ray + k2 * t
            x3RaySym = x03Ray + k3 * t

            # x1R = (x1 - v1) * Mr[0, 0] + (x2 - v2) * Mr[0, 1] + (x3 - v3) * Mr[0, 2]
            # x2R = (x1 - v1) * Mr[1, 0] + (x2 - v2) * Mr[1, 1] + (x3 - v3) * Mr[1, 2]
            # x3R = (x1 - v1) * Mr[2, 0] + (x2 - v2) * Mr[2, 1] + (x3 - v3) * Mr[2, 2]

            x1R = (x1 - v1) * Mr[0, 0] + (x2 - v2) * Mr[1, 0] + (x3 - v3) * Mr[2, 0]
            x2R = (x1 - v1) * Mr[0, 1] + (x2 - v2) * Mr[1, 1] + (x3 - v3) * Mr[2, 1]
            x3R = (x1 - v1) * Mr[0, 2] + (x2 - v2) * Mr[1, 2] + (x3 - v3) * Mr[2, 2]

            print('x1R = ', x1R)
            print('x2R = ', x2R)
            print('x3R = ', x3R)
            print('Mr')
            print(Mr)
            print('Mr[0, 0]', Mr[0, 0])
            print('Mr[0, 1]', Mr[0, 1])
            print('Mr[0, 2]', Mr[0, 2])
            print('Mr[1, 0]', Mr[1, 0])
            print('Mr[1, 1]', Mr[1, 1])
            print('Mr[1, 2]', Mr[1, 2])
            print('Mr[2, 0]', Mr[2, 0])
            print('Mr[2, 1]', Mr[2, 1])
            print('Mr[2, 2]', Mr[2, 2])

            Expr_A11 = x1R ** 2
            Expr_A22 = x2R ** 2
            Expr_A3 = x3R
            print('Expr_A11')
            print(Expr_A11)
            print('Expr_A22')
            print(Expr_A22)
            print('Expr_A3')
            print(Expr_A3)

            x1RayNum = x0RayAray[0] + kinArray[0] * t
            x2RayNum = x0RayAray[1] + kinArray[1] * t
            x3RayNum = x0RayAray[2] + kinArray[2] * t

            mainExpr = a11 * Expr_A11 + a22 * Expr_A22 - a3 * Expr_A3
            # print('mainExpr')
            # print(mainExpr)
            mainExprSubs = mainExpr.subs(x1, x1RaySym)
            mainExprSubsN = mainExpr.subs(x1, x1RayNum)
            mainExprSubs = mainExprSubs.subs(x2, x2RaySym)
            mainExprSubsN = mainExprSubsN.subs(x2, x2RayNum)
            mainExprSubs = mainExprSubs.subs(x3, x3RaySym)
            mainExprSubsN = mainExprSubsN.subs(x3, x3RayNum)

            # print(mainExprSubsN)
            # print('mainExprSubsN')
            mainExprExpanded = sp.expand(mainExprSubs)
            mainExprExpandedN = sp.expand(mainExprSubsN)
            # print(mainExprExpandedN)
            # print('mainExprExpandedN')
            mainExprCollctedSym = sp.collect(mainExprExpanded, t)
            mainExprCollctedN = sp.collect(mainExprExpandedN, t)
            A = mainExprCollctedN.coeff(t, 2)
            B = mainExprCollctedN.coeff(t, 1)
            C = mainExprCollctedN.coeff(t, 0)


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

            xRayCrossArray = self.getXRayCrossArray(tSolverList, kinArray, x0RayAray)

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

            xRayDetectorArray = self.getXDetector(kReflectedNormalArray,
                                                  xRayCrossArray)

            eInNormalArray = self.normalVector(eInArray)

                                                ##          P o l a r i z a t i o n

            #Ampl = self.rayInDF.Ain[RinIndex]
            Ampl = 1

            N1 = (eInNormalArray.dot(nNormalArray.T)) * nNormalArray
            Er1 = self.rotor(nNormalArray, eInNormalArray)
            Er2 = self.rotor(nNormalArray, Er1)
            absN = ((nNormalArray.dot(nNormalArray.T)) ** 0.5)
            ErefNormalArray = (N1 + Er2) / absN

            # kRef = np.array([N1 -r2])
            # ErefNormalArray = self.normalVector(eRef)
            # ErefNormalArraayAbs = abs(ErefNormalArray)
            # eRefMaxIndex = ErefNormalArraayAbs.argmax(0)
            # eRefMaxIndex = ErefNormalArraayAbs.argmax(0)
            #eRefMaxIndex = ErefNormalArray.argmax(0)

            ##   The point of vector polarization from the  mirror surf
            #  X = X0 + t*Ampl
            # XeCross =  (xRayCrossArray[0]  +  ErefNormalArray[0] * Ampl)
            # YeCross =  (xRayCrossArray[1]  +  ErefNormalArray[1] * Ampl)
            # ZeCross =  (xRayCrossArray[2]  +  ErefNormalArray[2] * Ampl)
            ##   The point of vector polarization the  detector  surf
            # XeDetector =  xRayDetectorArray[0]  +  ErefNormalArray[0] * Ampl
            # YeDetector =  xRayDetectorArray[1]  +  ErefNormalArray[1] * Ampl
            # ZeDetector =  xRayDetectorArray[2]  +  ErefNormalArray[2] * Ampl

            # if eRefMaxIndex == 0:
            #     XeCross= xRayCrossArray[0]
            #     XeDetector = xRayDetectorArray[0]
            #     tRefCross = (XeCross - xRayCrossArray[0]) / ErefNormalArray[0]
            #     tRefDetector = (XeDetector - xRayCrossArray[0]) / ErefNormalArray[0]
            #     YeCros = (xRayCrossArray[1] + ErefNormalArray[1] * tRef)
            #     ZeCros = (xRayCrossArray[2] + ErefNormalArray[2] * tRef)
            #
            #     YeDetector = (xRayDetectorArray[1] + ErefNormalArray[1] * tRef)
            #     ZeDetector = (xRayDetectorArray[2] + ErefNormalArray[2] * tRef)
            # elif eRefMaxIndex == 1:
            #     YeCros= self.rayInDF.Ye[RinIndex]
            #     YeDetector = self.rayInDF.Ye[RinIndex]
            #     tRef = (Ye - xRayCrossArray[1]) / ErefNormalArray[1]
            #     XeCros = (xRayCrossArray[0] + ErefNormalArray[0] * tRef) - self.mirrorDF.Offset[0]
            #     ZeCros = (xRayCrossArray[2] + ErefNormalArray[2] * tRef) - self.mirrorDF.Offset[2]
            #     XeDetector= (xRayCrossArray[0] + ErefNormalArray[0] * tRef) - self.mirrorDF.Offset[0]
            #     ZeDetector = (xRayCrossArray[2] + ErefNormalArray[2] * tRef) - self.mirrorDF.Offset[2]
            # elif eRefMaxIndex == 2:
            #     ZeCross = self.rayInDF.Ze[RinIndex]
            #     ZeDetector = xRayDetectorArray[2]
            #     tRef = (Ze - xRayCrossArray[2]) / ErefNormalArray[2]
            #     YeCross = (xRayCrossArray[1] + ErefNormalArray[1] * tRef) - self.mirrorDF.Offset[1]
            #     XeCross = (xRayCrossArray[0] + ErefNormalArray[0] * tRef) - self.mirrorDF.Offset[0]
            #
            #     YeDetector = (xRayCrossArray[1] + ErefNormalArray[1] * tRef) - self.mirrorDF.Offset[1]
            #     XeDetector = (xRayCrossArray[0] + ErefNormalArray[0] * tRef) - self.mirrorDF.Offset[0]
            # else:
            #     Xe = 0
            #     Ye = 0
            #     Ze = 0
            #

            eXRefCrossArray = np.array(
                                 [ErefNormalArray[0],
                                  ErefNormalArray[1],
                                  ErefNormalArray[2],
                                  ])

            eXRefDetectorArray = np.array(
                                    [ErefNormalArray[0],
                                    ErefNormalArray[1],
                                    ErefNormalArray[2],
                                    ])


            xRayCrossArray2D[RinIndex, :] = xRayCrossArray
            nNormallArray2D[RinIndex, :] = nNormalArray
            eCrossArray2D[RinIndex, :] = eXRefCrossArray

            xDetectorlArray2D[RinIndex, :] = xRayDetectorArray
            kReflectedArray2D[RinIndex, :] = kReflectedNormalArray
            eDetectorArray2D[RinIndex, :] = eXRefDetectorArray
            eInArraay2D[RinIndex, :] = eInNormalArray
            Kin2DArray[RinIndex, :] = kinArray
        print('*********************************************************************** End Ray Loop', RinIndex)

        NormalRaysDF = self.setRaysDataFrame(xRayCrossArray2D,
                                            nNormallArray2D,
                                            eCrossArray2D)
        ReflectedRaysDF = self.setRaysDataFrame(xDetectorlArray2D,
                                                kReflectedArray2D,
                                                eDetectorArray2D)

        xPleneLineRaysDF = self.setRaysDataFrame(xPlaneCrossArray2D,
                                                 Kin2DArray,
                                                 eInArraay2D)
        # self.saveRays2Execel(pathNormalRay,
        #                      NormalRaysDF)
        # self.saveRays2Execel(pathReflctedRay,
        #                      ReflectedRaysDF)
        return NormalRaysDF, ReflectedRaysDF, xPleneLineRaysDF


    def getInArray(self, RinIndex):
        x0RayArray = np.array([self.rayInDF.X[RinIndex] + self.mirrorDF.Source[0],
                              self.rayInDF.Y[RinIndex] + self.mirrorDF.Source[1],
                              self.rayInDF.Z[RinIndex] + self.mirrorDF.Source[2]
                              ])
        kinArray = np.array([self.rayInDF.Kx[RinIndex],
                             self.rayInDF.Ky[RinIndex],
                             self.rayInDF.Kz[RinIndex]
                             ])

        Ex = self.rayInDF.Ex[RinIndex]
        Ez = self.rayInDF.Ez[RinIndex]
        Ey = self.rayInDF.Ey[RinIndex]
        # Ey = -(self.rayInDF.Kx[RinIndex]*Ex + self.rayInDF.Kz[RinIndex]*Ez)/self.rayInDF.Ky[RinIndex]

        eInArray = np.array([Ex,
                             Ey,
                             Ez]
                            )
        return eInArray, kinArray, x0RayArray

    def setInitValue(self, a11, a22, a3, v1, v2, v3):
        xDegree = self.mirrorDF.Direction[0]
        yDegree = self.mirrorDF.Direction[1]
        zDegree = self.mirrorDF.Direction[2]
        a11 = 1 / (4 * self.mirrorDF.Focus[0])
        a22 = 1 / (4 * self.mirrorDF.Focus[2])
        a3 = 1
        v1 = self.mirrorDF.Vertex[0]
        v2 = self.mirrorDF.Vertex[1]
        v3 = self.mirrorDF.Vertex[2]
        # print(a11, a22, a3)
        # print(v1, v2, v3)
        Mr = self.getRotateMatrix(xDegree, yDegree, zDegree)
        xRayCrossArray2D = np.zeros((len(self.rayInDF.index), 3))
        nNormallArray2D = np.zeros((len(self.rayInDF.index), 3))
        eCrossArray2D = np.zeros((len(self.rayInDF.index), self.EinHeaders))
        xDetectorlArray2D = np.zeros((len(self.rayInDF.index), 3))
        xPleneCrossArray2D = np.zeros((len(self.rayInDF.index), 3))
        kReflectedArray2D = np.zeros((len(self.rayInDF.index), 3))
        eDetectorArray2D = np.zeros((len(self.rayInDF.index), self.EinHeaders))
        eInArraay2D = np.zeros((len(self.rayInDF.index), 3))
        Kin2DArray = np.zeros((len(self.rayInDF.index), 3))
        return Mr, a11, a22, a3, \
               eCrossArray2D, eDetectorArray2D, kReflectedArray2D, \
               nNormallArray2D, eInArraay2D, v1, v2, v3, \
               xDetectorlArray2D, xRayCrossArray2D, xPleneCrossArray2D, Kin2DArray

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
            [csY, 0, -snY],
            [0, 1, 0],
            [snY, 0, csY]
        ])
        Rz = np.array([
            [csZ, -snZ, 0],
            [snZ, csZ, 0],
            [0, 0, 1]
        ])
        Mr = (Rx.dot(Ry)).dot(Rz)
        return Mr

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

    def degree2Radian(self, alphaDegree):
        return (alphaDegree * pi) / 180

    def getXRayCrossArray(self, tSolver, kinArray, x0RayAraay):
        # print('tsolver',tSolver)
        tList = []
        for tindex in tSolver:
            # print('tindex', tindex)
            if tindex > 0:
                tList.append(tindex)
        # print(tList)
        if len(tList)>1:
            tRoot = min(tList)
        else:
            try:
                tRoot = tList[0]
            except:
                tRoot=0
                print('ERROR')
        # print('TSolver = ', tSolver)
        # print('tRoot = ', (tRoot))
        return  np.array([x0RayAraay[0] + kinArray[0]*tRoot,
                          x0RayAraay[1] + kinArray[1]*tRoot,
                          x0RayAraay[2] + kinArray[2]*tRoot
                          ])

    def getKreflected(self, kinArray, nNormalArray):
        r1 = self.rotor(nNormalArray, kinArray)
        r2 = self.rotor(r1, nNormalArray)
        N11 = (kinArray.dot(nNormalArray.T)) * nNormalArray
        absN = (nNormalArray.dot(nNormalArray.T)) ** 0.5
        kReflected = (r2 - N11) / absN
        kReflectedNormal = self.normalVector(kReflected)
        #print('kReflectedNormal', kReflectedNormal)
        return kReflectedNormal

    def rotor(self, nArray, kinArray):
        c11 = (nArray[1]*kinArray[2]) - (nArray[2]*kinArray[1])
        c12 = -((nArray[0]*kinArray[2]) - (nArray[2]*kinArray[0]))
        c13 = (nArray[0]*kinArray[1]) - (nArray[1]*kinArray[0])
        return [c11, c12, c13]

    def getXDetector(self, kReflectedNormal, xRayCrossArray):
        xDetArray = np.array([0,0,0])
        if (self.mirrorDF.Detector[0] - self.mirrorDF.Offset[0]) == 0:
            pass
        else:
            tRef1 = (self.mirrorDF.Detector[0] - xRayCrossArray[0]) / kReflectedNormal[0]
            x1det = self.mirrorDF.Detector[0]
            x2det = xRayCrossArray[1] + tRef1 * kReflectedNormal[1]
            x3det = xRayCrossArray[2] + tRef1 * kReflectedNormal[2]
            xDetArray = np.array([x1det, x2det, x3det])
        if (self.mirrorDF.Detector[1] - self.mirrorDF.Offset[1]) == 0:
            pass
        else:
            tRef2 = (self.mirrorDF.Detector[1] - xRayCrossArray[1]) / kReflectedNormal[1]
            x1det = xRayCrossArray[0] + tRef2 * kReflectedNormal[0]
            x2det = self.mirrorDF.Detector[1]
            x3det = xRayCrossArray[2] + tRef2 * kReflectedNormal[2]
            xDetArray = np.array([x1det, x2det, x3det])
        if (self.mirrorDF.Detector[2] - self.mirrorDF.Offset[2]) == 0:
            pass
        else:
            tRef3 = (self.mirrorDF.Detector[2] - xRayCrossArray[2]) / kReflectedNormal[2]
            x1det = xRayCrossArray[0] + tRef3 * kReflectedNormal[0]
            x2det = xRayCrossArray[1] + tRef3 * kReflectedNormal[1]
            x3det = self.mirrorDF.Detector[2]
            xDetArray = np.array([x1det, x2det, x3det])
        #print('xDetectorArray', xDetArray)
        xDetArray[0] = xDetArray[0] - self.mirrorDF.Detector[0]
        xDetArray[1] = xDetArray[1] - self.mirrorDF.Detector[1]
        xDetArray[2] = xDetArray[2] - self.mirrorDF.Detector[2]
        #print('xDetArray', xDetArray)
        return xDetArray

    def saveRays2Execel(self, fileName, raysDataFrame):
        raysDataFrame.to_excel(fileName)

    def getPlaneLinePoint(self, kinArray, x0RayAray, D ):
        t = -(x0RayAray[1]+D)/(kinArray[1])
        x1 = x0RayAray[0] + kinArray[0] * t
        x2 = x0RayAray[1] + kinArray[1] * t
        x3 = x0RayAray[2] + kinArray[2] * t
        return x1, x2, x3