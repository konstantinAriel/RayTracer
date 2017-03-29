

import numpy as np
import pandas as pd
import scipy as sy

class Rays:
    def __init__(self, kInArray):
        self.kInArray = kInArray

    def calcRInNormal(self,kInArray):
        return (kInArray/(np.sqrt(np.dot(kInArray, kInArray.T))))

    #def findCrossPoint(self, Rin):
