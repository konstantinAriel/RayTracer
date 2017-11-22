import os
import numpy as np
from numpy import nan
import pandas as pd
import xarray as xr
import plotly.graph_objs  as go

import plotly as py

from scr.MainParam import Parametrs
from scr.Ploting import PlotingRayTracing
from scr.Rays import Rays
from scr.getRaysFromMatrix import RaysFromMatrix


def pathName():
    global mainPath, fExtend, sysParamFname, raysInFname, ray4test3pointFname, mainPathForMatrix, mainPathToCompare
    mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
    fExtend = '.xls'
    sysParamFname = 'sysParam_1'
    raysInFname = 'RaysIn'
    raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname + '_' + sysParamFname
    ray4test3pointFname = mainPath + 'ray4test3Point_'  + sysParamFname + fExtend
    mainPathForMatrix = '/home/konstantin/PycharmProjects/RayTracer/result/'
    mainPathToCompare = '/home/konstantin/PycharmProjects/RayTracer/result/toCompare/'

def mirrorLoop(mirrorDictMain):
    for mirrorDictSub in mirrorDictMain.keys():
        #print(sys.dataSheet.Rin[0])
        countMirror = int(sys.dataSheet.Rin[0])
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',  mirrorList)
            print("Count = ", countMirror)
            # print("Current Mirror = ", mirrorList)

            Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
            # print('Mirror = ')
            # print(Mirror)
            ################################################################

            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                             'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                             'normalRay_' + str(countMirror) + '_' + str(countMirror)]

            RaysObject = Parametrs(mainPathToCompare + raysFName[0] + fExtend, 'Sheet1')
            path = [mainPathToCompare, raysFName, fExtend]
            # print(RaysObject.dataSheet)
            # print('path = ', path )
            rInObject.calcReflectedRays(path, Mirror, RaysObject.dataSheet)
            countMirror += 1
    # print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++   END      Mirror Loop         ',  mirrorList)

def plotLoop(mirrorDictMain):
    data = []
    for mirrorDictSub in mirrorDictMain.keys():
        # print('sysObject in plotLoop = ')
        # print(sysObject.dataSheet)
        countMirror = int(sysObject.dataSheet.Rin[0])
        # print('CountMirror', countMirror)
        # print('****************************************************************** Mirror Loop',countMirror)
        # print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',countMirror)
        data = []
        layout = []
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            # print("Count = ", countMirror)
            # print("Current Mirror = ", mirrorList)
            mirrorObject = Parametrs(mainPath + sysParamFname + fExtend, mirrorList)  ## mirror List - The name of Sheets in Exel file
            # print('Mirror = ')
            # print(mirrorObject.dataSheet)
            ################################################################
            # print('=============',RaysInDF)
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            path = [mainPathToCompare, raysFName, fExtend]
            # print('path = ', path )
            plotObject = PlotingRayTracing(path, mirrorObject.dataSheet, mirrorList)

            surfR = plotObject.setMirrorSurf

            #print('plotObject.data = ',plotObject.data)
            data.append(plotObject.rayInDict)
            data.append(plotObject.rayReflectedDict)
            data.append(surfR)

            # print('===========================================================================  End Mirror Loop')
            countMirror += 1
        data.append(plotObject.Tline1)
        data.append(plotObject.Tline2)
        layout = plotObject.layout
    #print(data)
    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, filename='/home/konstantin/PycharmProjects/RayTracer/result/htmlFiles/rayToCompare.html')

pathName()
rInObject = Rays()
tLine = Parametrs(mainPath+sysParamFname + fExtend, "LineParam")
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
# print('sys.dataSheet = ')
# print(sys.dataSheet)
mirror1SheetName = 'Mirror' + str(int(sys.dataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath+sysParamFname + fExtend, 'Mirror1')

mainRin = Parametrs(mainPath + raysInFname + fExtend, "Xin")
raysDataFrame = rInObject.rInNormalise(mirrorObject.dataSheet, mainRin.dataSheet)
rInObject.saveRays2Execel(mainPathToCompare + 'Ray'+'_' +
                           str(int(sys.dataSheet.Rin[0]-1)) + '_' +
                           str(int(sys.dataSheet.Rin[0]))
                           + fExtend,
                           raysDataFrame)
mirrorDictMain = sys.getMirrorList(sys.dataSheet)

mirrorLoop(mirrorDictMain)

sysObject = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
py.tools.set_credentials_file(username ='DemoAccount', api_key='lr1c37zw81')

plotLoop(mirrorDictMain)

for i in range(1,2):

    path2testMatrix = mainPathForMatrix + 'testMatrix_0_' + str(i) + fExtend
    # print('i = ')
    # print(i)
    # print('path2testMatrix = ')
    # print(path2testMatrix)
    matrixtestObject = Parametrs(path=path2testMatrix, sheetName='Sheet1')
    matrixtestDF = matrixtestObject.dataSheet
    # print('matrixtestDF = ')
    # print(matrixtestDF)

    raysFName = ['Ray_' + (str(i - 1)) + '_' + str(i),
                 'Ray_' + str(i) + '_' + str(i + 1),
                 'normalRay_' + str(i) + '_' + str(i)]
    path = [mainPathToCompare, raysFName, fExtend]
    RaysObject = Parametrs(mainPathToCompare + raysFName[0] + fExtend, 'Sheet1')
    RaysInSheetNameList = mainRin.sheetsNames
    print(' RaysInShetNameList = ')
    print(RaysInSheetNameList)
    for rayInSheetName in RaysInSheetNameList:
        print('rayInSheetName = ')
        print(rayInSheetName)
        RaysDF = RaysObject.dataSheet
        countOfRays = RaysDF.index
        for indexRays in countOfRays:
            # print('indexRays = ')
            # print(indexRays)
            rOutIndexList = matrixtestDF.index
            pathToRin = '/home/konstantin/PycharmProjects/RayTracer/result/toCompare/Ray_0_1.xls'
            rOutObject = RaysFromMatrix(pathToRin, matrixtestDF, rOutIndexList)
            Rout1 = rOutObject.getFirsOderRay(indexRays)
            Rout2 = rOutObject.getSecondOderRay(indexRays)
            Rout3 = rOutObject.getThirdOderRay(indexRays)
            # RoutTotal = Rout1 + Rout2 + Rout3
            # print('Rout1 =')
            # print(Rout1)
            # print('Rout2 =')
            # print(Rout2)
            # print('Rout3 =')
            # print(Rout3)
            RoutTotalX  = Rout1[0] + Rout2[0] + Rout3[0]
            RoutTotalKx = Rout1[1] + Rout2[1] + Rout3[1]
            RoutTotalZ  = Rout1[2] + Rout2[2] + Rout3[2]
            RoutTotalKz = Rout1[3] + Rout2[3] + Rout3[3]
            # print('RoutTotal =')
            # print(RoutTotal)
            # print('RoutTotal = ')
            # print(RoutTotal)
            # print('RoutTotal X = ')
            # print(RoutTotalX)
            # print('RoutTotal  Kx = ')
            # print(RoutTotalKx)
            # print('RoutTotal  Z = ')
            # print(RoutTotalZ)
            # print('RoutTotal  Kz = ')
            # print(RoutTotalKz)
    print('********************^^^^^^^^^^^^^^^^^^^^^^   END LOOP ^^^^^^^^^^^^^^^ ********************')

