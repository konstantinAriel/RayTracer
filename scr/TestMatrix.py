import numpy as np
import pandas as pd

from scr.MainParam import Parametrs


class TestMatrix:
    def __init__(self, path, mirrorDataSheet, mirrorList):
        self.mirrorList = mirrorList
        self.rayInDict, self.rayReflectedDict = self.setRays4Plot(path, mirrorDataSheet)


    def setRays4Plot(self, path, mirrorDataSheet):

        #print(mirrorDataSheet)

        xRayInData = []
        yRayInData = []
        zRayInData = []

        xRayReflectedData = []
        yRayReflectedData = []
        zRayReflectedData = []

        xRayNormalData = []
        yRayNormalData = []
        zRayNormalData = []
        #Construct List of pairs of Rays



        rayInDict = dict(x=xRayInData, y=yRayInData, z=zRayInData)
        rayReflectedDict = dict(x=xRayReflectedData, y=yRayReflectedData, z=zRayReflectedData)


        return rayInDict, rayReflectedDict