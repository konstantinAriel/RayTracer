import  numpy as np
import pandas as pd
from myPackages.readExelfile.ReadXls import ReadXls
from scr.Rays import Rays
from scr.MainParam import Parametrs

#path = "/home/kosta/RayTracer/RayTracer/files/settingsfiles/testSheets4py.xls"
mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
sysParamFname = 'sysParam_1.xls'
RaysInFname = 'RaysIn.xls'
RaysNormalisedFNname = mainPath + 'RaysNormalised_' + sysParamFname
tLine = Parametrs("LineParam", mainPath+sysParamFname)
sys = Parametrs("SysParam", mainPath+sysParamFname)

#=============  Normilise Rin for Mirror  ===========================
Rin = Parametrs("Rin", mainPath+RaysInFname)
#print(Rin.paramTable)

rInNormalized = Rays()

RaysInDF = rInNormalized.saveExecelRin(Rin.paramTable,RaysNormalisedFNname)

def printFromExel():
    print('==============================')
    print(tLine.paramTable)
    print('==============================')
    print(sys.paramTable)
    print('==============================')
    print(Rin.paramTable)
    print('==============================')


#printFromExel()

mirrorDictMain = sys.getMirrorList(sys.paramTable)
print(mirrorDictMain)
for mirrorDictSub in mirrorDictMain.keys():
    countMirror = int(sys.paramTable.Rin[0])
    #print(mirrorDictSub)
    #print(countMirror)
    for mirrorList in mirrorDictMain.get(mirrorDictSub):
        #print("Current Mirror = ", mirrorList)

        Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of SHeets in Exel file
        a11 = 1/(4*Mirror.Focus[0])
        a22 = 1/(4*Mirror.Focus[1])
        a3 = 1

        ################################################################
        #print('=============',RaysInDF)

        for RinIndex in Rin.paramTable.index:
            k1 = RaysInDF.Kxin[RinIndex]
            k2 = RaysInDF.Kyin[RinIndex]
            k3 = RaysInDF.Kzin[RinIndex]
            print(RinIndex)
            print('k1 = ', k1)
            print('k2 = ', k2)
            print('k3 = ', k3)


            RaysNameIn = 'inRay_' + (str(countMirror-1)) + '_' + str(countMirror)
            RaysNameOut = 'refRay_' + str(countMirror) + '_' + str(countMirror+1)
            RaysNormal2Surf = 'normalRay_' + str(countMirror) + '_' + str(countMirror)

            A = a11*(k1**2) + a22*(k2**2)
            B = 2*(
                (a11*k1*(X1-dx1)) + (a22*k2*(X2-dx2))
                ) - (a3*k3)
            C = (a11*((X1-dx1)**2)) + (a22*((X2 -dx2)**2)) - (a3*(X3-dx3))


    print("Count = ",countMirror)
    countMirror += 1


