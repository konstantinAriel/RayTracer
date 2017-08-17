import  numpy as np
import pandas as pd

from scr import Rays as r


class calcPolarization:
    def __init__(self, rayIn, normal):
        self.x0 = rayIn.Xin
        self.y0 = rayIn.Yin
        self.z0 = rayIn.Zin

        self.xM = normal.Xin
        self.yM = normal.Yin
        self.zM = normal.Zin

        self.kx = rayIn.Kxin
        self.ky = rayIn.Kyin
        self.kz = rayIn.Kzin

        self.nx = normal.Kxin
        self.ny = normal.Kyin
        self.nz = normal.Kzin

        self.Ex = self.kz
        self.Ez = self.ky
        self.Ey = self.getEy(rayIn, self.Ex, self.Ez)

        self.Ampl = rayIn.Ain

        self.kArray = np.array([self.kx, self.ky, self.kz])
        self.nArray = np.array([self.nx, self.ny, self.nz])
        self.raysObject = r.Rays()
    def getEy(self, rayIn, Ex, Ez):
        Ey = -(rayIn.Kxin*Ex + rayIn.Kzin*Ez)/rayIn.Kyin
        return  Ey

    def getReflectedPolarRay(self, kArray, nArray):
        kRef = np.zeros((1, 3))
        print('kRef  = ')
        print(kRef)
        r1 = self.raysObject.rotor(nArray, kArray)
        r2 = self.raysObject.rotor(r1, nArray)
        r2Arr = np.array(r2)
        N1 = (kArray.dot(nArray.T)) * nArray
        absN = self.raysObject.normalVector(N1)
        print('N1')
        print(absN)
        # print(N1[1]-r2[1])
        # print(N1[2]-r2[2])
        kRef = (absN-r2)
        # kRef = np.array([N1 -r2])
        absKref = self.raysObject.normalVector(kRef)
        print('kRef = ')
        print(kRef)
        print('abskRef = ')
        print(absKref)
        krefMaxIndex = absKref.argmax(0)
        print(krefMaxIndex)
        if krefMaxIndex == 0:
            xRef = self.Ampl
            tRef = (xRef - self.xM)/absKref[0]
            yRef = self.yM + absKref[1]*tRef
            zRef = self.zM + absKref[2]*tRef
        elif krefMaxIndex == 1:
            yRef = self.Ampl
            tRef = (yRef - self.yM) / absKref[1]
            xRef = self.yM + absKref[0] * tRef
            zRef = self.zM + absKref[2] * tRef
        elif krefMaxIndex == 2:
            zRef = self.Ampl
            tRef = (zRef - self.zM) / absKref[2]
            yRef = self.yM + absKref[1] * tRef
            xRef = self.zM + absKref[0] * tRef
        xRefArray  = np.array([xRef, yRef, zRef])

        # xRayCrossArray2D = np.zeros((len(raysDataFrame.index), 3))
        #
        # nNormallArray2D = np.zeros((len(raysDataFrame.index), 3))
        #
        # eCrossArray2D = np.zeros((len(raysDataFrame.index), 4))
        #
        # kReflectedArray2D = np.zeros((len(raysDataFrame.index), 3))

        return absKref, xRefArray
