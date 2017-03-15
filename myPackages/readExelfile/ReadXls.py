import pandas as pd
import numpy as np




class ReadXls:
    def __init__(self, path):
        self.path = path

    def readXlsFile(self, path):
        paramFile = pd.ExcelFile(path)
        sheets = paramFile.sheet_names
        Mnumber = len(sheets) - 3
        return paramFile

    def getLineParam(self, paramDataFile):
        lineParam = paramDataFile.parse(sheetname=0)
        return lineParam

    def getSysPAram(self, paramDataFile):
        sysParam = paramDataFile.parse(sheetname=1)
        return sysParam

    def getRaysIn(self, paramDataFile):
        raysIn = paramDataFile.parse(sheetname=2)
        return raysIn

    def getMirrorParam(self,paramDatafile, sheetname):
        mirror = paramDatafile.parse(sheetname=sheetname)
        return mirror