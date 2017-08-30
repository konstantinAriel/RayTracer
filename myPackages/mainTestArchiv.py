import numpy as np
import pandas as pd
import xarray as xr
import plotly.graph_objs  as go

import plotly as py
from numpy.linalg import inv
from numpy import nan
from scr.MainParam import Parametrs
from scr.Ploting import PlotingRayTracing
from scr.Rays import Rays
from scr.MainParam import Parametrs
from scr.TestMatrix import TestMatrix


def setZeroDict(rInList, rOutList, startMirror, countMirror):
    testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)

    tempNANarray84X4 = getNANarray()

    headerName = []
    for rInTemp1 in rInList:
        keynameA1 = 'A1' + '_' + rInTemp1
        headerName.append(keynameA1)

        for rInTemp2 in rInList:
            keynameA2 = 'A2' + rInTemp1 + '_' + rInTemp2
            headerName.append(keynameA2)
            for rInTemp3 in rInList:
                keynameA3 = 'A3' + rInTemp1 + rInTemp2 + '_' + rInTemp3
                headerName.append(keynameA3)

    testMatrixDF = pd.DataFrame(tempNANarray84X4, index=rOutList, columns=headerName)

    writer = pd.ExcelWriter('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls',
                            na_rep='nan')

    testMatrixDF.to_excel(writer, na_rep='nan', sheet_name='sheet1')
    writer.save()
    writer.close()
    # print('headerName')
    # print(headerName)
    # print('testMatrixDF')
    # print(testMatrixDF)
    # print('*************  After setZeroFunction')

    return testMatrixDF, writer


def getNANarray():
    tempNANarray21X4 = np.array(
        [[nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],

         [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],

         [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],

         [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
          nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]
         ])
    return tempNANarray21X4


def pathName():
    global mainPath, fExtend, sysParamFname, raysInFname, ray4test3pointFname
    mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
    fExtend = '.xls'
    sysParamFname = 'sysParam_1'
    raysInFname = 'RaysIn'
    raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname + '_' + sysParamFname
    ray4test3pointFname = mainPath + 'ray4test3Point_' + sysParamFname + fExtend


def mirrorLoop(mirrorDictMain):
    for mirrorDictSub in mirrorDictMain.keys():
        # print(sys.dataSheet.Rin[0])
        countMirror = int(sys.dataSheet.Rin[0])
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            # print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',  mirrorList)
            # print("Count = ", countMirror)
            # print("Current Mirror = ", mirrorList)

            Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
            # print('Mirror = ')
            # print(Mirror)

            ################################################################
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            RaysObject = Parametrs(mainPath + raysFName[0] + fExtend, 'Sheet1')
            # print(RaysObject.dataSheet)
            path = [mainPath, raysFName, fExtend]
            # print('path = ', path )
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
            path = [mainPath, raysFName, fExtend]
            # print('path = ', path )
            plotObject = PlotingRayTracing(path, mirrorObject.dataSheet, mirrorList)

            surfR = plotObject.setMirrorSurf

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
    py.offline.plot(fig, filename='42RaysforTest MAtrix.html')


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

            testMatrixDF, writer = setZeroDict(rInList, rOutList, startMirror, countMirror)

            print('testMatriDF')
            print(testMatrixDF)
            mirrorObject = Parametrs(mainPath + sysParamFname + fExtend,
                                     mirrorList)  ## mirror List - The name of Sheets in Exel file
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            # print('Rays Name')
            # print(raysFName)
            path = [mainPath, raysFName, fExtend]
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


            # Calculate Matrix for X, X**2, X**3

            for rInelement in rInList:
                keynameA1 = 'A1' + '_' + rInelement

                # print('*********************   Rin =  ********  ', rInelement,'   ******************')
                rayInArray = mainRinDF[(mainRinDF.Mode == rInelement)]
                index = min(rayInArray.index)
                indexMax = max(rayInArray.index)
                # print('rayInArray = ')
                # print(rayInArray)
                # print('indexMax', indexMax)
                # print('indexMin', indexMin)
                ## Calilus For a11 a22 a33 a44

                a11 = rayInArray.loc[index, rInelement]
                a12 = a11 ** 2
                a13 = a11 ** 3
                a21 = rayInArray.loc[index + 1, rInelement]
                a22 = a21 ** 2
                a23 = a21 ** 3
                a31 = rayInArray.loc[indexMax, rInelement]
                a32 = a31 ** 2
                a33 = a31 ** 3
                rInMatrix33 = np.array([
                    [a11, a12, a13],
                    [a21, a22, a23],
                    [a31, a32, a33]
                ])
                keynameA2 = 'A2' + rInelement + '_' + rInelement
                keynameA3 = 'A3' + rInelement + rInelement + '_' + rInelement

                for rayOutElement in rOutList:
                    rOutArray = RayReflectedDF.loc[index:indexMax, rayOutElement]
                    rOutColumn31 = np.array([[rOutArray[index]],
                                             [rOutArray[index + 1]],
                                             [rOutArray[indexMax]]])
                    rInMatrixInv33 = inv(rInMatrix33)
                    aTemp = rInMatrixInv33.dot(rOutColumn31)
                    print('A_TEMP[0] =                       ********************************<<<<<<<<<<')
                    print(aTemp)
                    # print('testMatrixDF.koc[rayOutElement, keynameA1] = ')
                    # print(testMatrixDF.loc[rayOutElement, keynameA1])
                    # print('testMatrixDF.koc[rayOutElement, keynameA2] = ')
                    # print(testMatrixDF.loc[rayOutElement, keynameA2])
                    # print('testMatrixDF.koc[rayOutElement, keynameA3] = ')
                    # print(testMatrixDF.loc[rayOutElement, keynameA3])

                    testMatrixDF.loc[rayOutElement, keynameA1] = aTemp[0]
                    testMatrixDF.loc[rayOutElement, keynameA2] = aTemp[1]
                    testMatrixDF.loc[rayOutElement, keynameA3] = aTemp[2]

                    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                    # print('testMatrixDF.koc[rayOutElement, keynameA1] =     ')
                    # print(testMatrixDF.loc[rayOutElement, keynameA1])
                    # print('testMatrixDF.koc[rayOutElement, keynameA2] = ')
                    # print(testMatrixDF.loc[rayOutElement, keynameA2])
                    # print('testMatrixDF.koc[rayOutElement, keynameA3] = ')
                    # print(testMatrixDF.loc[rayOutElement, keynameA3])
            testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)
            # writer = pd.ExcelWriter('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls')
            print('testMatrixDF.loc[rayOutElement, keynameA1] =     ')
            print(testMatrixDF)
            testMatrixDF.to_excel('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls',
                                  na_rep='nan')

            ## Calculate Matrix for X_Kx, X*Kx**2, X**2*Kx

            for rin1 in range(0, 3):
                for rin2 in range(rin1 + 1, 4):
                    rInelement1 = rInList[rin1]
                    rInelement2 = rInList[rin2]

                    if rInelement1 == rInelement2:
                        pass
                    else:
                        keynameA11ps = 'A1' + '_' + rInelement1
                        keynameA12pS = 'A2' + rInelement1 + '_' + rInelement1
                        keynameA13pS = 'A3' + rInelement1 + rInelement1 + '_' + rInelement1
                        keynameA21pS = 'A1' + '_' + rInelement2
                        keynameA22pS = 'A2' + rInelement2 + '_' + rInelement2
                        keynameA23pS = 'A3' + rInelement2 + rInelement2 + '_' + rInelement2

                        keynameA2 = 'A2' + rInelement1 + '_' + rInelement2
                        keynameA2inv = 'A2' + rInelement2 + '_' + rInelement1
                        keynameA31 = 'A3' + rInelement1 + rInelement1 + '_' + rInelement2
                        keynameA31inv11 = 'A3' + rInelement1 + rInelement2 + '_' + rInelement1
                        keynameA31inv12 = 'A3' + rInelement2 + rInelement1 + '_' + rInelement1
                        keynameA32 = 'A3' + rInelement2 + rInelement2 + '_' + rInelement1
                        keynameA32inv11 = 'A3' + rInelement2 + rInelement1 + '_' + rInelement2
                        keynameA32inv12 = 'A3' + rInelement1 + rInelement2 + '_' + rInelement2

                        rayInArray = mainRinDF[(mainRinDF.Mode == (rInelement1 + '_' + rInelement2))]
                        index = min(rayInArray.index)
                        indexMax = max(rayInArray.index)
                        # print('rayInArray = ')
                        # print(rayInArray)
                        # print('indexMax', indexMax)
                        # print('indexMin', indexMin)

                        rin11 = rayInArray.loc[index, rInelement1]
                        rin12 = rayInArray.loc[index + 1, rInelement1]
                        rin13 = rayInArray.loc[indexMax, rInelement1]
                        rin21 = rayInArray.loc[index, rInelement2]
                        rin22 = rayInArray.loc[index + 1, rInelement2]
                        rin23 = rayInArray.loc[indexMax, rInelement2]
                        a11 = rin11 * rin21
                        a12 = (rin11 ** 2) * rin21
                        a13 = rin11 * (rin21 ** 2)

                        a21 = rin12 * rin22
                        a22 = (rin12 ** 2) * rin22
                        a23 = rin12 * (rin22 ** 2)

                        a31 = rin13 * rin23
                        a32 = (rin13 ** 2) * rin23
                        a33 = rin13 * (rin23 ** 2)

                        rInMatrix33 = np.array([
                            [a11, a12, a13],
                            [a21, a22, a23],
                            [a31, a32, a33]
                        ])
                        rInMatrixInv33 = inv(rInMatrix33)

                        for rayOutElement in rOutList:
                            A11 = testMatrixDF.loc[rayOutElement, keynameA11ps]
                            A12 = testMatrixDF.loc[rayOutElement, keynameA12pS]
                            A13 = testMatrixDF.loc[rayOutElement, keynameA13pS]
                            A21 = testMatrixDF.loc[rayOutElement, keynameA21pS]
                            A22 = testMatrixDF.loc[rayOutElement, keynameA22pS]
                            A23 = testMatrixDF.loc[rayOutElement, keynameA23pS]

                            rOutArray = RayReflectedDF.loc[index:indexMax, rayOutElement]
                            rOutColumn31 = np.array([[rOutArray[index] -
                                                      (A11 * rin11 + A12 * (rin11 ** 2) + A13 * (
                                                      rin11 ** 3) + A21 * rin21 + A22 * (rin21 ** 2) + A23 * (
                                                       rin21 ** 3))],
                                                     [rOutArray[index + 1] -
                                                      (A11 * rin12 + A12 * (rin12 ** 2) + A13 * (
                                                      rin12 ** 3) + A21 * rin22 + A22 * (rin22 ** 2) + A23 * (
                                                       rin22 ** 3))],
                                                     [rOutArray[indexMax] -
                                                      (A11 * rin13 + A12 * (rin13 ** 2) + A13 * (
                                                      rin13 ** 3) + A21 * rin23 + A22 * (rin23 ** 2) + A23 * (
                                                       rin23 ** 3))]
                                                     ])
                            aTemp = rInMatrixInv33.dot(rOutColumn31)
                            testMatrixDF.loc[rayOutElement, keynameA2] = aTemp[0]
                            testMatrixDF.loc[rayOutElement, keynameA2inv] = 'a2'
                            testMatrixDF.loc[rayOutElement, keynameA31] = aTemp[1]
                            testMatrixDF.loc[rayOutElement, keynameA31inv11] = 'a3'
                            testMatrixDF.loc[rayOutElement, keynameA31inv12] = 'a3'
                            testMatrixDF.loc[rayOutElement, keynameA32] = aTemp[2]
                            testMatrixDF.loc[rayOutElement, keynameA32inv12] = 'a3'
                            testMatrixDF.loc[rayOutElement, keynameA32inv11] = 'a3'
            testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)

            testMatrixDF.to_excel('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls',
                                  na_rep='nan')

            ## Calculate Matrix for X_Kx_Z
            for i1 in range(0, 2):
                keyNameI1 = rInList[i1]
                keynameA11ps = 'A1' + '_' + keyNameI1  # x=
                keynameA211ps = 'A2' + keyNameI1 + '_' + keyNameI1  # x^2=
                keynameA3111ps = 'A3' + keyNameI1 + keyNameI1 + '_' + keyNameI1  # x^3

                for i2 in range((i1 + 1), 3):
                    keyNameI2 = rInList[i2]

                    keynameA12ps = 'A1' + '_' + keyNameI2  # k=
                    keynameA222ps = 'A2' + keyNameI2 + '_' + keyNameI2  # kx^2=
                    keynameA3222ps = 'A3' + keyNameI2 + keyNameI2 + '_' + keyNameI2  # kx^3=
                    keynameA212ps = 'A2' + keyNameI1 + '_' + keyNameI2  # k*x=
                    keynameA3221ps = 'A3' + keyNameI2 + keyNameI2 + '_' + keyNameI1  # k^2*x=
                    keynameA3112ps = 'A3' + keyNameI1 + keyNameI1 + '_' + keyNameI2  # x^2*k=

                    for i3 in range((i2 + 1), 4):
                        keyNameI3 = rInList[i3]

                        keynameA13ps = 'A1' + '_' + keyNameI3  # z=
                        keynameA233ps = 'A2' + keyNameI3 + '_' + keyNameI3  # z^2=
                        keynameA3333ps = 'A3' + keyNameI3 + keyNameI3 + '_' + keyNameI3  # z^3=
                        keynameA213ps = 'A2' + keyNameI1 + '_' + keyNameI3  # x*z=
                        keynameA223ps = 'A2' + keyNameI2 + '_' + keyNameI3  # k*z=
                        keynameA3113ps = 'A3' + keyNameI1 + keyNameI1 + '_' + keyNameI3  # x^2*z=
                        keynameA3223ps = 'A3' + keyNameI2 + keyNameI2 + '_' + keyNameI3  # k^2*z=
                        keynameA3331ps = 'A3' + keyNameI3 + keyNameI3 + '_' + keyNameI1  # z^2*x=
                        keynameA3332ps = 'A3' + keyNameI3 + keyNameI3 + '_' + keyNameI2  # z^2*k=

                        # print('***************** list of Headers ********************************')
                        # print(keynameA11ps)
                        # print(keynameA211ps)
                        # print(keynameA3111ps)
                        # print(keynameA12ps)
                        # print(keynameA222ps)
                        # print(keynameA3222ps)
                        # print(keynameA13ps)
                        # print(keynameA233ps)
                        # print(keynameA3333ps)
                        # print(keynameA212ps)
                        # print(keynameA213ps)
                        # print(keynameA223ps)
                        # print(keynameA223ps)
                        # print(keynameA3112ps)
                        # print(keynameA3113ps)
                        # print(keynameA3221ps)
                        # print(keynameA3223ps)
                        # print(keynameA3331ps)
                        # print(keynameA3332ps)

                        rayIn1x3 = mainRinDF[(mainRinDF.Mode == (keyNameI1 + '_' + keyNameI2 + '_' + keyNameI3))]
                        index = min(rayIn1x3.index)
                        rin11 = rayIn1x3.loc[index, keyNameI1]
                        rin21 = rayIn1x3.loc[index, keyNameI2]
                        rin31 = rayIn1x3.loc[index, keyNameI3]

                        for rOutElement in rOutList:
                            rOut = RayReflectedDF.loc[index, rOutElement]

                            A11ps = (testMatrixDF.loc[rOutElement, keynameA11ps] * rin11) + \
                                    (testMatrixDF.loc[rOutElement, keynameA211ps] * (rin11 ** 2)) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3111ps] * (rin11 ** 3))

                            A22ps = (testMatrixDF.loc[rOutElement, keynameA12ps] * rin21) + \
                                    (testMatrixDF.loc[rOutElement, keynameA222ps] * (rin21 ** 2)) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3222ps] * (rin21 ** 3))

                            A33ps = (testMatrixDF.loc[rOutElement, keynameA13ps] * rin31) + \
                                    (testMatrixDF.loc[rOutElement, keynameA233ps] * (rin31 ** 2)) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3333ps] * (rin31 ** 3))
                            ######################################################
                            A12ps = (testMatrixDF.loc[rOutElement, keynameA212ps] * rin11 * rin21) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3112ps] * ((rin11 ** 2) * rin21)) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3221ps] * ((rin21 ** 2) * rin11))

                            A13ps = (testMatrixDF.loc[rOutElement, keynameA213ps] * rin11 * rin31) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3112ps] * ((rin11 ** 2) * rin31)) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3221ps] * ((rin31 ** 2) * rin11))

                            A23ps = (testMatrixDF.loc[rOutElement, keynameA223ps] * rin21 * rin31) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3223ps] * ((rin21 ** 2) * rin31)) + \
                                    (testMatrixDF.loc[rOutElement, keynameA3332ps] * ((rin31 ** 2) * rin21))
                            ########################################################
                            AtotalPS = A11ps + A22ps + A33ps + A12ps + A13ps + A23ps
                            Rin = (rin11 * rin21 * rin31)
                            a = (rOut - AtotalPS) / Rin
                            header123 = 'A3' + keyNameI1 + keyNameI2 + '_' + keyNameI3
                            header132 = 'A3' + keyNameI1 + keyNameI3 + '_' + keyNameI2
                            header213 = 'A3' + keyNameI2 + keyNameI1 + '_' + keyNameI3
                            header231 = 'A3' + keyNameI2 + keyNameI3 + '_' + keyNameI1
                            header312 = 'A3' + keyNameI3 + keyNameI1 + '_' + keyNameI2
                            header321 = 'A3' + keyNameI3 + keyNameI2 + '_' + keyNameI1
                            testMatrixDF.loc[rOutElement, header123] = a
                            testMatrixDF.loc[rOutElement, header132] = 'A132'
                            testMatrixDF.loc[rOutElement, header213] = 'A213'
                            testMatrixDF.loc[rOutElement, header231] = 'A231'
                            testMatrixDF.loc[rOutElement, header312] = 'A312'
                            testMatrixDF.loc[rOutElement, header321] = 'A321'

            testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)

            testMatrixDF.to_excel('/home/konstantin/PycharmProjects/RayTracer/result/' +
                                  str(testMatrixFName) +
                                  '.xls', na_rep='nan')

            countMirror += 1

            print('***********************************************************    End  Ray Loop:    ', mirrorList)

    print('===========================================================================  End Mirror Loop')


pathName()

# ==================   Test for Aberation 1 =====================================

# *******************************  Rays Generator ******************************

rInObject = Rays()  # Create object of Rays
# Rays4Test3PointDF = t.raysTestGenerator()
# rInObject.saveRays2Execel(ray4test3pointFname, Rays4Test3PointDF)

##########################################################  Run For Test ############################################

# =============   Read  Excel file with Rays Data in =========================
tLine = Parametrs(mainPath + sysParamFname + fExtend, "LineParam")
sys = Parametrs(mainPath + sysParamFname + fExtend, "SysParam")
mainRin = Parametrs(ray4test3pointFname, "Sheet1")
raysSheetName0 = 'Ray_' + str(int(sys.dataSheet.Rin[0] - 1)) + '_' + str(int(sys.dataSheet.Rin[0]))

# =============  Normilise Rin for Mirror  ===================================
mirror1SheetName = 'Mirror' + str(int(sys.dataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath + sysParamFname + fExtend, 'Mirror1')
raysDataFrame = rInObject.rInNormalise(mirrorObject.dataSheet, mainRin.dataSheet)
# save to Excel
rInObject.saveRays2Execel(mainPath + 'Ray' + '_' +
                          str(int(sys.dataSheet.Rin[0] - 1)) + '_' +
                          str(int(sys.dataSheet.Rin[0]))
                          + fExtend,
                          raysDataFrame)

# ==============  Get List of Section for calculation ========================#
mirrorDictMain = sys.getMirrorList(sys.dataSheet)

# =============== Ray Tracing =================================================#
# mirrorLoop(mirrorDictMain)
#
# #=============== Plotting ====================================================
sys = Parametrs(mainPath + sysParamFname + fExtend, "SysParam")
# py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
# plotLoop(mirrorDictMain)

testMatrixLoop(mirrorDictMain)
