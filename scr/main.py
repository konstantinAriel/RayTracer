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

#  Read  Excel file with Rays Data in
tLine = Parametrs("LineParam", mainPath+sysParamFname + fExtend)
sys = Parametrs("SysParam", mainPath+sysParamFname + fExtend)
Rin = Parametrs("Rin", mainPath + raysInFname + fExtend)
raysSheetName = 'Ray_' + str(int(sys.dataSheet.Rin[0] - 1)) + '_' + str(int(sys.dataSheet.Rin[0]))

rInObject = Rays()  # Create object of Rays

#=============  Normilise Rin for Mirror  ===========================
mirror1SheetName = 'Mirror' + str(int(sys.dataSheet.Rin[0]))
mirrorObject = Parametrs('Mirror1', mainPath+sysParamFname + fExtend)

# print(Mirror1)
raysDataFrame = rInObject.rInNormalise(mirrorObject.dataSheet, Rin.dataSheet)
# seve to Excel
rInObject.saveRays2Execel(raysNormalisedFname + fExtend, raysDataFrame, raysSheetName)

def printFromExel():
    print('==============================')
    print(tLine.dataSheet)
    print('==============================')
    print(sys.dataSheet)
    print('==============================')
    print(Rin.dataSheet)
    print('==============================')

# print('sys.DataSheet',sys.dataSheet)

mirrorDictMain = sys.getMirrorList(sys.dataSheet)

# print('Rin.paramTable', Rin.paramTable)
# printFromExel()
# print(mirrorDictMain)

for mirrorDictSub in mirrorDictMain.keys():
    countMirror = int(sys.dataSheet.Rin[0])
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

        RaysNameList = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                        'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                        'normalRay_' + str(countMirror) + '_' + str(countMirror)]

        RaysObject = Parametrs(RaysNameList[0], raysNormalisedFname + fExtend)
        print(RaysObject.dataSheet)
        rInObject.calcReflectedRays(Mirror, RaysObject.dataSheet, RaysNameList)

        countMirror += 1
