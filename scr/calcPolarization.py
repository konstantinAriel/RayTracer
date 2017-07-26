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

        self.kArray = np.array([self.kx, self.ky, self.kz])
        self.nArray = np.array([self.nx, self.ny, self.nz])
        self.raysObject = r.Rays()
    def getEy(self, rayIn, Ex, Ez):
        Ey = -(rayIn.Kxin*Ex + rayIn.Kzin*Ez)/rayIn.Kyin
        return  Ey

    def getReflectedPolarRay(self, kArray, nArray):

        r1 = self.raysObject.rotor(nArray, kArray)
        r2 = self.raysObject.rotor(r1, nArray)

        N1 = (kArray*nArray.T)*nArray
        print('N1 = ')
        print(N1)
        print('r2 = ')
        print(r2)
        absN = self.raysObject.normalVector(self.nArray)
        kRef = (-1*r2 + N1)
        absKref = self.raysObject.normalVector(kRef)
        krefN = kRef/absKref
        return krefN
