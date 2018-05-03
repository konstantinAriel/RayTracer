import sympy as sp
from numpy import sin, cos, pi
from sympy import init_printing, pprint
import numpy as np
import pandas as pd
import scipy as sy

class Rays:
    def __init__(self):
        pass

    def rInNormalise(self, mirrorDataFrame, rInDataFrame):
        RaysHeads = rInDataFrame.columns
        RayCount = 0
        numberOfRays = len(rInDataFrame.Kxin)
        KinNormalArray2D = np.zeros((numberOfRays, 3))
        XinArray2D = np.zeros((numberOfRays, 3))
        EinArray2D = np.zeros((numberOfRays, 7))
        for RinIndex in rInDataFrame.index:
            # print(RinIndex)
            KinArray = np.array([rInDataFrame.Kxin[RinIndex],
                                 rInDataFrame.Kyin[RinIndex],
                                 rInDataFrame.Kzin[RinIndex]
                                 ])
            KinNormal = self.normalVector(KinArray)
            KinNormalArray2D[RinIndex, :] = KinNormal

            XinArray2D[RinIndex, :] = np.array([rInDataFrame.Xin[RinIndex],
                                              rInDataFrame.Yin[RinIndex],
                                              rInDataFrame.Zin[RinIndex]
                                              ])
            Eyin = -(rInDataFrame.Exin[RinIndex]*rInDataFrame.Kxin[RinIndex] + rInDataFrame.Ezin[RinIndex]*rInDataFrame.Kzin[RinIndex] )/ rInDataFrame.Kyin[RinIndex]

            EinArray2D[RinIndex, :] = np.array([rInDataFrame.Exin[RinIndex],
                                                Eyin,
                                              rInDataFrame.Ezin[RinIndex],
                                              rInDataFrame.Exin[RinIndex],
                                              rInDataFrame.Eyin[RinIndex],
                                              rInDataFrame.Ezin[RinIndex],
                                              rInDataFrame.Ain[RinIndex],
                                              ])
            RayCount += 1
            # print('KinNormalArray : ',KinNormalArray)
            # print('KinArray',KinArray)
            # print('KinNormal',KinNormal)
            # print('=========================')
            # print('XinArray=', XinArray)
        raysDF = self.setRaysDataFrame(XinArray2D, KinNormalArray2D, EinArray2D)
        # print('*************')
        # print('KinDF = ')
        # print('raysDF', raysDF)
        return raysDF

    def setRaysDataFrame(self,XinArray,  KinNormalArray, EinArray):
        #print('EinArray',EinArray)
        raysDF = pd.DataFrame({'Xin': XinArray[:, 0],
                               'Yin': XinArray[:, 1],
                               'Zin': XinArray[:, 2],
                               'Kxin': KinNormalArray[:, 0],
                               'Kyin': KinNormalArray[:, 1],
                               'Kzin': KinNormalArray[:, 2],
                               'Exin': EinArray[:, 0],
                               'Eyin': EinArray[:, 1],
                               'Ezin': EinArray[:, 2],
                               'Xe':   EinArray[:, 3],
                               'Ye':   EinArray[:, 4],
                               'Ze':   EinArray[:, 5],
                               'Ain':  EinArray[:, 6],
                               })
        return raysDF

    def saveRays2Execel(self, fileName, raysDataFrame):
        raysDataFrame.to_excel(fileName)

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
    ##  def pprintSymbol   NO U s a g e !!!
    def pprintSymbol(self, N1sym, N2sym, N3sym, N1,N2, N3, mainExpr, mainExprCollcted, mainExprSubs, nArray, nNormal, xNormal):
        print('mainExpr = ')
        pprint(mainExpr)
        print('mainExprSubs = ')
        pprint(mainExprSubs)
        # print('mainExprExpanded = ')
        # pprint(mainExprExpanded)
        print('Expr Collected = ')
        pprint(mainExprCollcted)
        # print('t = ')
        # pprint(tSolver)
        print('N1sym = ')
        pprint(N1sym)
        print('N2sym = ')
        pprint(N2sym)
        print('N3sym = ')
        pprint(N3sym)
        print('N1 = ')
        pprint(N1)
        print('N2 = ')
        pprint(N2)
        print('N3 = ')
        pprint(N3)
        print('nArray = ', nArray)
        print('nNormal = ', nNormal)
        print('xNormal =', xNormal)

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
        # print('******************************')
        # print(csX)
        # print(csY)
        # print(csZ)
        # print(snX)
        # print(snY)
        # print(snZ)
        # print(Rx)
        # print(Ry)
        # print(Rz)
        # print('===================')
        # print('Mr = ')
        # print(Mr)
        # print('*******************************')
        return Mr

    def rotor(self, nArray, kinArray):
        c11 = (nArray[1]*kinArray[2]) - (nArray[2]*kinArray[1])
        c12 = -((nArray[0]*kinArray[2]) - (nArray[2]*kinArray[0]))
        c13 = (nArray[0]*kinArray[1]) - (nArray[1]*kinArray[0])
        return [c11, c12, c13]

    def normalVector(self, inArray):
        return inArray / ((np.dot(inArray, inArray.T)))**0.5

    def getXDetector(self, MirrorDataSheet, kReflectedNormal, xRayCrossArray):
        xDetArray = np.array([0,0,0])
        if (MirrorDataSheet.Detector[0] - MirrorDataSheet.Offset[0]) == 0:
            pass
        else:
            tRef1 = (MirrorDataSheet.Detector[0] - xRayCrossArray[0]) / kReflectedNormal[0]
            x1det = MirrorDataSheet.Detector[0]
            x2det = xRayCrossArray[1] + tRef1 * kReflectedNormal[1]
            x3det = xRayCrossArray[2] + tRef1 * kReflectedNormal[2]
            xDetArray = np.array([x1det, x2det, x3det])
        if (MirrorDataSheet.Detector[1] - MirrorDataSheet.Offset[1]) == 0:
            pass
        else:
            tRef2 = (MirrorDataSheet.Detector[1] - xRayCrossArray[1]) / kReflectedNormal[1]
            x1det = xRayCrossArray[0] + tRef2 * kReflectedNormal[0]
            x2det = MirrorDataSheet.Detector[1]
            x3det = xRayCrossArray[2] + tRef2 * kReflectedNormal[2]
            xDetArray = np.array([x1det, x2det, x3det])
        if (MirrorDataSheet.Detector[2] - MirrorDataSheet.Offset[2]) == 0:
            pass
        else:
            tRef3 = (MirrorDataSheet.Detector[2] - xRayCrossArray[2]) / kReflectedNormal[2]
            x1det = xRayCrossArray[0] + tRef3 * kReflectedNormal[0]
            x2det = xRayCrossArray[1] + tRef3 * kReflectedNormal[1]
            x3det = MirrorDataSheet.Detector[2]
            xDetArray = np.array([x1det, x2det, x3det])
        #print('xDetectorArray', xDetArray)
        xDetArray[0] = xDetArray[0] - MirrorDataSheet.Detector[0]
        xDetArray[1] = xDetArray[1] - MirrorDataSheet.Detector[1]
        xDetArray[2] = xDetArray[2] - MirrorDataSheet.Detector[2]
        #print('xDetArray', xDetArray)
        return xDetArray

    def getKreflected(self, kinArray, nNormalArray):
        r1 = self.rotor(nNormalArray, kinArray)
        r2 = self.rotor(r1, nNormalArray)
        N11 = (kinArray.dot(nNormalArray.T)) * nNormalArray
        absN = (nNormalArray.dot(nNormalArray.T)) ** 0.5
        kReflected = (r2 - N11) / absN
        kReflectedNormal = self.normalVector(kReflected)
        #print('kReflectedNormal', kReflectedNormal)
        return kReflectedNormal

    def calcReflectedRays(self, path, Mirror, raysDataFrame):
        # print(Mirror)
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
            #print('===========******Calcilation Reflected Rays ***************************** ==============', RinIndex )
        #  RayIn parmetrs

            x0RayAray = np.array([raysDataFrame.Xin[RinIndex]  + Mirror.Source[0],
                                   raysDataFrame.Yin[RinIndex] + Mirror.Source[1],
                                   raysDataFrame.Zin[RinIndex] + Mirror.Source[2]
                                   ])

            kinArray = np.array([raysDataFrame.Kxin[RinIndex],
                                 raysDataFrame.Kyin[RinIndex],
                                 raysDataFrame.Kzin[RinIndex]
                                 ])
            eInArray = np.array([raysDataFrame.Exin[RinIndex] ,
                                 raysDataFrame.Eyin[RinIndex] ,
                                 raysDataFrame.Ezin[RinIndex] ]
                                 )

            x1RaySym = x01Ray + k1*t
            x2RaySym = x02Ray + k2*t
            x3RaySym = x03Ray + k3*t

            x1R = (x1 - v1) * Mr[0, 0] + (x2 - v2) * Mr[0, 1] + (x3 - v3) * Mr[0, 2]
            x2R = (x1 - v1) * Mr[1, 0] + (x2 - v2) * Mr[1, 1] + (x3 - v3) * Mr[1, 2]
            x3R = (x1 - v1) * Mr[2, 0] + (x2 - v2) * Mr[2, 1] + (x3 - v3) * Mr[2, 2]

            # print('x1R = ', x1R)
            # print('x2R = ', x2R)
            # print('x3R = ', x3R)

            Expr_A11 = x1R**2
            Expr_A22 = x2R**2
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
                tSolver = -C/B
                tSolverList.append(tSolver)
            else:
                D = (B**2 - (4*A*C))
                if D == 0:
                    tSolver = -B/(2*A)
                    tSolverList.append(tSolver)
                else:
                    if D > 0:
                        # print('D = ', D)
                        tSolver1 = (-B + (D**0.5))/(2*A)
                        tSolver2 = (-B - (D**0.5))/(2*A)
                        tSolverList.append(tSolver1)
                        tSolverList.append(tSolver2)
                    elif D<0:
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
            #self.pprintSymbol(N1sym, N2sym, N3sym, N1, N2,N3, mainExpr, mainExprCollctedSym, mainExprSubs, nArray, nNormalArray, xNormal)
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
            eRef = (N1 - Er2)/absN
            #kRef = np.array([N1 -r2])
            ErefNormalArraay = self.normalVector(eRef)
            ErefNormalArraayAbs = abs(ErefNormalArraay)
            eRefMaxIndex = ErefNormalArraayAbs.argmax(0)
            Ain = 100
            # zERef = 0
            # yERef = 0
            # xERef = 0
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
            eXRefArray = np.array([ErefNormalArraay[0], ErefNormalArraay[1], ErefNormalArraay[2], xERef, yERef, zERef, Ain])

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
        #print('eCrossArray2D', eCrossArray2D)
        print('********************* Calcilation Reflected Rays *************************** TOTAL RAYS is  ' , RinIndex)
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
        print('pathNormalRay = ', pathNormalRay)
        print('pathReflctedRay = ', pathReflctedRay)





