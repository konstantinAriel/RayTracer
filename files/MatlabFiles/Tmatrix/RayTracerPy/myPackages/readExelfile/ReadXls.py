import pandas as pd
import numpy as np

class ReadXls:
    def __init__(self, path):
        self.path = path

    def readXlsFile(self, path):
        paramFile = pd.ExcelFile(path)
        sheets = paramFile.sheet_names
        print('sheets:', sheets)
        Mnumber = len(sheets) - 3
        return paramFile

    def getLineParam(self, paramDataFile):
        lineParam = paramDataFile.parse(sheetname='LineParam')
        return lineParam

    def getSysPAram(self, paramDataFile):
        sysParam = paramDataFile.parse(sheetname='SysParam')
        return sysParam

    def getRaysIn(self, paramDataFile):
        raysIn = paramDataFile.parse(sheetname='RaysIn')
        return raysIn

    def getDataSheet(self,paramDatafile, sheetname):
        return paramDatafile.parse(sheetname=sheetname)
