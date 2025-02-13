import plotly as py
import scr.mainParamPakage as mp
from scr.Ploting import PlotingRayTracing
from scr.RayTracing.Rays import  Rays
from scr.MainParam import Parametrs
from scr.Polarization.calcPolarization import calcPolarization
import scr.RayTracing.Rays as rmain

def pathName():
    global mainPath, fExtend, sysParamFname, raysInFname, ray4test3pointFname

    tLine = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, "LineParam")
    sysParam = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend,"SysParam")
    Rin = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.rInDir + mp.raysInFname + mp.fExtend, 'circul10')
    # mainPath = "/home/konstantin/rt/RayTracer/files/XLS/systemSetting"
    # fExtend = '.xls'
    # sysParamFname = 'sysParam'
    # raysInFname = 'RaysIn'
    # raysNormalisedFname = '/home/konstantin/rt/RayTracer/files/XLS/Rin/RaysIn.xls' + raysInFname + '_' + sysParamFname
    ray4test3pointFname = mainPath + 'ray4test3Point_'  + sysParamFname + fExtend
    mirrorSheetName = 'Mirror' + str(int(sysParam.DataSheet.Rin[0]))
    raysSheetName = 'Ray_' + str(int(sysParam.DataSheet.Rin[0] - 1)) + '_' + str(int(sysParam.DataSheet.Rin[0]))
    # print('Rin.DataSheet = IN mainRun')
    # print(Rin.DataSheet)
    mirrorObj = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, 'Mirror1')
    rInObj = rmain.Rays(mirrorObj.DataSheet, Rin.DataSheet, getRefRay=0)  # Create object of Rays

    # raysInDFn = rInObj.RaysDFnormal
    raysInDFn = rInObj.RaysDFnormal
    rOutFname = 'Ray' + '_' + \
                str(int(sysParam.DataSheet.Rin[0] - 1)) + '_' + \
                str(int(sysParam.DataSheet.Rin[0]))
    mirrorList = sysParam.getMirrorList(sysParam.DataSheet)
    raysInDFn.to_excel(mp.mainPath + mp.xlsDir + mp.rOutDir + rOutFname + mp.fExtend)

def mirrorLoop(mirrorDictMain):
    for mirrorDictSub in mirrorDictMain.keys():
        #print(sys.dataSheet.Rin[0])
        countMirror = int(sys.dataSheet.Rin[0])
        for mirrorList in mirrorDictMain.get(mirrorDictSub):
            print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',  mirrorList)

            Mirror = sys.getParam(sys.paramFile, mirrorList)  ## mirror List - The name of Sheets in Exel file
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                          'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            print(raysFName)
            RaysInDF = Parametrs(mainPath + raysFName[0] + fExtend, 'Sheet1').dataSheet
            RaysNormalDF = Parametrs(mainPath + raysFName[2] + fExtend, 'Sheet1').dataSheet

            print('RaysInDF = ')
            print(RaysInDF)
            print('RaysNormalDF = ')
            print(RaysNormalDF)

            for index in RaysInDF.index:
                print('_____________________________________________' ,index )
                print('RaysInDF[index] = ')
                print(RaysInDF.loc[index, :])
                print('RaysNormalDF[index] = ',)
                print(RaysNormalDF.loc[index, :])
                print('____________________________________________')
                # rayIn = RaysInDF[index,:]
                # normalray = RaysNormalDF[index,:]
                pObject = calcPolarization(RaysInDF.loc[index, :], RaysNormalDF.loc[index,:])
                kRef, xRefArray = pObject.getReflectedPolarRay(pObject.kArray, pObject.nArray)

                print(xRefArray)
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
            plotObject = PlotingRayTracing(path, mirrorObject.dataSheet, mirrorList)

            surfR = plotObject.setMirrorSurf

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

pathName()

 ################################################################ for Standard RUN ################
#=============   Read  Excel file with Rays Data in =========================
tLine = Parametrs(mainPath+sysParamFname + fExtend, "LineParam")
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
# Rin = Parametrs(mainPath + raysInFname + fExtend, "Rin")
Rin = Parametrs('/home/konstantin/rt/RayTracer/files/XLS/Rin/RaysIn.xls', "Xin")
RinDF = Rin.dataSheet
raysSheetName0 = 'Ray_' + str(int(sys.dataSheet.Rin[0] - 1)) + '_' + str(int(sys.dataSheet.Rin[0]))
  # Create object of Rays

#=============  Normilise Rin for Mirror  ===================================
mirror1SheetName = 'Mirror' + str(int(sys.dataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath+sysParamFname + fExtend, 'Mirror1')
mirrorDF = mirrorObject.dataSheet
# save to Excel

rInObject = Rays(mirrorDF, RinDF, 0)
RinNormalize = rInObject.RaysDFnormal
rInObject.saveRays2Execel(mainPath + 'Ray'+'_' +
                          str(int(sys.dataSheet.Rin[0]-1)) + '_' +
                          str(int(sys.dataSheet.Rin[0]))
                          + fExtend,
                          RinNormalize)

#==============  Get List of Section for calculation ========================#
mirrorDictMain = sys.getMirrorList(sys.dataSheet)

#=============== Ray Tracing =================================================#
mirrorLoop(mirrorDictMain)

#=============== Plotting ====================================================
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
plotLoop(mirrorDictMain)

