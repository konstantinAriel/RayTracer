import scipy.io as sio
import datetime
import numpy as np
import math as m
import pandas as pd
import plotly as py
import plotly.tools as tls
import plotly.graph_objs  as go

tls.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

now = datetime.datetime.now()
print ('Start -> ', now.hour, ':', now.minute)

dataWx = []
dataWz = []
# dirPathInDataW = 'C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/inDataWxWz/'
dirPathInDataW = 'C:/Users/konstantinsh/Desktop/resultXls/'
modeDir = 'm_1_n_2/'

WxDir = 'wx/'
WyDir = 'wy/'

XinZinMat = sio.loadmat(dirPathInDataW + modeDir + 'xyPoints')
KxKzMat   = sio.loadmat(dirPathInDataW + modeDir + 'KxKyPoints')

Xn = 100
Yn = 100

WxDict = {}
WzDict = {}
keyWxArr = np.empty(Xn)
keyWzArr = np.empty(Yn)

for X in range(Xn):
    for Y in range(Yn):
        keyWx = 'wx_X_' + str(X+1) + '_Y_' + str(Y+1)
        keyWz = 'wy_X_' + str(X+1) + '_Y_' + str(Y+1)
        wXMat = sio.loadmat(dirPathInDataW + modeDir + WxDir + keyWx)
        wZMat = sio.loadmat(dirPathInDataW + modeDir + WyDir + keyWz)
        Wx = wXMat['wX_xyKxKy_TM']
        Wz = wZMat['wY_xyKxKy_TM']
        WxDict[keyWx] = Wx
        WzDict[keyWz] = Wz

########################### Constants #########################################

a=8
b=16

Linewidth = 0.5
SizeX = 20 # [mm]
SizeZ = 20 # [mm]

xPrime = SizeX/2
zPrime = SizeZ/2

xCell = 101
zCell = xCell

xLine = xCell+1
zLine = xCell+1

###############################

XinZin  =  XinZinMat['XY']
# Xin = (XinZin[:,0])+(SizeX/2)
# Zin = ((XinZin[:,1]))
Xin = (XinZin[:,0])
Zin = ((XinZin[:,1]))
KxKz    =  KxKzMat['KxKy']
Kx = KxKz[:,0]
Kz = KxKz[:,1]

SumWxRe = np.zeros([xCell,zCell])
SumWxIm = np.zeros([xCell,zCell])
SumWzRe = np.zeros([xCell,zCell])
SumWzIm = np.zeros([xCell,zCell])
KxMesh, KzMesh = np.meshgrid(Kx, Kz)


def PlotWxWzSurf():
    SurfDictWx = dict(go.Surface(x=KxMesh, y=KzMesh, z=Wx,
                                 showscale=False,
                                 opacity=1,
                                 type='surface',
                                 surfacecolor='blue',
                                 name=str("W_X")
                                 )
                      )
    SurfDictWz = dict(go.Surface(x=KxMesh, y=KzMesh, z=Wz,
                                 showscale=False,
                                 opacity=1,
                                 type='surface',
                                 surfacecolor='blue',
                                 name=str("W_X")
                                 )
                      )
    dataWx.append(SurfDictWx)
    dataWz.append(SurfDictWx)
    layout = go.Layout(width=1920, height=1200,
                       autosize=False,
                       margin=dict(
                           autoexpand=False),
                       title='Wigler Wx ', hovermode='closest',
                       )
    filenameHtmlWx = '/home/konstantin/rt/RayTracer/files/result/htmlFiles/Wigler_distrib/Wx.html'
    filenameHtmlWz = '/home/konstantin/rt/RayTracer/files/result/htmlFiles/Wigler_distrib/Wz.html'
    fig = dict(data=dataWx, layout=layout)
    fig = dict(data=dataWz, layout=layout)
    py.offline.plot(fig, filename=filenameHtmlWx)
    py.offline.plot(fig, filename=filenameHtmlWz)

##  Get grid  #################################################################################

XinSize = len(Xin)
ZinSize = len(Zin)

# xLineArray = np.linspace(0, SizeX, xLine)
# zLineArray = np.linspace(0, SizeZ, zLine)
xLineArray = np.linspace(-SizeX/2, SizeX/2, xLine)
zLineArray = np.linspace(-SizeZ/2, SizeZ/2, zLine)

xPointArray = np.empty(xCell)
zPointArray = np.empty(zCell)
xCellArray = np.empty(XinSize)
zCellArray = np.empty(ZinSize)

# print(xPointArray)

xVPointDict = []
zVPointDict = []

x0xCenterLine = []
z0zCenterLine = []

x0x1Line = []
z0z1Line = []
x0x0Line = []
z0z0Line = []
x0Dict = []
z0Dict = []

dataPlotDict = []
WxDataplot = []
WAmplDataplot = []
########################################## Grid Loop #############################################
for i in range(xCell):
    xAverage = (xLineArray[i] + xLineArray[i+1])/2
    xPointArray[i] = xAverage
# print('i = ', i)
# print('xArray = ', xPointArray[i])

for j in range(zCell):
    zAverage = (zLineArray[j] + zLineArray[j+1])/2
    zPointArray[j] = zAverage
########################################  LOOP FOR CALCULATE  ELECTRICAL FIELD ###################################
indexX = 0
for Xi in  Xin:
    xCellNum = ((m.ceil(((Xi+SizeX/2)/SizeX)*xCell)))-1
    xCellArray[indexX] = xCellNum
    indexZ = 0
    for Zi in Zin:
        zCellNum = ((m.ceil(((Zi+SizeZ/2) / SizeZ) * zCell)))-1
        zCellArray[indexZ] = zCellNum  ## number of ciel
        Kxindex=0
        for Kxi in Kx:
            Kzindex = 0
            for Kzi in Kz:
                Lx = 0
                Lz = 0
                keyWxi = 'wx_X_' + str(indexX+1) + '_Y_' + str(indexZ+1)
                WxDicti = WxDict[keyWxi]
                Wxi = WxDicti[Kxindex,Kzindex]

                keyWzi = 'wy_X_' + str(indexX + 1) + '_Y_' + str(indexZ + 1)
                WzDicti = WzDict[keyWzi]
                Wzi = WzDicti[Kxindex, Kzindex]

                SumWxRe[xCellNum, zCellNum] = SumWxRe[xCellNum, zCellNum] + (Wxi*np.cos(Lx*Kxi))
                SumWxIm[xCellNum, zCellNum] = SumWxIm[xCellNum, zCellNum] + (Wxi*np.sin(Lx*Kxi))
                SumWzRe[xCellNum, zCellNum] = SumWzRe[xCellNum, zCellNum] + (Wzi*np.cos(Lz*Kzi))
                SumWzIm[xCellNum, zCellNum] = SumWzIm[xCellNum, zCellNum] + (Wzi*np.sin(Lz*Kzi))
                Kzindex = Kzindex+1
            Kxindex = Kxindex+1
        indexZ = indexZ + 1
    indexX = indexX + 1

##########################################################################################################################
# print('xCellArray = ')
# print(xCellArray)
#
# print('zCellArray = ')
# print(xCellArray)

#####################################   Save to MAT File #################################################################
sio.savemat('C:/Users/konstantinsh/Desktop/resultXls//WxWzOut/SumWxWzReImDict',
            {'SumWxRe':SumWxRe,
             'SumWxIm':SumWxIm,
             'SumWzRe':SumWzRe,
             'SumWzIm':SumWzIm,
             'zPointArray':zPointArray,
             'xPointArray':xPointArray,
             'xCellArray':xCellArray,
             'zCellArray':zCellArray,
             },
            appendmat=True, format='5', long_field_names=False, do_compression=False, oned_as='column')
X1Mesh, X2Mesh = np.meshgrid(xPointArray,zPointArray)

WxMeshDict = dict(
                    go.Surface(x=X1Mesh, y=X2Mesh, z=SumWxRe,
                    showscale = False,
                    opacity = 1,
                    type = 'surface',
                    surfacecolor = 'blue',
                    name = 'SumWxRe'))
WxDataplot.append(WxMeshDict)
################################  Points Loop ###############################

for ii in range(xCell):
    for jj in range(zCell):
        xVPointDict.append(xPointArray[ii])
        zVPointDict.append(zPointArray[jj])
    xVPointDict.append(np.nan)
    zVPointDict.append(np.nan)
xIndex = 0
for x0 in Xin:
    zIndex = 0
    for z0 in Zin:
        iii = int(xCellArray[xIndex])
        jjj = int(zCellArray[zIndex])

        XcenterPoint = xPointArray[iii]
        x0xCenterLine.append(x0)
        x0xCenterLine.append(XcenterPoint)
        x0xCenterLine.append(np.nan)

        zCenterPoint = zPointArray[jjj]
        z0zCenterLine.append(z0)
        z0zCenterLine.append(zCenterPoint)
        z0zCenterLine.append(np.nan)
        zIndex = zIndex + 1
    xIndex = xIndex + 1
Wampl = np.zeros((xPointArray.size,zPointArray.size))
xIndex = 0
for x0 in xPointArray:
    zIndex = 0
    for z0 in zPointArray:
        # iii = int(xCellArray[xIndex])
        # jjj = int(zCellArray[zIndex])

        # XcenterPoint = xPointArray[iii]
        x01 = SumWxRe[xIndex, zIndex]
        x1 = x0+x01
        x0x1Line.append(x0)
        x0x1Line.append(x1)
        x0x1Line.append(np.nan)

        x0x0Line.append(x0)
        x0x0Line.append(x0)
        x0x0Line.append(np.nan)

        #zCenterPoint = zPointArray[jjj]
        z01 = SumWzRe[xIndex,zIndex]
        z1 = z0+z01
        z0z1Line.append(z0)
        z0z1Line.append(z1)
        z0z1Line.append(np.nan)

        z0z0Line.append(z0)
        z0z0Line.append(z0)
        z0z0Line.append(np.nan)
        Wampl[xIndex,zIndex] = (x1**2+z1)**0.5
        zIndex = zIndex + 1
    xIndex = xIndex + 1
WamplDict = dict(
                    go.Surface(x=X1Mesh, y=X2Mesh, z=Wampl,
                    showscale = False,
                    opacity = 1,
                    type = 'surface',
                    surfacecolor = 'blue',
                    name = 'SumWxRe'))
WAmplDataplot.append(WxMeshDict)
##################################### Lines Loop ##############################

xVLineDict = []
zVLineDict = []
xGLineDict = []
zGLineDict = []

for k in range(xLine):
    for l in range(zLine):
        xVLineDict.append(xLineArray[k])
        zVLineDict.append(xLineArray[l])

        xGLineDict.append(xLineArray[l])
        zGLineDict.append(xLineArray[k])

    xVLineDict.append(np.nan)
    zVLineDict.append(np.nan)
    xGLineDict.append(np.nan)
    zGLineDict.append(np.nan)

#####################################################################################################
xzVLines = dict(
        go.Scatter(x=xVLineDict, y=zVLineDict,
                  mode='lines',
                  name='V lines NET',
                  line=dict(width=Linewidth, color='blue')
                  ))
xzGLines = dict(
        go.Scatter(x=xGLineDict, y=zGLineDict,
                  mode='lines',
                  name='G lines NET',
                  line=dict(width=Linewidth, color='red')
                  ))
xzVPointsDict = dict(
        go.Scatter(x=xVPointDict, y=zVPointDict,
                  mode='markers',
                  name='V markers NET',
                  line=dict(width=Linewidth, color='black')
                  ))
x0z0xCzCLineDict =  dict(
                        go.Scatter(x=x0xCenterLine, y=z0zCenterLine,
                        mode='Line',
                        name='find cell',
                        line=dict(width=Linewidth, color='green')
                        ))
x0z0x1z1LineDict =  dict(
                        go.Scatter(x=x0x1Line, y=z0z1Line,
                        mode='Line',
                        name='Electricasl Field_ Total',
                        line=dict(width=Linewidth, color='green')
                        ))
x0z0x1z0LineDict =  dict(
                        go.Scatter(x=x0x1Line, y=z0z0Line,
                        mode='Line',
                        name='Electricasl Field _Ex',
                        line=dict(width=Linewidth, color='green')
                        ))

x0z0x0z1LineDict =  dict(
                        go.Scatter(x=x0x0Line, y=z0z1Line,
                        mode='Line',
                        name='Electricasl Field',
                        line=dict(width=Linewidth, color='green')
                        ))
dataPlotDict.append(xzVLines)
dataPlotDict.append(xzGLines)
dataPlotDict.append(x0z0xCzCLineDict)
dataPlotDict.append(xzVPointsDict)

dataPlotDict.append(x0z0x1z1LineDict)
dataPlotDict.append(x0z0x1z0LineDict)
dataPlotDict.append(x0z0x0z1LineDict)

layout = go.Layout(width=1920, height=1200,
                   autosize=True,
                   margin=dict(
                       autoexpand=False),
                   title='Test NET', hovermode='closest',
                   )
fig = dict(data=dataPlotDict, layout=layout)
py.offline.plot(fig, filename = 'testNET.html')

fig = dict(data=WxDataplot, layout=layout)
py.offline.plot(fig, filename = 'testSum Wx Re.html')

fig = dict(data=WAmplDataplot, layout=layout)
py.offline.plot(fig, filename = 'Wampl Re.html')

# x = np.array([0,0,0])
# >>> x
# array([0, 0, 0])
# >>> x.fill(np.nan)
##############################################__R_U_N__##############################################
#PlotWxWzSurf()

now = datetime.datetime.now()
print ('Start -> ', now.hour, ':', now.minute)
