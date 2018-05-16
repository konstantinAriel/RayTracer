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
dirPathInDataW = '/home/konstantin/rt/RayTracer/files/inDataWxWz/'
modeDir = 'm_1_n_2/'

WxDir = 'wx/'
WyDir = 'wy/'

XinZinMat   = sio.loadmat(dirPathInDataW + modeDir + 'xyPoints')
KxKzMat     = sio.loadmat(dirPathInDataW + modeDir + 'KxKyPoints')
wXMat       = sio.loadmat(dirPathInDataW + modeDir + WxDir + 'wx_X_1_Y_ 1' )
wZMat       = sio.loadmat(dirPathInDataW + modeDir + WyDir + 'wy_X_1_Y_ 1')

###########################  Constants #########################################

a=8
b=16

Linewidth = 0.5
SizeX = 250 # [mm]
SizeZ = 250 # [mm]

xPrime = SizeX / 2
zPrime = SizeZ / 2

xCell = 10
# zCell = 5
zCell = xCell

xLine = xCell+1
zLine = xCell+1

###############################

XinZin  =  XinZinMat['XY']
Xin = XinZin[:,0]+(SizeX/2)
Zin = XinZin[:,1]+(SizeZ/2)
KxKz    =  KxKzMat['KxKy']
Kx = KxKz[:,0]
Kz = KxKz[:,1]
Wx      =  wXMat['wX_xyKxKy_TM']
Wz      =  wZMat['wY_xyKxKy_TM']

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
    filenameHtmlWz = '/home/konstantin/rt/RayTracer/files/result/htmlFiles/Wigler_distrib/WzX.html'
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

print(xPointArray)


xVPointDict = []
zVPointDict = []
xGPointDict = []
zGPointDict = []
dataPlotDict = []

########################################## Grid Loop #############################################

index = 0
for X in  Xin:
    xCellNum = (m.ceil((X/SizeX)*xCell))
    xCellArray[index] = xCellNum-1
    index = index+1
    print('xCellArray = ')
    print(xCellArray)

for i in range(xCell):
    xAverage = (xLineArray[i] + xLineArray[i+1])/2
    xPointArray[i] = xAverage
    print('i = ', i)
    print('xArray = ', xPointArray[i])

for j in range(zCell):
    zAverage = (zLineArray[j] + zLineArray[j+1])/2
    zPointArray[j] = zAverage

################################  Points Loop ###############################

for ii in range(xCell):
    for jj in range(zCell):
        xVPointDict.append(xPointArray[ii])
        zVPointDict.append(zPointArray[jj])
                           
        # xGPointDict.append(xPointArray[jj])
        # zGPointDict.append(zPointArray[ii])

    xVPointDict.append(np.nan)
    zVPointDict.append(np.nan)
    # xGPointDict.append(np.nan)
    # zGPointDict.append(np.nan)

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
# xzGPointsDict = dict(
#         go.Scatter(x=xGPointDict, y=zGPointDict,
#                   mode='markers',
#                   name='V markers NET',
#                   line=dict(width=Linewidth, color='black')
#                   ))
dataPlotDict.append(xzVLines)
dataPlotDict.append(xzGLines)
dataPlotDict.append(xzVPointsDict)
# dataPlotDict.append(xzGPointsDict)


layout = go.Layout(width=1920, height=1200,
                   autosize=True,
                   margin=dict(
                       autoexpand=False),
                   title='Test NET', hovermode='closest',
                   )
fig = dict(data=dataPlotDict, layout=layout)
py.offline.plot(fig, filename='testNET.html')
# x = np.array([0,0,0])
# >>> x
# array([0, 0, 0])
# >>> x.fill(np.nan)



##############################################__R_U_N__##############################################


#PlotWxWzSurf()






































