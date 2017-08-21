import numpy as np
from numpy import nan
import pandas as pd
import xarray as xr
import plotly.graph_objs  as go

import plotly as py

from scr.Ploting import Ploting
from scr.Rays import Rays
from scr.MainParam import Parametrs
from scr.TestMatrix import TestMatrix  as tm, TestMatrix
from scr.getRaysFromMatrix import RaysFromMatrix

global mainPath, fExtend, sysParamFname, raysInFname, ray4TestMatrix3PointFname, mainPathForMatrix


def pathName():
    global mainPath, fExtend, sysParamFname, raysInFname, ray4TestMatrix3PointFname, mainPathForMatrix, raysToCompareFName
    mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
    fExtend = '.xls'
    sysParamFname = 'sysParam_1'
    raysInFname = 'RaysIn'
    raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname + '_' + sysParamFname
    ray4test3pointFname = mainPath + 'ray4test3Point_' + sysParamFname + fExtend
    raysToCompareFName = '/home/konstantin/PycharmProjects/RayTracer/result/toCompare/'
    mainPathForMatrix = '/home/konstantin/PycharmProjects/RayTracer/result/raysForMatrix/'


def mirrorLoop(mirrorDictMain):
    for mirrorDictSub in mirrorDictMain.keys():
        # print(sys.dataSheet.Rin[0])
        countMirror = int(sys.dataSheet.Rin[0])
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            print(
                '====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',
                mirrorList)
            print("Count = ", countMirror)
            # print("Current Mirror = ", mirrorList)

            Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
            # print('Mirror = ')
            # print(Mirror)

            ################################################################
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            RaysObject = Parametrs(raysToCompareFName + raysFName[0] + fExtend, 'Sheet1')
            # print(RaysObject.dataSheet)
            path = [raysToCompareFName, raysFName, fExtend]
            print('path = ', path)
            rInObject.calcReflectedRays(path, Mirror, RaysObject.dataSheet)
            countMirror += 1
            # print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++   END      Mirror Loop         ',  mirrorList)


def printFromExel():
    print('==============================')
    print(tLine.dataSheet)
    print('==============================')
    print(sys.dataSheet)
    print('==============================')
    # print(Rin.dataSheet)
    print('==============================')


def plotLoop(mirrorDictMain):
    data = []
    for mirrorDictSub in mirrorDictMain.keys():
        # print(sys.dataSheet)
        countMirror = int(sys.dataSheet.Rin[0])
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
            path = [raysToCompareFName, raysFName, fExtend]
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
    py.offline.plot(fig, filename='/home/konstantin/PycharmProjects/RayTracer/result/toCompare/RaysToCompare.html')


def testMatrixLoop(mirrorDictMain):
    data = []
    for mirrorDictSub in mirrorDictMain.keys():
        # print(sys.dataSheet)
        countMirror = int(sys.dataSheet.Rin[0])
        startMirror = int(sys.dataSheet.Rin[0]) - 1
        raysObject = Rays()
        print('***********************************+******************************* TestMatrixLOOP', countMirror)
        #### GET Ray_In in the System
        mainRinDF = mainRin.dataSheet
        # print(mainRinDF)

        rInList = ['Xin', 'Kxin', 'Zin', 'Kzin']
        # LOOP 1st ORDR
        path2testMatrix = []
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            if countMirror == 1:
                rOutList = ['Xin', 'Kxin', 'Yin', 'Kyin']
            elif countMirror == 2:
                rOutList = ['Xin', 'Kxin', 'Zin', 'Kzin']
            elif countMirror == 3:
                rOutList = ['Yin', 'Kyin', 'Zin', 'Kzin']
            elif countMirror == 4:
                rOutList = ['Xin', 'Kxin', 'Yin', 'Kyin']

            # print('rOutList = ', rOutList)
            # print('startMirror = ')
            # print(startMirror)
            # print('countMirror = ')
            # print(countMirror)

            mirrorObject = Parametrs(mainPath + sysParamFname + fExtend,
                                     mirrorList)  ## mirror List - The name of Sheets in Exel file
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            # print('Rays Name')
            # print(raysFName)
            path = [mainPathForMatrix, raysFName, fExtend]
            fName = path[1]
            pathInRay = path[0] + fName[0] + path[2]
            pathReflctedRay = path[0] + fName[1] + path[2]
            pathNormalRay = path[0] + fName[2] + path[2]
            RaysInObject = Parametrs(pathInRay, 'Sheet1')
            RaysInDF = RaysInObject.dataSheet
            RayReflectedObject = Parametrs(pathReflctedRay, 'Sheet1')
            RayReflectedDF = RayReflectedObject.dataSheet
            RaysNormalObject = Parametrs(pathNormalRay, 'Sheet1')
            # LOOP 1st ORDER
            testMatrixObject = TestMatrix(mirrorList)

            testMatrixDF, writer = testMatrixObject.setZeroDict(rOutList, startMirror, countMirror)
            # print('testMatrixDF')
            # print(testMatrixDF)

            # Calculate Matrix for X, X**2, X**3

            testMatrixObject.getFirsttStepMatrix(RayReflectedDF, countMirror, mainRinDF, rInList, rOutList, startMirror,
                                                 testMatrixDF)

            ## Calculate Matrix for X_Kx, X*Kx**2, X**2*Kx

            testMatrixObject.getSeconStepMatrix(RayReflectedDF, countMirror, mainRinDF, rInList, rOutList, startMirror,
                                                testMatrixDF)

            ## Calculate Matrix for X_Kx_Z
            testMatrixObject.getThirdStepMatrix(RayReflectedDF, countMirror, mainRinDF, rInList, rOutList, startMirror,
                                                testMatrixDF)
            # print(testMatrixObject.pathTotestMatrix)
            path2testMatrix.append(testMatrixObject.pathTotestMatrix)
            countMirror += 1
            print('***********************************************************    End  Ray Loop:    ', mirrorList)

    # print(path2testMatrix)
    print('===========================================================================  End Mirror Loop')
    return path2testMatrix


def getRout(path2testMatrix):
    for path2testMatrixElement in path2testMatrix:
        s = path2testMatrixElement[0]
        sIdWithExtension = s.rpartition("_")[2]
        sId = sIdWithExtension.rpartition(".xls")
        countMirror = sId[0]
        print('path2testMatrixElement = ')
        print(countMirror)

        if countMirror == '1':
            rOutList = ['Xin', 'Kxin', 'Yin', 'Kyin']
        elif countMirror == '2':
            rOutList = ['Xin', 'Kxin', 'Zin', 'Kzin']
        elif countMirror == '3':
            rOutList = ['Yin', 'Kyin', 'Zin', 'Kzin']
        elif countMirror == '4':
            rOutList = ['Xin', 'Kxin', 'Yin', 'Kyin']
        print('countMirror = ')
        print(countMirror)
        print(path2testMatrixElement)
        testMatrixFileObject = Parametrs(path=path2testMatrixElement[0], sheetName="Sheet1")
        testMatrixDF = testMatrixFileObject.dataSheet
        print(testMatrixDF)
        testMatrixObject = RaysFromMatrix(testMatrixDF)
        Rout1 = testMatrixObject.getFirsOderRay()
        Rout2 = testMatrixObject.getSecondOderRay()


pathName()

# ==================   Test for Aberation 1 =====================================

# *******************************  Rays Generator ******************************
testMatrixObject = TestMatrix(mirrorList=None)

rInObject = Rays()  # Create object of Rays

# Rays4Test3PointDF = testMatrixObject.RaysZeroDF
# rInObject.saveRays2Execel(ray4test3pointFname, Rays4Test3PointDF)

##########################################################  Run For Test ############################################

# =============   Read  Excel file with Rays Data in =========================
tLine = Parametrs(mainPath + sysParamFname + fExtend, "LineParam")
sys = Parametrs(mainPath + sysParamFname + fExtend, "SysParam")
# mainRin = Parametrs(mainPath +  raysInFname +  fExtend, "Rin")
mainRin = Parametrs(ray4TestMatrix3PointFname, "Sheet1")
# raysSheetName0 = 'Ray_' + str(int(sys.dataSheet.Rin[0] - 1)) + '_' + str(int(sys.dataSheet.Rin[0]))

# =============  Normilise Rin for Mirror  ===================================
mirror1SheetName = 'Mirror' + str(int(sys.dataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath + sysParamFname + fExtend, 'Mirror1')
raysDataFrame = rInObject.rInNormalise(mirrorObject.dataSheet, mainRin.dataSheet)
# # save to Excel
rInObject.saveRays2Execel(raysToCompareFName + 'Ray' + '_' +
                          str(int(sys.dataSheet.Rin[0] - 1)) + '_' +
                          str(int(sys.dataSheet.Rin[0]))
                          + fExtend,
                          raysDataFrame)

# ==============  Get List of Section for calculation ========================#
mirrorDictMain = sys.getMirrorList(sys.dataSheet)

# =============== Ray Tracing =================================================#
mirrorLoop(mirrorDictMain)

# #=============== Plotting ====================================================
sys = Parametrs(mainPath + sysParamFname + fExtend, "SysParam")
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
plotLoop(mirrorDictMain)

path2testMatrix = testMatrixLoop(mirrorDictMain)
print(path2testMatrix)

# testObject = RaysFromMatrix(path2testMatrix)

getRout(path2testMatrix)
