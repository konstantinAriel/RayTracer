import  numpy as np
import pandas as pd
from myPackages.readExelfile.ReadXls import ReadXls
from scr.Rays import Rays
from scr.MainParam import Parametrs

#path = "/home/kosta/RayTracer/RayTracer/files/settingsfiles/testSheets4py.xls"
mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
fExtend = '.xls'
sysParamFname = 'sysParam_1'
raysInFname = 'RaysIn'
raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname+'_' + sysParamFname
tLine = Parametrs("LineParam", mainPath+sysParamFname + fExtend)
sys = Parametrs("SysParam", mainPath+sysParamFname + fExtend)

#=============  Normilise Rin for Mirror  ===========================
Rin = Parametrs("Rin", mainPath + raysInFname + fExtend)
print('Rin.paramTable', Rin.paramTable)

rInObject = Rays()
RaysSheetName = 'inRay_' + str(int(sys.paramTable.Rin[0] - 1)) + '_' + str(int(sys.paramTable.Rin[0]))
raysDF = rInObject.rInNormalise(Rin.paramTable)
rInObject.saveExecelRin(raysNormalisedFname + fExtend, raysDF, RaysSheetName)

def printFromExel():
    print('==============================')
    print(tLine.paramTable)
    print('==============================')
    print(sys.paramTable)
    print('==============================')
    print(Rin.paramTable)
    print('==============================')

# printFromExel()

mirrorDictMain = sys.getMirrorList(sys.paramTable)
print(mirrorDictMain)
for mirrorDictSub in mirrorDictMain.keys():
    countMirror = int(sys.paramTable.Rin[0])
    #print(mirrorDictSub)
    #print(countMirror)
    for mirrorList in mirrorDictMain.get(mirrorDictSub):
        # print("Count = ", countMirror)
        # print("Current Mirror = ", mirrorList)

        Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
        # print('Mirror = ')
        # print(Mirror)

        ################################################################
        #print('=============',RaysInDF)

        RaysNameList = ['inRay_' + (str(countMirror - 1)) + '_' + str(countMirror),
                        'refRay_' + str(countMirror) + '_' + str(countMirror + 1),
                        'normalRay_' + str(countMirror) + '_' + str(countMirror)]

        # RaysFileObject =  ReadXls(raysNormalisedFname)
        # raysParamFile = RaysFileObject.readXlsFile(raysNormalisedFname)
        # RaysInDF = RaysFileObject.getDataSheet(raysParamFile, RaysNameList[0])
        # print(RaysInDF)
        # rInObject.calcReflectedRays(Mirror, RaysInDF, RaysNameList)

        countMirror += 1
