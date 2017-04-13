import pandas as pd
import numpy as np

class Parametrs:
    def __init__(self, sheetName, path):
        self.path = path
        self.sheetName = sheetName
        self.paramFile = pd.ExcelFile(self.path)
        self.sheetsNames = self.paramFile.sheet_names
        self.mNumber = len(self.sheetsNames) - 3
        self.dataSheet = self.getParam(self.paramFile, self.sheetName)

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
