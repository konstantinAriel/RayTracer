import pandas as pd
import numpy as np

class Parametrs:
    def __init__(self, path, sheetName):
        if sheetName == None:
            pass
        else:
            self.sheetName = sheetName
        if path == None:
            pass
        else:
            self.path = path
        self.paramFile = pd.ExcelFile(self.path)
        self.sheetsNames = self.paramFile.sheet_names
        self.mNumber = len(self.sheetsNames) - 3
        self.dataSheet = self.getParam(self.paramFile, self.sheetName)
        self.mainPath = self.getMainPath()
        self.fExtend = self.getFextend()
        self.sysParamFname = self.getSysParamFname()
        self.raysInFname = self.getRaysInFname()
        self.raysNormalisedFname = self.getRaysNormalisedFname()
        self.ray4test3pointFname = self.getRay4test3pointFname()
        self.mainPathForMatrix = self.getmMainPathForMatrix()


    def getParam(self, paramDataFile, sheetName):
        self.dataSheet = paramDataFile.parse(sheetname=sheetName)
        return self.dataSheet

    # def setParam(self, paramDataFile, paramName):
    #     self.paramTable = paramDataFile.parse(sheetname=paramName)

    def getMirrorList(self, sysParam):
        count = 0
        mirrorDict = {}
        for i in sysParam.Rin:
            if np.isnan(i):
                break
            else:
                mirrorList = []
                position = 0
                for j in range(int(sysParam.Rin[count]), int(sysParam.Rout[count]) + 1):
                    mirrorList.insert(position, 'Mirror' + str(j))
                    position += 1
                mirrorDict['mirrorDict'+str(count+1)] = mirrorList
                count += 1
        return mirrorDict

    def getMainPath(self):
        mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
        return  mainPath

    def getFextend(self):
        fExtend = '.xls'
        return  fExtend

    def getSysParamFname(self):
        sysParamFname = 'sysParam_1'
        return sysParamFname

    def getRaysInFname(self):
        raysInFname = 'RaysIn'
        return raysInFname

    def getRaysNormalisedFname(self):
        raysNormalisedFname = self.mainPath + 'raysNormalised_' + self.raysInFname + '_' + self.sysParamFname
        return raysNormalisedFname

    def getRay4test3pointFname(self):
        ray4test3pointFname = self.mainPath + 'ray4test3Point_'  + self.sysParamFname + self.fExtend
        return  ray4test3pointFname

    def getmMainPathForMatrix(self):
        mainPathForMatrix= '/home/konstantin/PycharmProjects/RayTracer/result/raysForMatrix/'
        return mainPathForMatrix