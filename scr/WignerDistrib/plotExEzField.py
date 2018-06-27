import scipy.io as sio
import numpy as np
import plotly as py
import datetime
import plotly.graph_objs  as go

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

now = datetime.datetime.now()
print ('Start -> ', now.hour, ':', now.minute)

a=8
b=16
Linewidth = 1
LinewidthEF = 3
SizeX = 20 # [mm]
SizeZ = 20 # [mm]


dirPathInDataW = 'C:/Users/konstantinsh/Desktop/resultXls/'
dirPathOutData = 'WxWzOut/'
modeDir = 'm_1_n_2/'
WxDir = 'wx/'
WyDir = 'wy/'

matVariable = sio.loadmat(dirPathInDataW + dirPathOutData + 'SumWxWzReImDict')
XinZinMat   = sio.loadmat(dirPathInDataW + modeDir        + 'xyPoints')
KxKzMat     = sio.loadmat(dirPathInDataW + modeDir        + 'KxKyPoints')

SumWxRe     = matVariable['SumWxRe']
SumWxIm     = matVariable['SumWxIm']
SumWzRe     = matVariable['SumWzRe']
SumWzIm     = matVariable['SumWxRe']

xPointArray = matVariable['xPointArray']
zPointArray = matVariable['zPointArray']

xCellArray = matVariable['xCellArray']
zCellArray = matVariable['zCellArray']
xCellSize = xCellArray.size
zCellSize = zCellArray.size
xCell = xPointArray.size
zCell = zPointArray.size
xLine = xCell+1
zLine = xCell+1
print('xCellSize = ', xCellSize)
print('zCellArray = ', zCellArray)
XinZin  =  XinZinMat['XY']
Xin = (XinZin[:,0])
Zin = (XinZin[:,1])

KxKz = KxKzMat['KxKy']
Kx = KxKz[:,0]
Kz = KxKz[:,1]
KxMesh, KzMesh = np.meshgrid(Kx, Kz)

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
WzDataplot = []
WAmplDataplot = []

xPointMesh, zPointMesh = np.meshgrid(xPointArray,zPointArray)

WxMeshDict = dict(
                    go.Surface(x=xPointMesh, y=zPointMesh, z=SumWxRe,
                    showscale = False,
                    opacity = 1,
                    type = 'surface',
                    surfacecolor = 'blue',
                    name = 'SumWxRe'))
WzMeshDict = dict(
                    go.Surface(x=xPointMesh, y=zPointMesh, z=SumWzRe,
                    showscale = False,
                    opacity = 1,
                    type = 'surface',
                    surfacecolor = 'blue',
                    name = 'SumWzRe'))

WxDataplot.append(WxMeshDict)
WzDataplot.append(WzMeshDict)

####################################################  P o i n t s   L o o p  ###############################################
for ii in range(xCell):
    for jj in range(zCell):
        xVi = xPointArray[ii]
        zVj = zPointArray[jj]

        xVPointDict.append(xVi[0])
        zVPointDict.append(zVj[0])
    xVPointDict.append(np.nan)
    zVPointDict.append(np.nan)

xIndex = 0
for x0 in Xin:
    zIndex = 0
    for z0 in Zin:

        iii = int(xCellArray[xIndex])
        jjj = int(zCellArray[zIndex])

        xPi = xPointArray[iii]
        XcenterPoint = xPi[0]
        x0xCenterLine.append(x0)
        x0xCenterLine.append(XcenterPoint)
        x0xCenterLine.append(np.nan)

        zPj = zPointArray[jjj]
        z0zCenterLine.append(z0)
        z0zCenterLine.append(zPj[0])
        z0zCenterLine.append(np.nan)
        zIndex = zIndex + 1
    xIndex = xIndex + 1
Wampl = np.zeros((xPointArray.size,zPointArray.size))
X1Mesh, X2Mesh = np.meshgrid(xPointArray,zPointArray)
xIndex = 0
for x0 in xPointArray:
    zIndex = 0
    for z0 in zPointArray:
        WxRei = SumWxRe[xIndex, zIndex]
        x1 = x0[0]+ WxRei

        x0x1Line.append(x0[0])
        x0x1Line.append(x1)
        x0x1Line.append(np.nan)

        x0x0Line.append(x0[0])
        x0x0Line.append(x0[0])
        x0x0Line.append(np.nan)

        WzRej = SumWzRe[xIndex, zIndex]
        z1 = z0[0]+ WzRej
        z0z1Line.append(z0[0])
        z0z1Line.append(z1)
        z0z1Line.append(np.nan)

        z0z0Line.append(z0[0])
        z0z0Line.append(z0[0])
        z0z0Line.append(np.nan)
        Wampl[xIndex, zIndex] = (WxRei ** 2 + WzRej) ** 0.5

        zIndex = zIndex + 1
    xIndex = xIndex + 1
WamplDict = dict(go.Surface(x=X1Mesh, y=X2Mesh, z=Wampl,
                    showscale = False,
                    opacity = 1,
                    type = 'surface',
                    surfacecolor = 'blue',
                    name = 'SumWxRe'))

WAmplDataplot.append(WamplDict)
##################################### Lines Loop ##############################
xLineArray = np.linspace(-SizeX/2, SizeX/2, xLine)
zLineArray = np.linspace(-SizeZ/2, SizeZ/2, zLine)
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
                  )) # Good
xzGLines = dict(
        go.Scatter(x=xGLineDict, y=zGLineDict,
                  mode='lines',
                  name='G lines NET',
                  line=dict(width=Linewidth, color='red')
                  )) # Good
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
                        name='Electric Field_Total',
                        line=dict(width=LinewidthEF, color='red')
                        ))
x0z0x1z0LineDict =  dict(
                        go.Scatter(x=x0x1Line, y=z0z0Line,
                        mode='Line',
                        name='E Field_Ex',
                        line=dict(width=LinewidthEF, color='blue')
                        ))
x0z0x0z1LineDict =  dict(
                        go.Scatter(x=x0x0Line, y=z0z1Line,
                        mode='Line',
                        name='E Field_Ez',
                        line=dict(width=LinewidthEF, color='blue')
                        ))
dataPlotDict.append(xzVLines)
dataPlotDict.append(xzGLines)
dataPlotDict.append(xzVPointsDict)
dataPlotDict.append(x0z0xCzCLineDict)
dataPlotDict.append(x0z0x1z1LineDict)
dataPlotDict.append(x0z0x1z0LineDict)
dataPlotDict.append(x0z0x0z1LineDict)

layoutDataPlot = go.Layout(width=1920, height=1200,
                   autosize=True,
                   margin=dict(
                    autoexpand=False),
                   title='Electrical Field', hovermode='closest',
                   )

layoutWxDataplot = go.Layout(width=1920, height=1200,
                   autosize=True,
                   margin=dict(
                       autoexpand=False),
                   title='Re_Wx', hovermode='closest',
                   )
layoutWzDataplot = go.Layout(width=1920, height=1200,
                   autosize=True,
                   margin=dict(
                       autoexpand=False),
                   title='Re_Wz', hovermode='closest',
                   )
layoutWamplDataplot = go.Layout(width=1920, height=1200,
                   autosize=True,
                   margin=dict(
                       autoexpand=False),
                   title='W ampl Re', hovermode='closest',
                   )

figDataPlotDict = dict(data=dataPlotDict, layout=layoutDataPlot)
py.offline.plot(figDataPlotDict, filename = 'testNET.html')

figWxDataplot = dict(data=WxDataplot, layout=layoutWxDataplot)
py.offline.plot(figWxDataplot, filename = 'Re_Wx.html')

figWzDataplot = dict(data=WzDataplot, layout=layoutWzDataplot)
py.offline.plot(figWzDataplot, filename = 'Re_Wz.html')

fig = dict(data=WAmplDataplot, layout=layoutWamplDataplot)
py.offline.plot(fig, filename = 'Wampl Re.html')

##############################################__R_U_N__##############################################
#PlotWxWzSurf()
######################################################################################################
now = datetime.datetime.now()
print ('Start -> ', now.hour, ':', now.minute)
