import  numpy as np
import pandas as pd
from myPackages.readExelfile.ReadXls import ReadXls
from scr.Rays import Rays
from scr.MainParam import Parametrs

#path = "/home/kosta/RayTracer/RayTracer/files/settingsfiles/testSheets4py.xls"
mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
sysParamFname = 'sysParam_1.xls'
RaysInFname = 'RaysIn.xls'
RaysNormalisedFNname = 'RaysNormalised_' + sysParamFname
tLine = Parametrs("LineParam", mainPath+sysParamFname)
sys = Parametrs("SysParam", mainPath+sysParamFname)
Rin = Parametrs("Rin", mainPath+RaysInFname)


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
     print(mirrorDictSub)
     countMirror = 0
     for mirrorList in mirrorDictMain.get(mirrorDictSub):
        Mirror = sys.getParam(sys.paramFile, mirrorList)
        print("Current Mirror = ", mirrorList)
        print(Mirror)
            #         RaysNameIn = 'Rays' + str(countMirror)
            #         RaysNameOut = 'Rays' + str(countMirror+1)
            #         Rin = Parametrs(RaysNameIn)
            #         RaysHeads = Rin.paramTable.columns
            #         RayCount = 0
            #         numberOfRays = len(Rin.paramTable.KxIn)
            #         KinNormalArray = np.zeros( (numberOfRays,3) )
            #         print(KinNormalArray)
            #         for RinIndex in Rin.paramTable.index:
            #             KinArray = np.array([Rin.paramTable.KxIn[RinIndex],
            #                                  Rin.paramTable.KyIn[RinIndex],
            #                                  Rin.paramTable.KzIn[RinIndex]])
            #
            #             XinArray = np.array([Rin.paramTable.Xin[RinIndex],
            #                                  Rin.paramTable.Yin[RinIndex],
            #                                  Rin.paramTable.Zin[RinIndex]])
            #             Kin = Rays(KinArray)
            #             KinNormal = Kin.calcRInNormal(KinArray)
            #             KinNormalArray[RinIndex,:] = KinNormal
            #             print(KinNormalArray)
            #             # print(KinArray)
            #             # print(KinNormal)
            #             # print(XinArray)
            #             RayCount += 1
            #             print('=========================')
            #         kInDF = pd.DataFrame(KinNormalArray, columns=['KxIN', 'KyIn', 'KzIn'])
            #         kInDF.to_excel(path1, sheet_name='Sheet2')
            #         print('KinDF = ')
            #         print(kInDF)
            #         countMirror += 1
