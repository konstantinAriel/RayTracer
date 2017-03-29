import  numpy as np
from myPackages.readExelfile.ReadXls import ReadXls
from scr.Rays import Rays
from scr.MainParam import Parametrs

#path = "/home/kosta/RayTracer/RayTracer/files/settingsfiles/testSheets4py.xls"
path = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/testSheets4py.xls"

tLine = Parametrs("LineParam")
sys = Parametrs("SysParam")




mirrorDictMain = sys.getMirrorList(sys.paramTable)
#print(mirrorDictMain)
for mirrorDictSub in mirrorDictMain.keys():
    #print(mirrorDictSub)
    countMirror = 0
    for mirrorList in mirrorDictMain.get(mirrorDictSub):
        mirror = Parametrs(mirrorList)
        print(mirrorList)
        RaysNameIn = 'Rays' + str(countMirror)
        RaysNameOut = 'Rays' + str(countMirror+1)
        Rin = Parametrs(RaysNameIn)
        RaysHeads = Rin.paramTable.columns
        for RinIndex in Rin.paramTable.index:
            KinArray = np.array([Rin.paramTable.KxIn[RinIndex],
                                 Rin.paramTable.KyIn[RinIndex],
                                 Rin.paramTable.KzIn[RinIndex]])

            XinArray = np.array([Rin.paramTable.Xin[RinIndex],
                                 Rin.paramTable.Yin[RinIndex],
                                 Rin.paramTable.Zin[RinIndex]])
            Kin = Rays(KinArray)
            KinNormal = Kin.calcRInNormal(KinArray)
            
            print(KinArray)
            print(KinNormal)

            print(XinArray)
            

            print('=========================')
        countMirror += 1
