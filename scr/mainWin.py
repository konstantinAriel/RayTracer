import scipy.io as sio
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
    global mainPath, fExtend, matExtend, sysParamFname, raysInFname, ray4test3pointFname, RayPath,RinPath, RnormalPath, htmlDir, htmlFN
    mainPath = "C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/XLS/systemSetting/"
    RayPath = "C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/XLS/m_0_n_1/"
    RinPath         = 'Rin/'
    RnormalPath     = 'RNormal/'
    fExtend         = '.xls'
    matExtend       = '.mat'
    sysParamFname   = 'sysParam'
    raysInFname     = 'RaysIn'
    htmlDir = RayPath + 'htmlDir/'
    htmlFN = 'RayTracing.html'
    raysNormalisedFname = mainPath + 'raysNormalised_'
    ray4test3pointFname = mainPath + 'ray4test3Point_'  + sysParamFname + fExtend

def getDFromMAT(rInPath):
    rayInMatS = sio.loadmat(rInPath)
    rayInS = rayInMatS['struct']
    Xs = rayInS['X']
    Ys = rayInS['Y']
    Zs = rayInS['Z']
    Kxs = rayInS['Kx']
    Kys = rayInS['Ky']
    Kzs = rayInS['Kz']
    Exs = rayInS['Ex']
    Eys = rayInS['Ey']
    Ezs = rayInS['Ez']
    # Hxs = rayInS['Hx']
    # Hys = rayInS['Hy']
    # Hzs = rayInS['Hz']

    X0 = Xs[0]
    Y0 = Ys[0]
    Z0 = Zs[0]
    Kx0 = Kxs[0]
    Ky0 = Kys[0]
    Kz0 = Kzs[0]
    Ex0 = Exs[0]
    Ey0 = Eys[0]
    Ez0 = Ezs[0]
    # Hx0 =Hxs[0]
    # Hy0 =Hys[0]
    # Hz0 =Hzs[0]

    X00 = X0[0]
    Y00 = Y0[0]
    Z00 = Z0[0]
    Kx00 = Kx0[0]
    Ky00 = Ky0[0]
    Kz00 = Kz0[0]
    Ex00 = Ex0[0]
    Ey00 = Ey0[0]
    Ez00 = Ez0[0]

    X000 = X00[:, 0]
    Y000 = Y00[:, 0]
    Z000 = Z00[:, 0]
    Kx000 = Kx00[:, 0]
    Ky000 = Ky00[:, 0]
    Kz000 = Kz00[:, 0]
    Ex000 = Ex00[:, 0]
    Ey000 = Ey00[:, 0]
    Ez000 = Ez00[:, 0]
    # Hx00 = Hx0[0]
    # Hy00 = Hy0[0]
    # Hz00 = Hz0[0]

    RinDF = pd.DataFrame({'X': X000,
                          'Y': Y000,
                          'Z': Z000,
                          'Kx': Kx000,
                          'Ky': Ky000,
                          'Kz': Kz000,
                          'Ex': Ex000,
                          'Ey': Ey000,
                          'Ez': Ez000,
                          # 'Hx':Hx00,
                          # 'Hy':Hy00,
                          # 'Hz':Hz00,
                          })
    return  RinDF


def mirrorLoop(mirrorList):
    countMirror = int(sysParam.DataSheet.Rin[0])
    for mirrorIndex in mirrorList:
        print( ' ++++++++++++++++++++++++++++++++++++++++++++++++++++++  Mirror Loop  ',mirrorIndex)
        MirrorDF = sys.getParam(sys.paramFile, mirrorIndex)  ## mirror List - The name of Sheets in Exel file

        raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                    'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                    'normalRay_' + str(countMirror) + '_' + str(countMirror)]

        rInPath     = 'C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/XLS/m_0_n_1/Rin/'     + raysFName[0]
        rOutPath    = 'C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/XLS/m_0_n_1/Rin/'     + raysFName[1]
        rNormalPath = 'C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/XLS/m_0_n_1/RNormal/' + raysFName[2]
        XpLaneLinePath = 'C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/XLS/m_0_n_1/Rout/' + raysFName[2]
        RinDF = getDFromMAT(rInPath)

        RaysObject = rmain.Rays(MirrorDF, RinDF, getRefRay = 1)
        RayRefDF = RaysObject.ReflectedRayDF
        RayNormalDF = RaysObject.NormalRayDF
        xPleneLineRaysDF = RaysObject.xPleneLineRaysDF
        sio.savemat(rOutPath,
                    {'struct': RayRefDF.to_dict("list")},
                    appendmat=True, format='5', long_field_names=False, do_compression=False, oned_as='column')
        sio.savemat(rNormalPath,
                    {'struct': RayNormalDF.to_dict("list")},
                    appendmat=True, format='5', long_field_names=False, do_compression=False, oned_as='column')
        sio.savemat(XpLaneLinePath,
                    {'struct': xPleneLineRaysDF.to_dict("list")},
                    appendmat=True, format='5', long_field_names=False, do_compression=False, oned_as='column')
        countMirror += 1

    print(' +++++++++++++++++++++++++++++++++++++++++++          END Mirror Loop  ---->  ',  mirrorList)

def plotLoop(mirrorList):
    # print(' ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Plot Loop         ',countMirror)
    # countMirror = int(sys.dataSheet.Rin[0])
    countMirror = 1
    fileName = htmlDir + htmlFN
    dataRays = []
    for mirrorIndex in mirrorList:
        mirrorObject = Parametrs(mainPath + sysParamFname + fExtend, mirrorList)  ## mirror List - The name of Sheets in Exel file
        mirrorDataSheet = mirrorObject.dataSheet
        mirrorDF = mirrorDataSheet[mirrorIndex]
        raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                     'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                     'normalRay_' + str(countMirror) + '_' + str(countMirror)]

        rInPath  = RayPath + RinPath + raysFName[0]
        rOutPath = RayPath + RinPath + raysFName[1]
        rNormalPath = RayPath + RnormalPath + raysFName[2]

        RinDF = getDFromMAT(rInPath)
        RrefDF = getDFromMAT(rOutPath)
        RnDF = getDFromMAT(rNormalPath)

        plotObject = PlotingRayTracing(mirrorDF, mirrorIndex, RinDF, RrefDF, RnDF, fileName)

        surfR = plotObject.setMirrorSurf()

        dataRays.append(plotObject.rayInDict)
        dataRays.append(plotObject.rayReflectedDict)
        dataRays.append(surfR)
        countMirror += 1
    dataRays.append(plotObject.Tline1)
    dataRays.append(plotObject.Tline2)
    layout = plotObject.layout

    fig1 = dict(data=dataRays, layout=layout)
    py.offline.plot(fig1, filename=fileName)

#######################################################################################################
#                                                                                                     #
#                                                                                                     #
#                      P R O G R A M M    I S   R U N N I N G  F R O M    H E R E                    #
#                                                                                                     #
#                                                                                                     #
#######################################################################################################

pathName()

 ########  for Standard RUN ################
#=============   Read  Excel file with Rays Data in =========================

tLine = Parametrs(mainPath+sysParamFname + fExtend, "LineParam")
sysParam = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, "SysParam")

# #   C H O O S E   F I L E    W I T H   RAYS_in
dirPathInData = 'C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/XLS/'
modeDir = 'm_0_n_1/'
RinMat = sio.loadmat(dirPathInData + modeDir + 'RayInA')
RinArr = RinMat['rayIn']

raysIn0 = 'Ray_' + str(int(sysParam.DataSheet.Rin[0] - 1)) + '_' + str(int(sysParam.DataSheet.Rin[0]))  # Ray_0_1

##=============  Normilise Rin for Mirror  ===================================
mirror1SheetName = 'Mirror' + str(int(sysParam.DataSheet.Rin[0]))
mirrorObject = Parametrs(mainPath+sysParamFname + fExtend, 'Mirror1')
rOutFname ='Ray'+'_' + \
           str(int(sysParam.DataSheet.Rin[0]-1)) + '_' + \
           str(int(sysParam.DataSheet.Rin[0]))
rNormalFname = 'Ray'+'_' + \
           str(int(sysParam.DataSheet.Rin[0]-1)) + '_' + \
           str(int(sysParam.DataSheet.Rin[0]-1))
RinDF = pd.DataFrame({  'X'  : RinArr[:,0],
                        'Y'  : RinArr[:,1],
                        'Z'  : RinArr[:,2],
                        'Kx' : RinArr[:,3],
                        'Ky' : RinArr[:,4],
                        'Kz' : RinArr[:,5],
                        'Ex' : RinArr[:,6],
                        'Ey' : RinArr[:,7],
                        'Ez' : RinArr[:,8],
                        'Hx' : RinArr[:,9],
                        'Hy' : RinArr[:,10],
                        'Hz' : RinArr[:,11],
                      })
rInObject = rmain.Rays(mirrorObject.dataSheet, RinDF, getRefRay = 0)  # Create object of Rays
raysInDFn = rInObject.RaysDFnormal
# raysInDFn.to_excel(mp.mainPath + mp.xlsDir + mp.rOutDir  + rOutFname + mp.fExtend)
path2NormalRay = 'C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/XLS/m_0_n_1/Rin/' + raysIn0
sio.savemat(path2NormalRay,
            {'struct':raysInDFn.to_dict("list")},
            appendmat=True, format='5', long_field_names=False, do_compression=False, oned_as='column')
##==============  Get List of Section for calculation ========================#
mirrorDictMain = sysParam.getMirrorList(sysParam.DataSheet)
sys = Parametrs(mainPath+sysParamFname + fExtend, "SysParam")

##=============== Ray Tracing =================================================#
mirrorLoop(mirrorDictMain)
# #=============== Plotting ====================================================
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
plotLoop(mirrorDictMain)

