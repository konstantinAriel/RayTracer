import  numpy as np
import pandas as pd
import plotly.graph_objs  as go
from scr.Ploting.PlotingRayTracing import PlotingRayTracing
import scr.mainParamPakage as mp
import plotly as py
import scr.RayTracing.Rays as rmain

#from scr.Ploting import Ploting
from scr.MainParam import Parametrs
from scr import Ploting

####################################################################################################
#                                                                                                  #
#                                F U N C T I O N                                                   #
#                                                                                                  #
####################################################################################################

def pathName():
    global mainPath, fExtend, sysParamFname, raysInFname, ray4test3pointFname
    mainPath = "/home/konstantin/rt/RayTracer/files/settingsfiles/"
    fExtend = '.xls'
    sysParamFname = 'sysParam_1'

    raysInFname = 'RaysIn'

    raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname + '_' + sysParamFname
    ray4test3pointFname = mainPath + 'ray4test3Point_'  + sysParamFname + fExtend

def mirrorLoop(mirrorList):
    countMirror = int(sysParam.DataSheet.Rin[0])
    for mirrorIndex in mirrorList:
        print( '====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++  Mirror Loop  ',mirrorIndex)
        Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
        ################################################################
        raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                    'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                    'normalRay_' + str(countMirror) + '_' + str(countMirror)]

        ## mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"

        RaysObject = Parametrs(mainPath + raysFName[0] + fExtend, 'Sheet1')
        rayInData2dDict = []
        rayReflectedDict2d = []
        path = [mainPath, raysFName, fExtend]
        rInObject.getReflectedRays()
        countMirror += 1
    print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++   END   Mirror Loop         ',  mirrorList)

def printFromExel():   ## N O  U S E G E !!!
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

            mirrorObject = Parametrs(mainPath + sysParamFname + fExtend, mirrorList)  ## mirror List - The name of Sheets in Exel file

            ################################################################
            # print('=============',RaysInDF)
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            path = [mainPath, raysFName, fExtend]
            print('path = ', path )
            # RaysInObject =
            # RaysNormalObject
            # RayReflectedObject
            plotObject = Ploting(path, mirrorObject.dataSheet, mirrorList, RaysInObject, RaysNormalObject, RayReflectedObject)

            surfR = plotObject.setMirrorSurf

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

#######################################################################################################
#                                                                                                     #
#                                                                                                     #
#                      P R O G R A M M    I S   R  U N N I N G  F R O M    H E R E                    #
#                                                                                                     #
#                                                                                                     #
#######################################################################################################

pathName()  #

 ####################################################################################  for Standard RUN ################
#=============   Read  Excel file with Rays Data in =========================

tLine = Parametrs(mainPath+sysParamFname + fExtend, "LineParam")
sysParam = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, "SysParam")

#   C H O O S E   F I L E    W I T H   RAYS_in
Rin = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.rInDir +  mp.raysInFname + mp.fExtend, 'Xin')

#Rin = Parametrs(mainPath + raysInFname + fExtend, "Rin")
# Rin = Parametrs('/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/RaysIn.xls', "Xin")
# Rin = Parametrs('/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/RaysIn.xls', 'circul')
# Rin = Parametrs('/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/RaysIn.xls', 'circlParalel')
#Rin = Parametrs('/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/RaysIn.xls', 'KonusFrom1Point')

raysSheetName0 = 'Ray_' + str(int(sysParam.DataSheet.Rin[0] - 1)) + '_' + str(int(sysParam.DataSheet.Rin[0]))  # Ray_0_1


#=============  Normilise Rin for Mirror  ===================================
mirror1SheetName = 'Mirror' + str(int(sysParam.DataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath+sysParamFname + fExtend, 'Mirror1')
rOutFname = 'Ray'+'_' + \
           str(int(sysParam.DataSheet.Rin[0]-1)) + '_' + \
           str(int(sysParam.DataSheet.Rin[0]))
rInObject = rmain.Rays(mirrorObject.dataSheet, Rin.DataSheet, getRefRay = 0)  # Create object of Rays
raysInDFn = rInObject.RaysDFnormal
raysInDFn.to_excel(mp.mainPath + mp.xlsDir + mp.rOutDir  + rOutFname + mp.fExtend)

#==============  Get List of Section for calculation ========================#
mirrorDictMain = sysParam.getMirrorList(sysParam.DataSheet)
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
#=============== Ray Tracing =================================================#
mirrorLoop(mirrorDictMain)

#=============== Plotting ====================================================

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
plotLoop(mirrorDictMain)

