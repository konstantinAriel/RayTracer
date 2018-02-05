import  numpy as np
import pandas as pd

from scr import Rays as r
import scr.RayTracing.Rays as rays

class calcPolarization:
    def __init__(self, rayInDF, normalDF):
        self.x0 = rayInDF.Xin
        self.y0 = rayInDF.Yin
        self.z0 = rayInDF.Zin

        self.xM = normalDF.Xin
        self.yM = normalDF.Yin
        self.zM = normalDF.Zin

        self.kx = rayInDF.Kxin
        self.ky = rayInDF.Kyin
        self.kz = rayInDF.Kzin

        self.nx = normalDF.Kxin
        self.ny = normalDF.Kyin
        self.nz = normalDF.Kzin

        self.Ex = rayInDF.Exin
        self.Ez = rayInDF.Ezin
        self.Ey = self.getEy(rayInDF, self.Ex, self.Ez)

        self.Ampl = rayInDF.Ain

        self.kArray = np.array([self.kx, self.ky, self.kz])
        self.nArray = np.array([self.nx, self.ny, self.nz])
        self.raysObject = r.Rays()
        a = rays.rotor
    def getEy(self, rayIn, Ex, Ez):
        Ey = -(self.kx*Ex + self.kz*Ez)/rayIn.Kyin
        return  Ey

    def getReflectedPolarRay(self, kArray, nArray):
        kRef = np.zeros((1, 3))
        print('kRef  = ')
        print(kRef)
        r1 = rays.rotor(nArray, kArray)
        r2 = rays.rotor(r1, nArray)
        r2Arr = np.array(r2)
        N1 = (kArray.dot(nArray.T)) * nArray
        absN = rays.normalVector(N1)
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
