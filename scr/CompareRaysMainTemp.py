import os
import numpy as np
from numpy import nan
import pandas as pd
import xarray as xr
import plotly.graph_objs  as go

import plotly as py

from scr.MainParam import Parametrs
from scr.Ploting import Ploting
from scr.Rays import Rays
from scr.getRaysFromMatrix import RaysFromMatrix

def pathName():

    global mainPath, fExtend, sysParamFname, raysInFname, ray4test3pointFname, mainPathForMatrix, mainPathToCompare
    mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
    fExtend = '.xls'
    sysParamFname = 'sysParam_1'
    raysInFname = 'RaysIn'
    raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname + '_' + sysParamFname
    ray4test3pointFname = mainPath + 'ray4test3Point_' + sysParamFname + fExtend
    mainPathForMatrix = '/home/konstantin/PycharmProjects/RayTracer/result/'
    mainPathToCompare = '/home/konstantin/PycharmProjects/RayTracer/result/toCompare/'

def mirrorLoop(mirrorDictMain):
    typeOfRays = [
                    'Xin',
                    'Kxin',
                    'Zin',
                    'Kzin',
                    'Xin_Kxin',
                    'Xin_Zin',
                    'Xin_Kzin',
                    'Kxin_Zin',
                    'Kxin_Kzin',
                    'Zin_Kzin',
                    'Xin_Kxin_Zin',
                    'Xin_Kxin_Kzin',
                    'Xin_Zin_Kzin',
                    'Kxin_Zin_Kzin'
                    ]

    for mirrorDictSub in mirrorDictMain.keys():
        # print(sys.dataSheet.Rin[0])
        countMirror = int(sys.dataSheet.Rin[0])
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            print(
                '====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',
                mirrorList)
            print("Count = ", countMirror)
            print("Current Mirror = ", mirrorList)

            Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
            path2testMatrix = mainPathForMatrix + 'testMatrix_0_' + str(countMirror) + fExtend
            matrixtestObject = Parametrs(path = path2testMatrix, sheetName = 'Sheet1')
            matrixtestDF = matrixtestObject.dataSheet

            # print(RaysObject.dataSheet)
            # print('path = ', path )

            RaysInSheetNameList = mainRin.sheetsNames
            print(' RaysInShetNameList = ')
            print(RaysInSheetNameList)
            for rayType in typeOfRays:
                xRayInData = []
                yRay1MXOutData  = []
                yRay1MKxOutData = []
                yRay1MZOutData  = []
                yRay1MKzOutData = []

                yRay2MXOutData  = []
                yRay2MKxOutData = []
                yRay2MZOutData  = []
                yRay2MKzOutData = []

                yRay3MXOutData  = []
                yRay3MKxOutData = []
                yRay3MZOutData  = []
                yRay3MKzOutData = []


                yRayTotalXMOutData  = []
                yRayTotalKxMOutData = []
                yRayTotalZMOutData  = []
                yRayTotalKzOutData  = []

                yRayTotalXRTOutData = []
                yRayTotalKxRTOutData = []
                yRayTotalZRTOutData = []
                yRayTotalKzRTOutData = []

                raysFName = [rayType + '_' + (str(countMirror - 1)) + '_' + str(countMirror),
                             rayType + '_' + str(countMirror) + '_' + str(countMirror + 1),
                             'normal' + rayType + str(countMirror) + '_' + str(countMirror)]
                print('raysFName = ')
                print(raysFName)

                path = [mainPathToCompare + mirrorList + '/', raysFName, fExtend]
                RaysInObject = Parametrs(mainPath + raysInFname + fExtend, rayType)  # For each mirror
                RaysDF = RaysInObject.dataSheet
                rayObject.calcReflectedRays(path, Mirror, RaysDF)
                print('rayType = ')
                print(rayType)

                pathToRin = mainPathToCompare  + rayType + '_0_1' + fExtend
                RaysOutObjectFromRayTraycer = Parametrs(mainPathToCompare + mirrorList + '/' + raysFName[1] + fExtend,
                                                        'Sheet1')  # For each mirror
                RayFromRTDF = RaysOutObjectFromRayTraycer.dataSheet
                print('RyaFromRTDF = ')
                print(RayFromRTDF)

                for indexRays in RaysDF.index:
                    print('indexRays = ')
                    print(indexRays)
                    rOutIndexList = matrixtestDF.index

                    rOutFromMatrixObject = RaysFromMatrix(pathToRin, matrixtestDF, rOutIndexList)

                    Rout1 = rOutFromMatrixObject.getFirsOderRay(indexRays)
                    Rout2 = rOutFromMatrixObject.getSecondOderRay(indexRays)
                    Rout3 = rOutFromMatrixObject.getThirdOderRay(indexRays)

                    RayFromRTDFindexX = RayFromRTDF.loc[indexRays, 'Xin']
                    RayFromRTDFindexKx = RayFromRTDF.loc[indexRays, 'Kxin']
                    RayFromRTDFindexZ = RayFromRTDF.loc[indexRays, 'Zin']
                    RayFromRTDFindexKz = RayFromRTDF.loc[indexRays, 'Kzin']

                    print('RayFromRTDFindex = ')
                    print(RayFromRTDFindex)

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
                    print('RoutTotal X = ')
                    print(RoutTotalX)
                    print('RoutTotal  Kx = ')
                    print(RoutTotalKx)
                    print('RoutTotal  Z = ')
                    print(RoutTotalZ)
                    print('RoutTotal  Kz = ')
                    print(RoutTotalKz)





        rayInDict = dict(
            go.Scatter(x=xRayInData, y=yRayInData,
                         mode='lines',
                         name='rayIn',
                         line=dict(width=1, color='blue')
                         ))


            countMirror+=1
            print('********************^^^^^^^^^^^^^^^^^^^^^^  END LOOP  ^^^^^^^^^^^^^^^ ********************')

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
            mirrorObject = Parametrs(mainPath + sysParamFname + fExtend,
                                     mirrorList)  ## mirror List - The name of Sheets in Exel file
            # print('Mirror = ')
            # print(mirrorObject.dataSheet)
            ################################################################
            # print('=============',RaysInDF)
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            path = [mainPathToCompare, raysFName, fExtend]
            # print('path = ', path )
            plotObject = Ploting(path, mirrorObject.dataSheet, mirrorList)

            surfR = plotObject.setMirrorSurf(mirrorObject.dataSheet)

            # print('plotObject.data = ',plotObject.data)
            data.append(plotObject.rayInDict)
            data.append(plotObject.rayReflectedDict)
            data.append(surfR)

            # print('===========================================================================  End Mirror Loop')
            countMirror += 1
        data.append(plotObject.Tline1)
        data.append(plotObject.Tline2)
        layout = plotObject.layout
    # print(data)
    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, filename='/home/konstantin/PycharmProjects/RayTracer/result/htmlFiles/rayToCompare.html')

pathName()
typeOfRays = [
                'Xin',
                'Kxin',
                'Zin',
                'Kzin',
                'Xin_Kxin',
                'Xin_Zin',
                'Xin_Kzin',
                'Kxin_Zin',
                'Kxin_Kzin',
                'Zin_Kzin',
                'Xin_Kxin_Zin',
                'Xin_Kxin_Kzin',
                'Xin_Zin_Kzin',
                'Kxin_Zin_Kzin'
                ]

rayObject = Rays()
tLine = Parametrs(mainPath + sysParamFname + fExtend, "LineParam")
sys = Parametrs(mainPath + sysParamFname + fExtend, "SysParam")
# print('sys.dataSheet = ')
# print(sys.dataSheet)
mirror1SheetName = 'Mirror' + str(int(sys.dataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath + sysParamFname + fExtend, 'Mirror1')
for rayType in typeOfRays:
    mainRin = Parametrs(mainPath + raysInFname + fExtend, sheetName=rayType)
    raysDataFrame = rayObject.rInNormalise(mirrorObject.dataSheet, mainRin.dataSheet)
    rayObject.saveRays2Execel(mainPathToCompare + rayType + '_' +
                          str(int(sys.dataSheet.Rin[0] - 1)) + '_' +
                          str(int(sys.dataSheet.Rin[0]))
                          + fExtend,
                          raysDataFrame)

mirrorDictMain = sys.getMirrorList(sys.dataSheet)

mirrorLoop(mirrorDictMain)

sysObject = Parametrs(mainPath + sysParamFname + fExtend, "SysParam")
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

plotLoop(mirrorDictMain)








