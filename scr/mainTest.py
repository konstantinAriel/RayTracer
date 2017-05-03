import  numpy as np
import pandas as pd
import plotly.graph_objs  as go

import plotly as py

from scr.Test import Test
from scr.MainParam import Parametrs
from scr.Ploting import Ploting
from scr.Rays import Rays
from scr.MainParam import Parametrs
from scr.TestMatrix import TestMatrix


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
          countMirror = int(sys.dataSheet.Rin[0])+1

          print('****************************************************************** TestMatrixLOOP',countMirror)
#### GET Ray_In in  the System
          mainRinDF = mainRin.dataSheet
          print(mainRinDF)
          data = []
          layout = []
          rInList = ['Xin', 'Kxin', 'Zin', 'Kzin']

          # LOOP 1st ORDR
          countMirror = int(sys.dataSheet.Rin[0])
          for mirrorList in mirrorDictMain.get(mirrorDictSub):
              mirrorObject = Parametrs(mainPath + sysParamFname + fExtend,
                                       mirrorList)  ## mirror List - The name of Sheets in Exel file

              raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                           'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                           'normalRay_' + str(countMirror) + '_' + str(countMirror)]
              print('Rays Name')
              print(raysFName)
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
              for rInelement in rInList:
                  print('i = ', rInelement)
                  print('*********************   Rin =  ********  ', rInelement,'   ******************')
                  rayInArray = mainRinDF[(mainRinDF.Mode == rInelement)]
                  indexMin = min(rayInArray.index)
                  indexMax = max(rayInArray.index)
                  print('rayInArray = ')
                  print(rayInArray)
                  print('indexMax', indexMax)
                  print('indexMin', indexMin)
              ## Calilus For a11 a22 a33 a44

                  a11 = rayInArray.loc[indexMin, rInelement]
                  a21 = a11**2
                  a31 = a11**3
                  a12 = rayInArray.loc[indexMin+1,rInelement]
                  a22 = a12**2
                  a32 = a12**3
                  a13 = rayInArray.loc[indexMax, rInelement]
                  a23 = a13**2
                  a33 = a13**3
                  rInMatrixInv33 = np.array([
                            [a11, a12, a13],
                            [a21, a22, a23],
                            [a31, a32, a33]
                             ])
                  for rayOutelement in rInList:
                        rOutArray = RayReflectedDF.loc[indexMin:indexMax, rayOutelement]
                        rOutColumn31 = np.array([[rOutArray[indexMin]],
                                                [rOutArray[indexMin + 1]],
                                                [rOutArray[indexMax]]])
                        aTemp = rInMatrixInv33.dot(rOutColumn31)
                        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ',  rayOutelement,    '^^^^^^^^^^^^^^')
                        print('rInArray = ')
                        print(rInMatrixInv33)
                        print('rOutArray = ')
                        print(rOutColumn31)
                        print('A_TEMP = ')
                        print(aTemp)
                        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
              countMirror += 1
              # print('path = ', path)
              # print(mirrorObject.dataSheet)
              # print(RaysInObject.dataSheet)
              # print(RayReflectedObject.dataSheet)
              # print(RaysNormalObject.dataSheet)
              # print('mirrorDictMain.get(mirrorDictSub):', mirrorDictMain.get(mirrorDictSub))
              # print("Current Mirror = ", mirrorList)
              # print("Count = ", countMirror)
              print('***********************************************************    End  Ray Loop:    ', mirrorList)
              # print('Ray In = ', raysObject.rayInDict)
              # print('Reflected', raysObject.rayReflectedDict)
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
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
plotLoop(mirrorDictMain)

testMatrixLoop(mirrorDictMain)
