import numpy as np
import pandas as pd
from numpy import nan

class Test:
    def __init__(self):
        self.rInLisl = ['Xin', 'KXin', 'Zin', 'KZin']
        self.aList = ['a44', 'a444', 'a4444']
        self.rOutList = ['Xout', 'KXout', 'Zout', 'KZout']

        self.nanArray = np.array([[nan, nan, nan, nan],
                                  [nan, nan, nan, nan],
                                  [nan, nan, nan, nan],
                                  [nan, nan, nan, nan]])

    def testloop(self):
        for rIn in self.rInLisl:
            dict44 = dict(self.nanArray)
