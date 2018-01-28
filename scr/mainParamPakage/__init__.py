import pandas as pd
import  numpy as np


global mainPath, xlsDir, fExtend, rInDir, rOutDir, systemSettingsDir, sysParamFilename, raysInFname, raysNormalisedFname, ray4TestMatrix3PointFname

mainPath = "/home/konstantin/rt/RayTracer/files/"
xlsDir  =  'XLS/'
fExtend = '.xls'
rInDir = 'Rin/'
rOutDir = 'Rout/'
systemSettingsDir = 'systemSetting/'
rNormalDir = 'Rnormal/'
rReflectedDir = 'Rreflected/'

sysParamFilename = 'sysParam'
raysInFname = 'RaysIn'
raysNormalisedFname = 'Rin_0_1'
ray4TestMatrix3PointFname = 'ray4TestMatrix3Points'

class Parametrs:

    def __init__(self, path, sheetName):
        self.path = path
        self.sheetName = sheetName
        self.xlsFile = self.getXlsFile(self.path)
        self.DataSheet = self.getDataSheet(self.xlsFile, self.sheetName)
        self.sheetsNames = self.xlsFile.sheet_names

    def getXlsFile(self, path):
        return  pd.ExcelFile(path)

    def getDataSheet(self, xlsFile, sheetname):
        return xlsFile.parse(sheetname=sheetname)

    def getmirrorNumber (self, sheetNames):
        return len(sheetNames) - 3

    def getMirrorList(self, sysParamDF):
        count = 0
        mirrorList = []
        for i in sysParamDF.Rin:
            if np.isnan(i):
                break
            else:
                for j in range(int(sysParamDF.Rin[count]), int(sysParamDF.Rout[count]) + 1):
                    mirrori = 'Mirror' + str(j)
                    mirrorList.append(mirrori)
                count += 1
        return mirrorList



