import  numpy as np
from myPackages.readExelfile.ReadXls import ReadXls
from scr.MainParam import Parametrs

#path = "/home/kosta/RayTracer/RayTracer/files/settingsfiles/testSheets4py.xls"
path = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/testSheets4py.xls"

tLine = Parametrs("LineParam")
sys = Parametrs("SysParam")
Rin = Parametrs( "RaysIn")


mirrorDictMain = Rin.getMirrorList(sys.paramTable)

for mirrorDictSub in mirrorDictMain.keys():
    print(mirrorDictSub)
    for mirrorList in mirrorDictSub:
        print(mirrorList)
