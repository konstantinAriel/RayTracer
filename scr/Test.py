import numpy as np
import pandas as pd
from numpy import nan

from scr.Rays import Rays


class Test:
    def __init__(self):
        self.rInList = ['Xin', 'KxIn', 'Zin', 'KzIn']
        self.aList = ['a44', 'a444', 'a4444']
        self.rOutList = ['Xout', 'Kxout', 'Zout', 'Kzout']
        self.xMax = 6
        self.kMax = 0.02
        self.nanArray = np.array([[nan, nan, nan, nan],
                                  [nan, nan, nan, nan],
                                  [nan, nan, nan, nan],
                                  [nan, nan, nan, nan]])
        self.numberOfPoints = 3
        self.numberOfRays = (4 + 6 + 4)*self.numberOfPoints
        self.pointArray = np.array([[1], [-1], [0.5]])
        self.RaysZeroDF = self.setZeroRaysDataFrame(self.numberOfRays)

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
                i0+=1
        # Loop for XZ  X^2*Z  Z^2*X
        for rin1 in  range(0, 3):
            for rin2 in range(rin1+1, 4):
                if rin2 == rin1:
                    pass
                else:
                    print(self.rInList[rin1], self.rInList[rin2])
                    for point in self.pointArray:
                        print('point = ', point)
                        self.RaysZeroDF.loc[i0, self.rInList[rin1]] = point
                        self.RaysZeroDF.loc[i0, self.rInList[rin2]] = point
                        i0+=1
        # Loop for XYZ:
        for rin1 in  range(0, 2):
            for rin2 in range(rin1+1, 3):
                for rin3 in range (rin2+1,4):
                        print(self.rInList[rin1], self.rInList[rin2],self.rInList[rin3])
                        for point in self.pointArray:
                            print('point = ', point)
                            self.RaysZeroDF.loc[i0, self.rInList[rin1]] = point
                            self.RaysZeroDF.loc[i0, self.rInList[rin2]] = point
                            self.RaysZeroDF.loc[i0, self.rInList[rin3]] = point
                            i0+=1
        self.RaysZeroDF.loc[:, 'Xin'] = self.RaysZeroDF.Xin * self.xMax
        self.RaysZeroDF.loc[:, 'Zin'] = self.RaysZeroDF.Zin * self.xMax
        self.RaysZeroDF.loc[:, 'KxIn'] = self.RaysZeroDF.KxIn * self.kMax
        self.RaysZeroDF.loc[:, 'KzIn'] = self.RaysZeroDF.KzIn * self.kMax
        self.RaysZeroDF.loc[:, 'KyIn'] = 1
        return self.RaysZeroDF

    def setZeroRaysDataFrame(self, numberOfRays):
        raysZeroDF = pd.DataFrame({'Xin': np.zeros((numberOfRays), dtype='float32'),
                                   'Yin': np.zeros((numberOfRays), dtype='float32'),
                                   'Zin': np.zeros((numberOfRays), dtype='float32'),
                                   'KxIn':np.zeros((numberOfRays), dtype='float32'),
                                   'KyIn':np.zeros((numberOfRays), dtype='float32'),
                                   'KzIn':np.zeros((numberOfRays), dtype='float32'),
                                   'ExIn':np.zeros((numberOfRays), dtype='float32'),
                                   'EyIn':np.zeros((numberOfRays), dtype='float32'),
                                   'EzIn':np.zeros((numberOfRays), dtype='float32'),
                                   'Ain': np.zeros((numberOfRays), dtype='float32')
                                 })
        return raysZeroDF


