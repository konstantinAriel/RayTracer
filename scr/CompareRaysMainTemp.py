import os
import numpy as np
from numpy import nan
import pandas as pd
import xarray as xr
import plotly.graph_objs  as go

import plotly as pl

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
            # print(' RaysInShetNameList = ')
            # print(RaysInSheetNameList)
            data2 = []
            for rayType in typeOfRays:
                # if rayType == 'Xin':
                    rIn1, rIn2, rIn3 = getRayIntype(rayType)
                    print('rayType =                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                    print(rayType)
                    # xRayInDataX =  []
                    # xRayInDataKx = []
                    # xRayInDataZ =  []
                    # xRayInDataKz = []

                    xRayInData =      []
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
                    yRayTotalKzMOutData = []

                    yRayTotalXRTOutData =  [] #
                    yRayTotalKxRTOutData = [] #
                    yRayTotalZRTOutData =  [] #
                    yRayTotalKzRTOutData = [] #

                    raysFName = [rayType + '_' + (str(countMirror - 1)) + '_' + str(countMirror),
                                             rayType + '_' + str(countMirror) + '_' + str(countMirror + 1),
                                 'normal' + rayType + str(countMirror) + '_' + str(countMirror)]
                    # print('raysFName = ')
                    # print(raysFName)

                    path = [mainPathToCompare + mirrorList + '/', raysFName, fExtend]

                    if  mirrorList == 'Mirror1':
                        RaysInObject = Parametrs(mainPath + raysInFname + fExtend, rayType)  # For first mirror
                        RaysInDF = RaysInObject.dataSheet
                    else:
                        RaysInObject = Parametrs(mainPathToCompare + 'Mirror' + str(countMirror -1) + '/' + raysFName[0] + fExtend, 'Sheet1')  # For 2-4 mirror
                        RaysInDF = RaysInObject.dataSheet

                    rayObject.calcReflectedRays(path, Mirror, RaysInDF)
                    # print('rayType = ')
                    # print(rayType)

                    pathToRin = mainPathToCompare  + rayType + '_0_1' + fExtend
                    RaysOutObjectFromRayTraycer = Parametrs(mainPathToCompare + mirrorList + '/' + raysFName[1] + fExtend,
                                                            'Sheet1')  # For each mirror
                    RayFromRTDF = RaysOutObjectFromRayTraycer.dataSheet
                    # print('RyaFromRTDF = ')
                    # print(RayFromRTDF)

                    RaysInObjectForPlot = Parametrs(mainPath + raysInFname + fExtend, rayType)  # For first mirror
                    RaysInDForPlot = RaysInObjectForPlot.dataSheet

                    rIn2value = RaysInDForPlot.loc[0, rIn2]
                    rIn3value = RaysInDForPlot.loc[0, rIn3]

                    for indexRays in RaysInDF.index:
                        # print('indexRays = ')
                        # print(indexRays)

                        xRayInData.append(RaysInDForPlot.loc[indexRays, rIn1])

                        # xRayInDataKx.append(RaysInDF.Kxin[indexRays])
                        # xRayInDataZ.append(RaysInDF.Zin[indexRays])
                        # xRayInDataKz.append(RaysInDF.Kzin[indexRays])

                        if countMirror == 1:
                            rOutList = ['Xin', 'Kxin', 'Yin', 'Kyin']
                        elif countMirror == 2:
                            rOutList = ['Xin', 'Kxin', 'Zin', 'Kzin']
                        elif countMirror == 3:
                            rOutList = ['Yin', 'Kyin', 'Zin', 'Kzin']
                        elif countMirror == 4:
                            rOutList = ['Xin', 'Kxin', 'Yin', 'Kyin']

                        yRayTotalXRTOutData. append(RayFromRTDF.loc[indexRays,  rOutList[0]])
                        yRayTotalKxRTOutData.append(RayFromRTDF.loc[indexRays,  rOutList[1]])
                        yRayTotalZRTOutData. append(RayFromRTDF.loc[indexRays,  rOutList[2]])
                        yRayTotalKzRTOutData.append(RayFromRTDF.loc[indexRays,  rOutList[3]])

                        # rOutIndexList = matrixtestDF.index

                        rOutFromMatrixObject = RaysFromMatrix(pathToRin, matrixtestDF)

                        Rout1 = rOutFromMatrixObject.getFirsOderRay(indexRays)

                        # print('Rout1 = ')
                        # print(Rout1[:,0])

                        yRay1MXOutData. append(Rout1[0, 0])
                        yRay1MKxOutData.append(Rout1[1, 0])
                        yRay1MZOutData. append(Rout1[2, 0])
                        yRay1MKzOutData.append(Rout1[3, 0])

                        Rout2 = rOutFromMatrixObject.getSecondOderRay(indexRays, rIn1)

                        yRay2MXOutData .append(Rout2[0,0])
                        yRay2MKxOutData.append(Rout2[1,0])
                        yRay2MZOutData .append(Rout2[2,0])
                        yRay2MKzOutData.append(Rout2[3,0])

                        Rout3 = rOutFromMatrixObject.getThirdOderRay(indexRays, rIn1, rIn2)

                        yRay3MXOutData .append(Rout3[0,0])
                        yRay3MKxOutData.append(Rout3[1,0])
                        yRay3MZOutData .append(Rout3[2,0])
                        yRay3MKzOutData.append(Rout3[3,0])

                        # RoutTotal = Rout1 + Rout2 + Rout3
                        # print('Rout1 =')
                        # print(Rout1)
                        # print('Rout2 =')
                        # print(Rout2)
                        # print('Rout3 =')
                        # print(Rout3)

                        RoutTotalX  = Rout1[0,0] + Rout2[0,0] + Rout3[0,0]
                        RoutTotalKx = Rout1[1,0] + Rout2[1,0] + Rout3[1,0]
                        RoutTotalZ  = Rout1[2,0] + Rout2[2,0] + Rout3[2,0]
                        RoutTotalKz = Rout1[3,0] + Rout2[3,0] + Rout3[3,0]

                        yRayTotalXMOutData .append(RoutTotalX)
                        yRayTotalKxMOutData.append(RoutTotalKx)
                        yRayTotalZMOutData .append(RoutTotalZ)
                        yRayTotalKzMOutData.append(RoutTotalKz)

                        # print('RoutTotal =')
                        # print(RoutTotal)
                        # print('RoutTotal X = ')
                        # print(RoutTotalX)
                        # print('RoutTotal  Kx = ')
                        # print(RoutTotalKx)
                        # print('RoutTotal  Z = ')
                        # print(RoutTotalZ)
                        # print('RoutTotal  Kz = ')
                        # print(RoutTotalKz)

                    trace111 =  go.Scatter(x=xRayInData, y=yRay1MXOutData,       xaxis='x1',   yaxis='y1',  mode = 'lines',  name = rIn2 + str(rIn2value) +  '_' + rIn3 + str(rIn3value) +'X_M1')      # Xin - XoutM1
                    trace112 =  go.Scatter(x=xRayInData, y=yRay2MXOutData,       xaxis='x1',   yaxis='y1',  mode = 'lines',  name = 'X_M2')      # Xin - XoutM2
                    trace113 =  go.Scatter(x=xRayInData, y=yRay3MXOutData,       xaxis='x1',   yaxis='y1',  mode = 'lines',  name = 'X_M3')      # Xin - XoutM3

                    trace121 =  go.Scatter(x=xRayInData, y=yRay1MKxOutData,      xaxis='x2',   yaxis='y2',  mode = 'lines',  name = 'Kx_M1')     # Xin - KxOutM1
                    trace122 =  go.Scatter(x=xRayInData, y=yRay2MKxOutData,      xaxis='x2',   yaxis='y2',  mode = 'lines',  name = 'Kx_M2')     # Xin - KxOutM2
                    trace123 =  go.Scatter(x=xRayInData, y=yRay3MKxOutData,      xaxis='x2',   yaxis='y2',  mode = 'lines',  name = 'Kx_M3')     # Xin - KxOutM3

                    trace131 = go.Scatter(x=xRayInData,  y=yRay1MZOutData,       xaxis='x3',   yaxis='y3',  mode = 'lines',  name = 'Z_M1')      # Xin - ZOutM1
                    trace132 = go.Scatter(x=xRayInData,  y=yRay2MZOutData,       xaxis='x3',   yaxis='y3',  mode = 'lines',  name = 'Z_M2')      # Xin - ZOutM2
                    trace133 = go.Scatter(x=xRayInData,  y=yRay3MZOutData,       xaxis='x3',   yaxis='y3',  mode = 'lines',  name = 'Z_M3')      # Xin - ZOutM3

                    trace141 = go.Scatter(x=xRayInData,  y=yRay1MKzOutData,      xaxis='x4',   yaxis='y4',  mode = 'lines',  name = 'KZ_M1')    # Xin - KZOutM1
                    trace142 = go.Scatter(x=xRayInData,  y=yRay2MKzOutData,      xaxis='x4',   yaxis='y4',  mode = 'lines',  name = 'KZ_M2')    # Xin - KZOutM2
                    trace143 = go.Scatter(x=xRayInData,  y=yRay3MKzOutData,      xaxis='x4',   yaxis='y4',  mode = 'lines',  name = 'KZ_M3')    # Xin - KZOutM3

                    trace211 = go.Scatter(x=xRayInData,  y=yRayTotalXMOutData,   xaxis='x5',   yaxis='y5',  mode = 'lines',  name = 'Total_X_M ')
                    trace212 = go.Scatter(x=xRayInData,  y=yRayTotalXRTOutData,  xaxis='x5',   yaxis='y5',  mode = 'lines',  name = 'Total_X_RT')

                    trace221 = go.Scatter(x=xRayInData,  y=yRayTotalKxMOutData,  xaxis='x6',   yaxis='y6',  mode = 'lines',  name = 'Total_Kx_M')
                    trace222 = go.Scatter(x=xRayInData,  y=yRayTotalKxRTOutData, xaxis='x6',   yaxis='y6',  mode = 'lines',  name = 'Total_Kx_RT')

                    trace231 = go.Scatter(x=xRayInData,  y=yRayTotalZMOutData,   xaxis='x7',   yaxis='y7',  mode = 'lines',  name = 'Total_Z_M')
                    trace232 = go.Scatter(x=xRayInData,  y=yRayTotalZRTOutData,  xaxis='x7',   yaxis='y7',  mode = 'lines',  name = 'Total_Z_RT')

                    trace241 = go.Scatter(x=xRayInData,  y=yRayTotalKzMOutData,  xaxis='x8',   yaxis='y8',  mode = 'lines',  name = 'Total_Kz_M')
                    trace242 = go.Scatter(x=xRayInData,  y=yRayTotalKzRTOutData, xaxis='x8',   yaxis='y8',  mode = 'lines',  name = 'Total_Kz_RT')


                    data1 = [trace111, trace112, trace113,
                            trace121, trace122, trace123,
                            trace131, trace132, trace133,
                            trace141, trace142, trace143,
                            trace211, trace212,
                            trace221, trace222,
                            trace231, trace232,
                            trace241, trace242]
                    # data = [trace111, trace112, trace113]

                    # data11 = [trace111, trace112, trace113]
                    # data12 = [trace121, trace122, trace123]
                    # data13 = [trace131, trace132, trace133]
                    # data14 = [trace141, trace142, trace143]
                    #
                    # data21 = [trace211, trace212]
                    # data22 = [trace221, trace222]
                    # data23 = [trace231, trace232]
                    # data24 = [trace241, trace242]

                    # fig = pl.tools.make_subplots(rows=2, cols=4)
                    #
                    # fig.append_trace(data11, 1, 1)
                    # fig.append_trace(data12, 1, 2)
                    # fig.append_trace(data13, 1, 3)
                    # fig.append_trace(data14, 1, 4)
                    #
                    # fig.append_trace(data21, 2, 1)
                    # fig.append_trace(data22, 2, 2)
                    # fig.append_trace(data23, 2, 3)
                    # fig.append_trace(data24, 2, 4)

                    layout1 = setLayout()

                    fig1 = go.Figure(data=data1, layout=layout1)
                    pl.offline.plot(fig1, filename='/home/konstantin/PycharmProjects/RayTracer/result/htmlFiles/' + mirrorList + '_' + rayType + '.html' )

            countMirror+=1
            print('********************^^^^^^^^^^^^^^^^^^^^^^  END LOOP  ^^^^^^^^^^^^^^^ ********************')

def getRayIntype(rayType):
    rIn2 = 'Zin'
    rIn3 = 'Zin'
    if rayType == 'Xin':
        rIn1 = 'Xin'
        # print('Xin')
    elif rayType == 'Kxin':
        rIn1 = 'Kxin'
        # print('Kxin')
    elif rayType == 'Zin':
        rIn1 = 'Zin'
        # print('Zin')
    elif rayType == 'Kzin':
        rIn1 = 'Kzin'
        # print('Kzin')
    elif rayType == 'Xin_Kxin':
        rIn1 = 'Xin'
        rIn2 = 'Kxin'
        # print('Xin_Kxin')
    elif rayType == 'Xin_Zin':
        rIn1 = 'Xin'
        rIn2 = 'Zin'
        # print('Xin_Zin')
    elif rayType == 'Xin_Kzin':
        rIn1 = 'Xin'
        rIn2 = 'Kzin'
        # print('Xin_Kzin')
    elif rayType == 'Kxin_Zin':
        rIn1 = 'Kxin'
        rIn2 = 'Zin'
        # print('Kxin_Zin')
    elif rayType == 'Kxin_Kzin':
        rIn1 = 'Kxin'
        rin2 = 'Kzin'
        # print('Kxin_Kzin')
    elif rayType == 'Zin_Kzin':
        rIn1 = 'Zin'
        rIn2 = 'Kzin'
        # print('Zin_Kzin')
    elif rayType == 'Xin_Kxin_Zin':
        rIn1 = 'Xin'
        rIn2 = 'Kxin'
        rIn3 = 'Zin'
        # print('Xin_Kxin_Zin')
    elif rayType == 'Xin_Kxin_Kzin':
        rIn1 = 'Xin'
        rIn2 = 'Kxin'
        rIn3 = 'Kzin'
        # print ('Xin_Kxin_Kzin')
    elif rayType == 'Xin_Zin_Kzin':
        rIn1 = 'Xin'
        rIn2 = 'Zin'
        rIn3 = 'Kzin'
        # print('Xin_Zin_Kzin')
    elif rayType == 'Kxin_Zin_Kzin':
        rIn1 = 'Kxin'
        rIn2 = 'Zin'
        rIn3 = 'Kzin'
        # print('Kxin_Zin_Kzin')
    return rIn1, rIn2, rIn3

def setLayout():
    layout = go.Layout(
        xaxis1=dict(
            domain=[0, 0.2],
            anchor='y1'
        ),
        yaxis1=dict(
            domain=[0.5, 1],
            anchor='x1'
        ),
        xaxis2=dict(
            domain=[0.25, 0.45],
            anchor='y2'
        ),
        yaxis2=dict(
            domain=[0.5, 1],
            anchor='x2'
        ),
        xaxis3=dict(
            domain=[0.5, 0.70],
            anchor='y3'
        ),
        yaxis3=dict(
            domain=[0.5, 1],
            anchor='x3'
        ),
        xaxis4=dict(
            domain=[0.75, 1],
            anchor='y4'
        ),
        yaxis4=dict(
            domain=[0.5, 1],
            anchor='x4'
        ),
        xaxis5=dict(
            domain=[0, 0.2],
            anchor='y5'
        ),
        yaxis5=dict(
            domain=[0, 0.45],
            anchor='x5'
        ),
        xaxis6=dict(
            domain=[0.25, 0.45],
            anchor='y6'
        ),
        yaxis6=dict(
            domain=[0, 0.45],
            anchor='x6'
        ),
        xaxis7=dict(
            domain=[0.5, 0.7],
            anchor='y7'
        ),
        yaxis7=dict(
            domain=[0, 0.45],
            anchor='x7'
        ),
        xaxis8=dict(
            domain=[0.75, 1],
            anchor='y8'
        ),
        yaxis8=dict(
            domain=[0, 0.45],
            anchor='x8'
        ),
    )
    return layout

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
    pl.offline.plot(fig, filename='/home/konstantin/PycharmProjects/RayTracer/result/htmlFiles/rayToCompare.html')

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

# sysObject = Parametrs(mainPath + sysParamFname + fExtend, "SysParam")
# py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
#
# plotLoop(mirrorDictMain)








