import  numpy as np
import pandas as pd
import plotly.graph_objs  as go

import plotly as py

from scr.MainParam import Parametrs
from scr.Ploting import Ploting
from scr.Rays import Rays
from scr.MainParam import Parametrs

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

def pathName():
    global mainPath, fExtend, sysParamFname, raysInFname
    mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
    fExtend = '.xls'
    sysParamFname = 'sysParam_1'
    raysInFname = 'RaysIn'
    raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname + '_' + sysParamFname
def mirrorLoop(mirrorDictMain):
    for mirrorDictSub in mirrorDictMain.keys():
        #print(sys.dataSheet.Rin[0])
        countMirror = int(sys.dataSheet.Rin[0])
        #print('========= Mirror Loop',countMirror)
        #print(mirrorDictSub)
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            # print("Count = ", countMirror)
            #print("Current Mirror = ", mirrorList)

            Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
            # print('Mirror = ')
            # print(Mirror)

            ################################################################
            # print('=============',RaysInDF)
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                             'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                             'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            RaysObject = Parametrs(mainPath + raysFName[0] + fExtend, 'Sheet1')
            #print(RaysObject.dataSheet)
            path = [mainPath, raysFName, fExtend]
            # print('path = ', path )
            rInObject.calcReflectedRays(path, Mirror, RaysObject.dataSheet)
            countMirror += 1
def printFromExel():
    print('==============================')
    print(tLine.dataSheet)
    print('==============================')
    print(sys.dataSheet)
    print('==============================')
    print(Rin.dataSheet)
    print('==============================')
def plotLoop(mirrorDictMain):
    for mirrorDictSub in mirrorDictMain.keys():
        # print(sys.dataSheet)
        countMirror = int(sys.dataSheet.Rin[0])
        print('CountMirror', countMirror)
        print('****************************************************************** Mirror Loop',countMirror)
        print(mirrorDictSub)
        data = []
        layout = []
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            print("Count = ", countMirror)
            print("Current Mirror = ", mirrorList)
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
            plotObject.setMirrorSurf(mirrorObject.dataSheet)
            #print('plotObject.data = ',plotObject.data)
            data.append(plotObject.rayInDict)
            data.append(plotObject.rayReflectedDict)
            print('===========================================================================  End Mirror Loop')
            countMirror += 1
        data.append(plotObject.Tline1)
        data.append(plotObject.Tline2)
        layout = plotObject.layout
    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, filename='line-mode.html')



pathName()

#=============   Read  Excel file with Rays Data in =========================
tLine = Parametrs(mainPath+sysParamFname + fExtend, "LineParam")
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
Rin = Parametrs(mainPath + raysInFname + fExtend, "Rin")
raysSheetName0 = 'Ray_' + str(int(sys.dataSheet.Rin[0] - 1)) + '_' + str(int(sys.dataSheet.Rin[0]))

rInObject = Rays()  # Create object of Rays

#=============  Normilise Rin for Mirror  ===================================
mirror1SheetName = 'Mirror' + str(int(sys.dataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath+sysParamFname + fExtend, 'Mirror1')
raysDataFrame = rInObject.rInNormalise(mirrorObject.dataSheet, Rin.dataSheet)
# save to Excel
rInObject.saveRays2Execel(mainPath + 'Ray'+'_' +
                          str(int(sys.dataSheet.Rin[0]-1)) + '_' +
                          str(int(sys.dataSheet.Rin[0]))
                          + fExtend,
                          raysDataFrame)
#==============  Get List of Section for calculation ========================
mirrorDictMain = sys.getMirrorList(sys.dataSheet)

#=============== Ray Tracing =================================================
#mirrorLoop(mirrorDictMain)

#=============== Plotting ====================================================
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
plotLoop(mirrorDictMain)

