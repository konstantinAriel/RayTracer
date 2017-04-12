import pandas as pd
import numpy as np

class Parametrs:
    def __init__(self, paramName, path):
        self.path = path
        self.paramName = paramName
        self.paramFile = pd.ExcelFile(self.path)
        self.sheetsNames = self.paramFile.sheet_names
        self.mNumber = len(self.sheetsNames) - 3
        self.paramTable = self.getParam(self.paramFile, self.paramName)

    def getParam(self,paramDataFile, paramName):
        self.paramTable = paramDataFile.parse(sheetname=paramName)
        return self.paramTable

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
