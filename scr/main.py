import  numpy as np
import pandas as pd
import plotly.graph_objs  as go
import plotly as py

from scr.MainParam import Parametrs
from scr.Ploting import Ploting
from scr.Rays import Rays
from scr.MainParam import Parametrs

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
            print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',  mirrorList)
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
            print(RaysObject.dataSheet)
            rayInData2dDict = []
            rayReflectedDict2d = []
            path = [mainPath, raysFName, fExtend]
            # print('path = ', path )
            rInObject.calcReflectedRays(path, Mirror, RaysObject.dataSheet)
            countMirror += 1
    print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++   END   Mirror Loop         ',  mirrorList)

def printFromExel():
    print('==============================')
    print(tLine.dataSheet)
    print('==============================')
    print(sys.dataSheet)
    print('==============================')
    print(Rin.dataSheet)
    print('==============================')

def plotLoop(mirrorDictMain):
    dataRays = []
    for mirrorDictSub in mirrorDictMain.keys():
        # print(sys.dataSheet)
        countMirror = int(sys.dataSheet.Rin[0])
        # print('CountMirror', countMirror)
        # print('****************************************************************** Mirror Loop',countMirror)
        # print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',countMirror)
        dataRays = []
        dataIn2d = []
        dataRef2d = []
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
            dataRays.append(plotObject.rayInDict)
            dataRays.append(plotObject.rayReflectedDict)
            # dataRays.append(plotObject.PolarInDict)
            # dataRays.append(plotObject.PolarReflectedDict)
            dataRays.append(surfR)
            # dataIn2d.append(plotObject.rayInData2dDict)
            # dataRef2d.append(plotObject.rayReflectedDict2d)
            # layout = plotObject.layout
            # fig2 = dict(data=dataIn2d, layout=layout)
            # py.offline.plot(fig2, filename='DataIn_' + str(mirrorList) + '.html')
            #
            # fig3 = dict(data=dataRef2d, layout=layout)
            # py.offline.plot(fig3, filename='DataRef'  + str(mirrorList) +'.html')

            # print('===========================================================================  End Mirror Loop')
            countMirror += 1
        dataRays.append(plotObject.Tline1)
        dataRays.append(plotObject.Tline2)
        layout = plotObject.layout
    #print(data)
    fig1 = dict(data=dataRays, layout=layout)
    py.offline.plot(fig1, filename='RayTracing.html')

    # fig2 = dict(data=dataIn2d, layout=layout)
    # py.offline.plot(fig2, filename='DataIn.html')
    #
    # fig3 = dict(data=dataRef2d, layout=layout)
    # py.offline.plot(fig3, filename='RayTracing.html')

pathName()

 ####################################################################################  for Standard RUN ################
#=============   Read  Excel file with Rays Data in =========================
tLine = Parametrs(mainPath+sysParamFname + fExtend, "LineParam")
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
# Rin = Parametrs(mainPath + raysInFname + fExtend, "Rin")
#Rin = Parametrs('/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/RaysIn.xls', "Xin")
# Rin = Parametrs('/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/RaysIn.xls', 'circul')
Rin = Parametrs('/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/RaysIn.xls', 'circlParalel')
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

#==============  Get List of Section for calculation ========================#
mirrorDictMain = sys.getMirrorList(sys.dataSheet)

#=============== Ray Tracing =================================================#
mirrorLoop(mirrorDictMain)

#=============== Plotting ====================================================
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
plotLoop(mirrorDictMain)

