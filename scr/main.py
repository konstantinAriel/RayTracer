import  numpy as np
import pandas as pd
from myPackages.readExelfile.ReadXls import ReadXls
from scr.Rays import Rays
from scr.MainParam import Parametrs

#path = "/home/kosta/RayTracer/RayTracer/files/settingsfiles/testSheets4py.xls"
mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
sysParamFname = 'sysParam_1.xls'
RaysInFname = 'RaysIn.xls'
RaysNormalisedFname = mainPath + 'RaysNormalised_' + sysParamFname
tLine = Parametrs("LineParam", mainPath+sysParamFname)
sys = Parametrs("SysParam", mainPath+sysParamFname)

#=============  Normilise Rin for Mirror  ===========================
Rin = Parametrs("Rin", mainPath+RaysInFname)
#print(Rin.paramTable)

rInObject = Rays()
RaysNameIn = 'inRay_' + str(int(sys.paramTable.Rin[0])) + '_' + str(int(sys.paramTable.Rin[0]+1))
RaysInDF = rInObject.saveExecelRin(Rin.paramTable, RaysNormalisedFname,RaysNameIn)

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
        #print("Current Mirror = ", mirrorList)

        Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
        a11 = 1/(4*Mirror.Focus[0])
        a22 = 1/(4*Mirror.Focus[1])
        a3 = 1

        ################################################################
        #print('=============',RaysInDF)

        rInObject.calcReflectedRays(Mirror, RaysInDF)

        RaysNameIn = 'inRay_' + (str(countMirror - 1)) + '_' + str(countMirror)
        RaysNameOut = 'refRay_' + str(countMirror) + '_' + str(countMirror + 1)
        RaysNormal2Surf = 'normalRay_' + str(countMirror) + '_' + str(countMirror)


    print("Count = ",countMirror)
    countMirror += 1


