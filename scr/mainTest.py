import  numpy as np
import pandas as pd
import xarray as xr
import plotly.graph_objs  as go

import plotly as py
from numpy.linalg import inv
from numpy import nan
from scr.Test import Test
from scr.MainParam import Parametrs
from scr.Ploting import Ploting
from scr.Rays import Rays
from scr.MainParam import Parametrs
from scr.TestMatrix import TestMatrix

def setZeroDict(rInList, rOutList, startMirror, countMirror):
    testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)

    tempNANarray44 = np.array([[nan, nan, nan, nan],
                             [nan, nan, nan, nan],
                             [nan, nan, nan, nan],
                             [nan, nan, nan, nan]
                             ])
    # tempDataSet = xr.Dataset()

    tempNANdf4x4 = pd.DataFrame(tempNANarray44, index=rOutList, columns=rInList)
    keynameA1 = 'A1'
    # tempDataSet[keynameA1] = tempNANdf4x4
    # testMatrixDict = dict()
    matrixName = []
    # testMatrixDict[keynameA1] = tempNANdf4x4
    matrixName.append(keynameA1)
    for rInTemp1 in rInList:
        keynameA2 = 'A2'  + rInTemp1
        matrixName.append(keynameA2)
        # tempDataSet[keynameA2] = tempNANdf4x4
        # testMatrixDict[keynameA2] = tempNANdf4x4
        for rInTemp2 in rInList:
            keynameA3 = 'A3'  + rInTemp1  + rInTemp2
            # tempDataSet[keynameA3] = tempNANdf4x4
            matrixName.append(keynameA3)
            # testMatrixDict[keynameA3] = tempNANdf4x4
    testMatrixDict = dict()
    testMatrixDict = testMatrixDict.fromkeys(matrixName, tempNANdf4x4)
    # print('matrixName')
    # print(matrixName)
    # print('testMatrixDict = ')
    # print(testMatrixDict)
    writer = pd.ExcelWriter('/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls', na_rep='nan')
    for matrixNameElement in matrixName:
        # print('matrixNameElement')
        # print(matrixNameElement)
        # print('testMatrixDict = ')
        # print(testMatrixDict[matrixNameElement])
        testMatrixDict[matrixNameElement].to_excel(writer, na_rep='nan', sheet_name=matrixNameElement)
    writer.save()
    return testMatrixDict, writer


def pathName():
    global mainPath, fExtend, sysParamFname, raysInFname, ray4test3pointFname
    mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
    fExtend = '.xls'
    sysParamFname = 'sysParam_1'
    raysInFname = 'RaysIn'
    raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname + '_' + sysParamFname
    ray4test3pointFname = mainPath + 'ray4test3Point_'  + sysParamFname + fExtend

def mirrorLoop(mirrorDictMain):
    for mirrorDictSub in mirrorDictMain.keys():
        #print(sys.dataSheet.Rin[0])
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
    #print(Rin.dataSheet)
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
            mirrorObject = Parametrs(mainPath + sysParamFname + fExtend, mirrorList)  ## mirror List - The name of Sheets in Exel file
            # print('Mirror = ')
            # print(mirrorObject.dataSheet)
            ################################################################
            # print('=============',RaysInDF)
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            path = [mainPath, raysFName, fExtend]
            # print('path = ', path )
            plotObject = Ploting(path, mirrorObject.dataSheet, mirrorList)

            surfR = plotObject.setMirrorSurf(mirrorObject.dataSheet)

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
    py.offline.plot(fig, filename='42RaysforTest MAtrix.html')

def testMatrixLoop(mirrorDictMain):
    data = []
    for mirrorDictSub in mirrorDictMain.keys():
          # print(sys.dataSheet)
          countMirror = int(sys.dataSheet.Rin[0])
          startMirror = int(sys.dataSheet.Rin[0])-1
          raysObject = Rays()
          print('***********************************+******************************* TestMatrixLOOP',countMirror)
#### GET Ray_In in  the System
          mainRinDF = mainRin.dataSheet
          # print(mainRinDF)
          data = []
          layout = []
          rInList = ['Xin', 'Kxin', 'Zin', 'Kzin']
          # rOutList = ['Xout','Kxout','Zout', 'Kzout']
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
              print('startMirror = ')
              print(startMirror)
              print('countMirror = ')
              print(countMirror)
              testMatrixDataset, writer = setZeroDict(rInList, rOutList, startMirror, countMirror)
              # print('testMatrixDict')
              # print(testMatrixDict)
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
              keynameA1 = 'A1'
              matrixName = []
              matrixName.append(keynameA1)
              tempNANarray44 = np.array([[nan, nan, nan, nan],
                                         [nan, nan, nan, nan],
                                         [nan, nan, nan, nan],
                                         [nan, nan, nan, nan]
                                         ])
              tempNANdf4x4 = pd.DataFrame(tempNANarray44, index=rOutList, columns=rInList)


              for rInelement in rInList:
                  # print('i = ', rInelement)
                  # print('*********************   Rin =  ********  ', rInelement,'   ******************')
                  rayInArray = mainRinDF[(mainRinDF.Mode == rInelement)]
                  indexMin = min(rayInArray.index)
                  indexMax = max(rayInArray.index)
                  # print('rayInArray = ')
                  # print(rayInArray)
                  # print('indexMax', indexMax)
                  # print('indexMin', indexMin)
              ## Calilus For a11 a22 a33 a44
                  a1 = np.array([[1, 1, 1], [2,2,2]])
                  a2 = np.array([[3,3,3], [4,4,4]])
                  Alist  = [a1, a2]
                  print('Alist = ')
                  print(Alist)
                  Alist[a1[0,0]] = 5
                  print('Alist = ')
                  print(Alist)
                  a11 = rayInArray.loc[indexMin, rInelement]
                  a12 = a11**2
                  a13 = a11**3
                  a21 = rayInArray.loc[indexMin+1,rInelement]
                  a22 = a21**2
                  a23 = a21**3
                  a31 = rayInArray.loc[indexMax, rInelement]
                  a32 = a31**2
                  a33 = a31**3
                  rInMatrixInv33 = np.array([
                                             [a11, a12, a13],
                                             [a21, a22, a23],
                                             [a31, a32, a33]
                                          ])
                  keynameA2 = 'A2' +  rInelement
                  keynameA3 = 'A3' +  rInelement + rInelement

                  matrixName.append(keynameA2)
                  matrixName.append(keynameA3)
                  for rayOutelement in rOutList:

                      rOutArray = RayReflectedDF.loc[indexMin:indexMax, rayOutelement]
                      rOutColumn31 = np.array([[rOutArray[indexMin]],
                                               [rOutArray[indexMin + 1]],
                                               [rOutArray[indexMax]]])
                      rInMatrixInv33 = inv(rInMatrixInv33)
                      aTemp = rInMatrixInv33.dot(rOutColumn31)

                      print('A_TEMP = ')
                      print(aTemp)
                      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                      a = aTemp[0]
                      b = aTemp[1]
                      c = aTemp[2]
                      print(' writer.path = ')
                      print( writer.path)
                      paramExelfile = pd.ExcelFile(writer.path)
                      print(paramExelfile.sheet_names)
                      testMatrixFName = 'testMatrix_' + str(startMirror) + '_' + str(countMirror)
                      writer = pd.ExcelWriter(
                                              '/home/konstantin/PycharmProjects/RayTracer/result/' + str(testMatrixFName) + '.xls',
                                              na_rep='nan'
                                             )
                      for sheetNameElement in paramExelfile.sheet_names:
                          AtempDF = Parametrs(writer.path, sheetNameElement).dataSheet
                          if sheetNameElement == keynameA1:
                              AtempDF.loc[rayOutelement, rInelement] = a
                              AtempDF.to_excel(writer, na_rep='nan', sheet_name=sheetNameElement)
                          elif sheetNameElement == keynameA2:
                              AtempDF.loc[rayOutelement, rInelement] = b
                              AtempDF.to_excel(writer, na_rep='nan', sheet_name=sheetNameElement)
                          elif sheetNameElement == keynameA3:
                              AtempDF.loc[rayOutelement, rInelement] = c
                              AtempDF.to_excel(writer, na_rep='nan', sheet_name=sheetNameElement)
                          else:
                              AtempDF.to_excel(writer, na_rep='nan', sheet_name=sheetNameElement)
                      writer.save()


              countMirror += 1

              print('***********************************************************    End  Ray Loop:    ', mirrorList)

    print('===========================================================================  End Mirror Loop')

pathName()

#==================   Test for Aberation 1 =====================================

# *******************************  Rays Generator ******************************
t = Test()
rInObject = Rays()  # Create object of Rays
Rays4Test3PointDF = t.raysTestGenerator()
rInObject.saveRays2Execel(ray4test3pointFname, Rays4Test3PointDF)

##########################################################  Run For Test ############################################

#=============   Read  Excel file with Rays Data in =========================
tLine = Parametrs(mainPath+sysParamFname + fExtend, "LineParam")
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
mainRin = Parametrs(ray4test3pointFname, "Sheet1")
raysSheetName0 = 'Ray_' + str(int(sys.dataSheet.Rin[0] - 1)) + '_' + str(int(sys.dataSheet.Rin[0]))

#=============  Normilise Rin for Mirror  ===================================
mirror1SheetName = 'Mirror' + str(int(sys.dataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath+sysParamFname + fExtend, 'Mirror1')
raysDataFrame = rInObject.rInNormalise(mirrorObject.dataSheet, mainRin.dataSheet)
# save to Excel
rInObject.saveRays2Execel(mainPath + 'Ray'+'_' +
                          str(int(sys.dataSheet.Rin[0]-1)) + '_' +
                          str(int(sys.dataSheet.Rin[0]))
                          + fExtend,
                          raysDataFrame)

#==============  Get List of Section for calculation ========================#
mirrorDictMain = sys.getMirrorList(sys.dataSheet)

#=============== Ray Tracing =================================================#
# mirrorLoop(mirrorDictMain)
#
# #=============== Plotting ====================================================
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
# py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
# plotLoop(mirrorDictMain)

testMatrixLoop(mirrorDictMain)
