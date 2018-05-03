from scr.Ploting.PlotingRayTracing import PlotingRayTracing
from scr.Ploting.PlotPoarization import Plotpolarization
import scr.mainParamPakage as mp
import scr.RayTracing.Rays as rmain

# import numpy as np
#                                            I n i t

tLine = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, "LineParam")
sysParam = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, "SysParam")
Rin = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.rInDir +  mp.raysInFname + mp.fExtend, 'circul20')

mirrorSheetName = 'Mirror' + str(int(sysParam.DataSheet.Rin[0]))
raysSheetName = 'Ray_' + str(int(sysParam.DataSheet.Rin[0] - 1)) + '_' + str(int(sysParam.DataSheet.Rin[0]))
# print('Rin.DataSheet = IN mainRun')
# print(Rin.DataSheet)

mirrorObj = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, 'Mirror1')
rInObj = rmain.Rays(mirrorObj.DataSheet, Rin.DataSheet, getRefRay=0)  # Create object of Rays

raysInDFn = rInObj.RaysDFnormal
# save to Excel
rOutFname = 'Ray'+'_' + \
           str(int(sysParam.DataSheet.Rin[0]-1)) + '_' + \
           str(int(sysParam.DataSheet.Rin[0]))

mirrorList = sysParam.getMirrorList(sysParam.DataSheet)
raysInDFn.to_excel(mp.mainPath + mp.xlsDir + mp.rOutDir  + rOutFname + mp.fExtend)

#     ==============  Get List of Section for calculation ========================#

def mirrorLoop(mirrorList):
        countMirror = int(sysParam.DataSheet.Rin[0])
        for mirrorIndex in mirrorList:
            print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',  mirrorIndex)
            Mirror = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, mirrorIndex)  ## mirror List - The name of Sheets in Exel file
            raysFName =  ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            RaysObj = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[0] + mp.fExtend, 'Sheet1' )
            # print(RaysObj.DataSheet)
            pathList = [mp.mainPath + mp.xlsDir + mp.rOutDir , raysFName, mp.fExtend]
            refRayObj = rmain.Rays(Mirror.DataSheet, RaysObj.DataSheet, getRefRay=1)
            refRayObj.NormalRayDF.to_excel(mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[2] + mp.fExtend, 'Sheet1')
            refRayObj.ReflectedRayDF.to_excel(mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[1] + mp.fExtend, 'Sheet1')
            countMirror += 1
        print('============== ++++++++++++++++++++++++++++++++++++++++++++++++++++++   END   Mirror Loop',  mirrorIndex)

def plotLoop(mirrorList):

    countMirror = int(sysParam.DataSheet.Rin[0])

    print('******************************************************************  PlotLoop',countMirror)
    dataRays = []
    data2D= []
    for mirrorIndex in mirrorList:
        print('mirrorIndex = ', mirrorIndex)
        Mirror = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, mirrorIndex)  ## mirror List - The name of Sheets in Exel file
        raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                     'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                     'normalRay_' + str(countMirror) + '_' + str(countMirror)]

        pathInRay = mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[0] + mp.fExtend
        pathReflctedRay = mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[1] + mp.fExtend
        pathNormalRay = mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[2] + mp.fExtend

        # print('pathInRay = ', pathInRay)
        # print('pathReflctedRay = ', pathReflctedRay)
        # print('pathNormalRay = ', pathNormalRay)

        RaysInObject = mp.Parametrs(pathInRay, 'Sheet1')
        RayReflectedObject = mp.Parametrs(pathReflctedRay, 'Sheet1')
        RaysNormalObject = mp.Parametrs(pathNormalRay, 'Sheet1')
        plotFileName = mp.mainPath + 'result/htmlFiles/test.html'
        plotFileName2D = mp.mainPath + 'result/htmlFiles/test2D' + '_' + mirrorIndex + '.html'

        plotObject = PlotingRayTracing(Mirror.DataSheet, RaysInObject.DataSheet, RayReflectedObject.DataSheet, RaysNormalObject.DataSheet, mirrorIndex, plotFileName)
        plotObject2D = Plotpolarization(Mirror.DataSheet, RaysInObject.DataSheet, RayReflectedObject.DataSheet,
                                      RaysNormalObject.DataSheet, mirrorIndex, plotFileName2D)

        surfR = plotObject.setMirrorSurf()
        dataRays.append(plotObject.rayInDict)
        dataRays.append(plotObject.rayReflectedDict)
        dataRays.append(plotObject.rayReflectedDictMarkers)
        dataRays.append(plotObject.rayInDictMarkers)
        dataRays.append(plotObject.pInData)
        # dataRays.append(surfR)

        data2D.append(plotObject.rayInDict)
        data2D.append(plotObject.pInData)
        if mirrorIndex == 'Mirror4':
             data2D.append(plotObject.rayReflectedDict)
        plotObject2D.plotIs(data2D, plotObject.layout, plotObject2D.plotFileName)

        data2D = []

        countMirror += 1
    print('===========================================================================  End Plot Loop')
    dataRays.append(plotObject.Tline1)
    dataRays.append(plotObject.Tline2)
    layout = plotObject.layout
    plotObject.plotIs(dataRays, layout)

def plotLoopPolar(mirrorList):
    countMirror = int(sysParam.DataSheet.Rin[0])
    # print('****************************************************************** Mirror Loop',countMirror)
    dataRays = []
    data1 = []
    dataInOut = []
    for mirrorIndex in mirrorList:
        Mirror = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend,
                              mirrorIndex)  ## mirror List - The name of Sheets in Exel file
        MdfSx = Mirror.DataSheet.Source[0]
        MdfSy = Mirror.DataSheet.Source[1]
        MdfSz = Mirror.DataSheet.Source[2]

        MdfDx = Mirror.DataSheet.Detector[0]
        MdfDy = Mirror.DataSheet.Detector[1]
        MdfDz = Mirror.DataSheet.Detector[2]

        raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                     'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                     'normalRay_' + str(countMirror) + '_' + str(countMirror)]

        pathInRay = mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[0] + mp.fExtend
        pathReflctedRay = mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[1] + mp.fExtend
        pathNormalRay = mp.mainPath + mp.xlsDir + mp.rOutDir + raysFName[2] + mp.fExtend

        RaysInObject = mp.Parametrs(pathInRay, 'Sheet1')
        RayReflectedObject = mp.Parametrs(pathReflctedRay, 'Sheet1')
        RaysNormalObject = mp.Parametrs(pathNormalRay, 'Sheet1')

        plotFileName = mp.mainPath +'result/htmlFiles/Rin_vs_Rout' + str(mirrorIndex) + '.html'
        plotFileName1 = mp.mainPath +'result/htmlFiles/DataIN_' + str( mirrorIndex) + '.html'
        plotFileName2 = mp.mainPath + 'result/htmlFiles/DataInOut_' + str( mirrorIndex) + '.html'

        plotObject = Plotpolarization(Mirror.DataSheet, RaysInObject.DataSheet, RayReflectedObject.DataSheet,
                                      RaysNormalObject.DataSheet, mirrorIndex, plotFileName)
        dataRays.append(plotObject.setRays4Plot_All)

        DataIn1, DataOut1, DataInOut1, PinData1, POutData1, rayMInDict = plotObject.setRays4plotSection(0,20, Mirror.DataSheet, 'blue') #from 0 t0 19

        data1.append(DataIn1)
        data1.append(DataOut1)
        data1.append(PinData1)
        data1.append(POutData1)
        data1.append(rayMInDict)

        dataInOut.append(DataInOut1)
        dataInOut.append(PinData1)
        dataInOut.append(POutData1)

        # DataIn2, DataOut2, DataInOut2, PinData2, POutData2 = plotObject.setRays4plotSection(20, 40, 'green' )
        #
        # data1.append(DataIn2)
        # data1.append(DataOut2)
        # data1.append(PinData2)
        # data1.append(POutData2)
        #
        # dataInOut.append(DataInOut2)
        # dataInOut.append(PinData2)
        # dataInOut.append(POutData2)
        #
        # DataIn3, DataOut3, DataInOut3, PinData3, POutData3 = plotObject.setRays4plotSection(40, 60,'red')
        #
        # data1.append(DataIn3)
        # data1.append(DataOut3)
        # data1.append(PinData3)
        # data1.append(POutData3)
        #
        # dataInOut.append(DataInOut3)
        # dataInOut.append(PinData3)
        # dataInOut.append(POutData3)

        # print('DataIn1 = ')
        # print(DataIn1)
        # print('DataIn2 = ')
        # print(DataIn2)
        # print('DataIn3 = ')
        # print(DataIn3)

        countMirror += 1
        #dataRays.append(plotObject.rayReflectedDict)

        layout = plotObject.layout
        # plotObject.plotIs(dataRays, layout, plotFileName)
        plotObject.plotIs(data1, layout, plotFileName1)
        plotObject.plotIs(dataInOut, layout, plotFileName2)
        dataRays = []
    print('===========================================================================  End Plot Loop')

mirrorLoop(mirrorList)

# mainDir = '/home/konstantin/rt/RayTracer/'
# RinDirName = '/home/konstantin/rt/RayTracer/files/XLS/Rout/'
# R1 = mp.Parametrs(RinDirName + 'Ray_0_1.xls', 'Sheet1')
# R2 = mp.Parametrs(RinDirName + 'Ray_1_2.xls', 'Sheet1')
# R3 = mp.Parametrs(RinDirName + 'Ray_2_3.xls', 'Sheet1')
# R4 = mp.Parametrs(RinDirName + 'Ray_3_4.xls', 'Sheet1')
# R5 = mp.Parametrs(RinDirName + 'Ray_4_5.xls', 'Sheet1')
#-
# mirrorIndex = 'Aperture-morror2'
# plotFileName2 = mainDir + 'result/htmlFiles/Rin_vs_Rout_Section_In_Out_0_1' + '.html'
# plotFileName3 = mainDir + 'result/htmlFiles/Rin_vs_Rout_Section_In_Out_0_2'  + '.html'
# plotFileName4 = mainDir + 'result/htmlFiles/Rin_vs_Rout_Section_In_Out_AA'  + '.html'
#
# Mirror = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, 'Mirror1')  ## mirror List - The name of Sheets in Exel file
# plotObject = Plotpolarization(Mirror.DataSheet, R1.DataSheet, R2.DataSheet, R3.DataSheet, mirrorIndex , plotFileName2)
#
# # rayInDict_markers1, rayOutDict_markers1 = plotObject.setRays4plotR1R2R3Section_markers(R1.DataSheet, R3.DataSheet, 0, 20, 'blue')
# # rayInDict_markers2, rayOutDict_markers2 = plotObject.setRays4plotR1R2R3Section_markers(R1.DataSheet, R3.DataSheet, 21, 41, 'red')
# # rayInDict_markers3, rayOutDict_markers3 = plotObject.setRays4plotR1R2R3Section_markers(R1.DataSheet, R3.DataSheet, 42, 62, 'green')
#
# # rayInDict_markers3, rayOutDict_markers3 = plotObject.setRays4plot_R1_R2_Section_markers(R1.DataSheet, R2.DataSheet, 0, 20, 'green')
# # rayInDict_line3 = plotObject.setRays4plot_R1_R2_Section_Lines(R1.DataSheet,  R2.DataSheet, 0, 20, 'blue')
# # PrayInDict3, PrayOutDict3 = plotObject.setPolRays4Plot_R1_R2_Section_0_1(R1.DataSheet,  R2.DataSheet, 0, 20,)
# # PrayInOutDict3 = plotObject.setPolRays4Plot_R1_R2_Section_direction_0_1(R1.DataSheet, R2.DataSheet, 0, 20,)
#
# #rayInDict_line1 = plotObject.setRays4plotR1R2R3Section_Lines(R1.DataSheet,  R2.DataSheet, 0, 20, 'blue')
# #rayInDict_line2 = plotObject.setRays4plotR1R2R3Section_Lines(R1.DataSheet,  R2.DataSheet, 21, 41, 'red')
#
# # rayInDict_line03 = plotObject.setRays4plot_R1_R3_Section_Lines(R1.DataSheet,  R3.DataSheet, 0, 20, 'blue')
# # rayInDict_markers03, rayOutDict_markers03 = plotObject.setRays4plot_R1_R3_Section_markers(R1.DataSheet, R3.DataSheet, 0, 20, 'green')
# # PrayInDict03, PrayOutDict03 = plotObject.setPolRays4Plot_R1_R3_Section_0_2(R1.DataSheet,  R3.DataSheet, 0, 20,)
# # PrayInOutDict03 = plotObject.setPolRays4Plot_R1_R3_Section_direction_0_2(R1.DataSheet, R3.DataSheet, 0, 20,)
#
# #r1m1, r2m1, r3m1 = plotObject.setRays4plot_R1_R2_R3_Section_markers(R1.DataSheet, R2.DataSheet, R3.DataSheet,  0, 20, 'green')
# r1m1, r2m1, r3m1, r4m1, r5m1 = plotObject.setRays4plot_R1_R2_R3_R4_R5_Section_markers(R1.DataSheet, R2.DataSheet, R3.DataSheet, R4.DataSheet,R5.DataSheet, 0, 20, 'green')
# rl1 = plotObject.setRays4plot_R1_R2_R3_R4_R5_Section_Lines(R1.DataSheet, R2.DataSheet, R3.DataSheet, R4.DataSheet,R5.DataSheet, 0, 20, 'blue')
#
# # rl1 = plotObject.setRays4plot_R1_R2_Section_Lines(R1.DataSheet, R2.DataSheet, 0, 20, 0, 400,'blue')
# # rl2 = plotObject.setRays4plot_R1_R2_Section_Lines(R2.DataSheet, R3.DataSheet, 0, 20, 400, 800,'blue')
# # rl3 = plotObject.setRays4plot_R1_R2_Section_Lines(R3.DataSheet, R4.DataSheet, 0, 20, 800, 1250,'blue')
# # rl4 = plotObject.setRays4plot_R1_R2_Section_Lines(R4.DataSheet, R5.DataSheet, 0, 20, L1, L2,'blue')
# p01, p11, p21, pAA = plotObject.setPolRays4Plot_R1_R2_R3_Section_0_3(R1.DataSheet,  R2.DataSheet, R3.DataSheet, 0, 20,)
# pDirection1 = plotObject.setPolRays4Plot_R1_R2_R3_Section_direction_0_3(R1.DataSheet, R2.DataSheet, R3.DataSheet, 0, 20,)
#
# layout = plotObject.layout
#
# data4Plot=[]
# data4Plot1=[]
# data4Plot2=[]
# data1 = []
#
# # data4Plot.append(rayInDict_markers1)
# # data4Plot.append(rayOutDict_markers1)
# # data4Plot.append(rayInDict_line1)
# #
# # data4Plot.append(rayInDict_markers2)
# # data4Plot.append(rayOutDict_markers2)
# # data4Plot.append(rayInDict_line2)
# #
# # data4Plot.append(rayInDict_markers3)
# # data4Plot.append(rayOutDict_markers3)
# # data4Plot.append(rayInDict_line3)
# # data4Plot.append(PrayInDict3)
# # data4Plot.append(PrayOutDict3)
# # data4Plot.append(PrayInOutDict3)
# #
# # data4Plot1.append(rayInDict_markers03)
# # data4Plot1.append(rayOutDict_markers03)
# # data4Plot1.append(rayInDict_line03)
# # data4Plot1.append(PrayInDict03)
# # data4Plot1.append(PrayOutDict03)
# # data4Plot1.append(PrayInOutDict03)
#
# data4Plot1.append(r1m1)
# data4Plot1.append(r2m1)
# data4Plot1.append(r3m1)
# data4Plot1.append(r4m1)
# data4Plot1.append(r5m1)
# data4Plot2.append(rl1)
# # data4Plot2.append(rl2)
# # data4Plot2.append(rl3)
# # data4Plot2.append(rl4)
#
# #data4Plot1.append(p01)
# #data4Plot1.append(p11)
# #data4Plot1.append(p21)
# #data4Plot1.append(pDirection1)
# data1.append(pAA)
#
# plotObject.plotIs(data4Plot, layout, plotFileName2)
# plotObject.plotIs(data4Plot1, layout, plotFileName3)
# plotObject.plotIs(data4Plot2, layout, plotFileName4)
# #plotObject.plotIs(pAA, layout, plotFileName4)
plotLoop(mirrorList)
#plotLoopPolar(mirrorList)