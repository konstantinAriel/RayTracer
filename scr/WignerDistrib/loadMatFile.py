import scipy.io as sio
import datetime
import numpy as np
import math as m
import plotly as py

import pandas as pd
import plotly.tools as tls
import plotly.graph_objs  as go

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

dataWx = []
dataWz = []
dirPathInDataW = 'C:/Users/konstantinsh/Google Drive/U4eba/Ariel University/TOAR_II/TEZA/RayTracer/files/inDataWxWz/'
modeDir = 'm_1_n_2/'

WxDir = 'wx/'
WyDir = 'wy/'

XinZinMat = sio.loadmat(dirPathInDataW + modeDir + 'xyPoints')
KxKzMat   = sio.loadmat(dirPathInDataW + modeDir + 'KxKyPoints')

Xn = 2
Yn = 2
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
SizeX = 250 # [mm]
SizeZ = 250 # [mm]

xPrime = SizeX / 2
zPrime = SizeZ / 2

xCell = 21
#zCell = 5
zCell = xCell

xLine = xCell+1
zLine = xCell+1

###############################

XinZin  =  XinZinMat['XY']
Xin = (XinZin[:,0])+(SizeX/2)
# print('Xin', Xin)
Zin = ((XinZin[:,1])+(SizeZ/2))
# print('Zin', Zin)
KxKz    =  KxKzMat['KxKy']
Kx = KxKz[:,0]
Kz = KxKz[:,1]

SumWxRe = np.zeros([zCell,xCell])
SumWxIm = np.zeros([zCell,xCell])
SumWzRe = np.zeros([zCell,xCell])
SumWzIm = np.zeros([zCell,xCell])

# print('XY = ',  XinZin)
# print('KxKz = ',   KxKz)
# print('Kx = ',   Kx)
# print('wx = ', Wx)
# print('wY = ', Wz)

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

xLineArray = np.linspace(0, SizeX, xLine)
zLineArray = np.linspace(0, SizeZ, zLine)

xPointArray = np.empty(xCell)
zPointArray = np.empty(zCell)
xCellArray = np.empty(XinSize)
zCellArray = np.empty(ZinSize)

# print(xPointArray)

xVPointDict = []
zVPointDict = []

x0xCenterLine = []
z0zCenterLine = []

x0Dict = []
z0Dict = []

dataPlotDict = []

########################################## Grid Loop #############################################

indexX = 0
xIn = Xin[0:2]
zIn = Zin[0:2]
for Xi in  xIn:
    xCellNum = (m.ceil((Xi/SizeX)*xCell))
    xCellArray[indexX] = xCellNum-1

    indexZ = 0
    for Zi in zIn:
        zCellNum = (m.ceil((Zi / SizeZ) * zCell))
        zCellArray[indexZ] = zCellNum - 1  ## number of ciel

        for Kxi in Kx:
            for Kzi in Kz:
                Lx = 0
                Lz = 0
                keyWxi = 'wx_X_' + str(indexX+1) + '_Y_' + str(indexZ+1)
                WxDicti = WxDict[keyWxi]
                Wxi = WxDicti[xCellNum,zCellNum]

                keyWzi = 'wy_X_' + str(indexX + 1) + '_Y_' + str(indexZ + 1)
                WzDicti = WzDict[keyWzi]
                Wzi = WzDicti[xCellNum, zCellNum]

                SumWxRe[xCellNum, zCellNum] = SumWxRe[xCellNum, zCellNum]+ (Wxi*np.cos(Lx*Kxi))
                SumWxIm[xCellNum, zCellNum] = SumWxIm[xCellNum, zCellNum]+ (Wxi*np.sin(Lx*Kxi))
                SumWzRe[xCellNum, zCellNum] = SumWzRe[xCellNum, zCellNum] + (Wzi*np.cos(Lz*Kzi))
                SumWzIm[xCellNum, zCellNum] = SumWzIm[xCellNum, zCellNum] + (Wzi*np.sin(Lz*Kzi))
        indexZ = indexZ + 1
    indexX = indexX + 1
# print('xCellArray = ')
# print(xCellArray)

# print('zCellArray = ')
# print(xCellArray)

for i in range(xCell):
    xAverage = (xLineArray[i] + xLineArray[i+1])/2
    xPointArray[i] = xAverage
# print('i = ', i)
# print('xArray = ', xPointArray[i])

for j in range(zCell):
    zAverage = (zLineArray[j] + zLineArray[j+1])/2
    zPointArray[j] = zAverage

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

dataPlotDict.append(xzVLines)
dataPlotDict.append(xzGLines)
dataPlotDict.append(xzVPointsDict)
dataPlotDict.append(x0z0xCzCLineDict)

layout = go.Layout(width=1920, height=1200,
                   autosize=True,
                   margin=dict(
                       autoexpand=False),
                   title='Test NET', hovermode='closest',
                   )
fig = dict(data=dataPlotDict, layout=layout)
py.offline.plot(fig, filename = 'testNET.html')

# x = np.array([0,0,0])
# >>> x
# array([0, 0, 0])
# >>> x.fill(np.nan)
##############################################__R_U_N__##############################################


#PlotWxWzSurf()






































