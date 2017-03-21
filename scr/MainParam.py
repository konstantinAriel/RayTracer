import pandas as pd
import numpy as np

class Parametrs:
    def __index__(self,path, paramName):
        self.path = path
        self.paramName = paramName
        self.paramFile = pd.ExcelFile(self.path)
        self.sheetsNames = self.paramFile.sheet_names
        self.mNumber = len(self.sheetsNames) - 3
        self.paramObj = self.getLineParam()


    def getParam(self):
        self.setParam(self.paramFile, self.paramName)
        return self.paramObj


    def setParam(self, paramDataFile, paramName):
        self.paramObj = paramDataFile.parse(sheetname=paramName)


# def getMirrorList():
#     count = 0
#     mirrorDict = {}
#     print(mirrorDict)
#     for i in sysParam.Rin:
#             if np.isnan(i):
#               break
#             else:
#                 mirrorList = []
#                 position = 0
#                 for j in range(int(sysParam.Rin[count]), int(sysParam.Rout[count]) + 1):
#                     mirrorList.insert(position, 'mirror' + str(j))
#                     position = position + 1
#                 mirrorDict['mirrorDict'+str(count+1)] = mirrorList
#                 count = count + 1
#     return mirrorDict
