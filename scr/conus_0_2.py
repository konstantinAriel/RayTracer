import pandas as pd
import numpy as np

import plotly as py
import plotly.tools as tls
import plotly.graph_objs  as go
import plotly.figure_factory as ff

from scr.MainParam import Parametrs
from scr.Rays import Rays

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
pathIn = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/RaysIn.xls'
pathOut = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/Ray_2_3.xls'
pathNormal = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/normalRay_1_1.xls'
paramFileIn = pd.ExcelFile(pathIn)
paramFileOut = pd.ExcelFile(pathOut)
paramFileNormal = pd.ExcelFile(pathNormal)
dataSheetIn = paramFileIn.parse(sheetname ='circul')
dataSheetOut = paramFileOut.parse(sheetname ='Sheet1')
dF  = paramFileNormal.parse(sheetname ='Sheet1')
print(dF)
t=200
data1 = []
data2 = []
data3 =[]
data4 =[]
rayInDict = []
rayOutDict = []
Xin = dataSheetIn.Xin
Yin = dataSheetIn.Yin
Zin = dataSheetIn.Zin

KxIn = dataSheetIn.Kxin
KyIn = dataSheetIn.Kyin
KzIn = dataSheetIn.Kzin

Nx = dF.Kxin
Ny = dF.Kyin
Nz = dF.Kzin

Exin = dataSheetIn.Exin
Eyin = dataSheetIn.Eyin
Ezin = dataSheetIn.Ezin
Ain = dataSheetIn.Ain

XeIn = Xin + Ain*Exin
YeIn = Yin + Ain*Eyin
ZeIn = Zin + Ain*Ezin

Xout = dataSheetOut.Xin
Yout = dataSheetOut.Yin
Zout = dataSheetOut.Zin
KxOut = dataSheetOut.Kxin
KyOut = dataSheetOut.Kyin
KzOut = dataSheetOut.Kzin

ExOut = dataSheetOut.Exin
EyOut = dataSheetOut.Eyin
EzOut = dataSheetOut.Exin

XeOut = Xout + Ain*ExOut
YeOut = 200 + Ain*EyOut
ZeOut = Zout + Ain*EzOut

Xin1 = Xin + KxIn * t
Yin1 = Yin + KyIn * t
Zin1 = Zin + KzIn * t

x1RayInData = []
y1RayInData = []
z1RayInData = []

x1RayData = []
y1RayData = []
z1RayData = []

x2RayInData = []
y2RayInData = []
z2RayInData = []

x2RayData = []
y2RayData = []
z2RayData = []

x3RayInData = []
y3RayInData = []
z3RayInData = []

x3RayData = []
y3RayData = []
z3RayData = []

x4RayData = []
y4RayData = []
z4RayData = []


xRayReflectedData = []
yRayReflectedData = []
zRayReflectedData = []

XpolarDataIn1 = []
YpolarDataIn1 = []
ZpolarDataIn1 = []

XpolarDataIn2 = []
YpolarDataIn2 = []
ZpolarDataIn2 = []

XpolarDataIn3 = []
YpolarDataIn3 = []
ZpolarDataIn3 = []

XpolarDataOut1 = []
YpolarDataOut1 = []
ZpolarDataOut1 = []

XpolarDataOut2 = []
YpolarDataOut2 = []
ZpolarDataOut2 = []

XpolarDataOut3 = []
YpolarDataOut3 = []
ZpolarDataOut3 = []

XinPoint1 = []
YinPoint1 = []
ZinPoint1 = []

XinPoint2 = []
YinPoint2 = []
ZinPoint2 = []

XinPoint3 = []
YinPoint3 = []
ZinPoint3 = []

XoutPoint1 = []
YoutPoint1 = []
ZoutPoint1 = []

XoutPoint2 = []
YoutPoint2 = []
ZoutPoint2 = []

XoutPoint3 = []
YoutPoint3 = []
ZoutPoint3 = []

XxpolarDataIn1 = []
XzpolarDataIn1 = []
ZzpolarDataIn1 = []
ZxpolarDataIn1 = []

XxpolarDataIn2 = []
XzpolarDataIn2 = []
ZzpolarDataIn2 = []
ZxpolarDataIn2 = []

XxpolarDataIn3 = []
XzpolarDataIn3 = []
ZzpolarDataIn3 = []
ZxpolarDataIn3 = []

XxpolarDataOut1 = []
XzpolarDataOut1 = []
ZxpolarDataOut1 = []
ZzpolarDataOut1 = []

XxpolarDataOut2 = []
XzpolarDataOut2 = []
ZxpolarDataOut2 = []
ZzpolarDataOut2 = []

XxpolarDataOut3 = []
XzpolarDataOut3 = []
ZxpolarDataOut3 = []
ZzpolarDataOut3 = []

for i in range(0,19):
    print(i)
    #  In DATA
    x1RayInData.append(Xin[i])
    x1RayInData.append(Xin1[i])
    x1RayInData.append(np.nan)

    y1RayInData.append(Yin[i])
    y1RayInData.append(Yin1[i])
    y1RayInData.append(np.nan)

    z1RayInData.append(Zin[i])
    z1RayInData.append(Zin1[i])
    z1RayInData.append(np.nan)

conus1Dict = dict(
        go.Scatter3d(x=x1RayInData, y=y1RayInData, z=z1RayInData,
                     mode='marker',
                     name='rayInParalel',
                     line=dict(width=1, color='green')
                     ))

for i in range(20,39):
    #  In DATA
    x2RayInData.append(Xin[i])
    x2RayInData.append(Xin1[i])
    x2RayInData.append(np.nan)

    y2RayInData.append(Yin[i])
    y2RayInData.append(Yin1[i])
    y2RayInData.append(np.nan)

    z2RayInData.append(Zin[i])
    z2RayInData.append(Zin1[i])
    z2RayInData.append(np.nan)


conus2Dict = dict(
        go.Scatter3d(x=x2RayInData, y=y2RayInData, z=z2RayInData,
                     mode='marker',
                     name='ray2',
                     line=dict(width=1, color='red')
                     ))

for i in range(40, 59):
    #  In DATA
    x3RayInData.append(Xin[i])
    x3RayInData.append(Xin1[i])
    x3RayInData.append(np.nan)

    y3RayInData.append(Yin[i])
    y3RayInData.append(Yin1[i])
    y3RayInData.append(np.nan)

    z3RayInData.append(Zin[i])
    z3RayInData.append(Zin1[i])
    z3RayInData.append(np.nan)

conus3Dict = dict(
    go.Scatter3d(x=x3RayInData, y=y3RayInData, z=z3RayInData,
                 mode='marker',
                 name='ray3',
                 line=dict(width=1, color='blue')
                 ))


ErefNormalArraay = np.zeros((57,3))
##############################################################################################################
for i in range(0, 19):
    # kinArray = np.array([KxIn[i],
    #                      KyIn[i],
    #                      KzIn[i]
    #                      ])
    # EyIn =  (KxIn[i]* Exin[i]+ KzIn[i]*Ezin[i])/KyIn[i]
    # eInArray = np.array([Exin[i],
    #                      Eyin,
    #                      Ezin[i]]
    #                     )
    # nArray = np.array([Nx[i],
    #                    Ny[i],
    #                    Nz[i]
    #                    ])
    # eRef = np.zeros((1, 3))
    # N1 = (eInArray.dot(nArray.T)) * nArray
    # Er1 = rotor(nArray, eInArray)
    # Er2 = rotor(Er1, nArray)
    # ErefNormal = normalVector(eRef)
    # ErefNormalArraay[i, :] = ErefNormal
    # ExOut = ErefNormal[0]
    # EyOut = ErefNormal[1]
    # EzOut = ErefNormal[2]

    # XeOut = Xout[i] + Ain * ExOut
    # YeOut = Yout[i] + Ain * EyOut
    # ZeOut = Zout[i] + Ain * EzOut

    x1RayData.append(Xin[i])
    x1RayData.append(Xout[i])
    x1RayData.append(np.nan)

    y1RayData.append(Yin[i])
    # y1RayData.append(Zout[i])
    y1RayData.append(200)
    y1RayData.append(np.nan)

    z1RayData.append(Zin[i])
    z1RayData.append(Zout[i])
    z1RayData.append(np.nan)

    XxpolarDataIn1.append(Xin[i])
    XxpolarDataIn1.append(XeIn[i])
    XxpolarDataIn1.append(np.nan)

    XzpolarDataIn1.append(Zin[i])
    XzpolarDataIn1.append(Zin[i])
    XzpolarDataIn1.append(np.nan)

    YpolarDataIn1.append(0)
    YpolarDataIn1.append(0)
    YpolarDataIn1.append(np.nan)

    ZxpolarDataIn1.append(Xin[i])
    ZxpolarDataIn1.append(Xin[i])
    ZxpolarDataIn1.append(np.nan)

    ZzpolarDataIn1.append(Zin[i])
    ZzpolarDataIn1.append(ZeIn[i])
    ZzpolarDataIn1.append(np.nan)

    # XpolarDataOut1.append(Xout[i])
    # XpolarDataOut1.append(XeOut[i])
    # XpolarDataOut1.append(np.nan)

    XxpolarDataOut1.append(Xout[i])
    XxpolarDataOut1.append(XeOut[i])
    XxpolarDataOut1.append(np.nan)

    XzpolarDataOut1.append(Zout[i])
    XzpolarDataOut1.append(Zout[i])
    XzpolarDataOut1.append(np.nan)

    YpolarDataOut1.append(200)
    YpolarDataOut1.append(200)
    YpolarDataOut1.append(np.nan)

    ZxpolarDataOut1.append(Xout[i])
    ZxpolarDataOut1.append(Xout[i])
    ZxpolarDataOut1.append(np.nan)

    ZzpolarDataOut1.append(Zout[i])
    ZzpolarDataOut1.append(ZeOut[i])
    ZzpolarDataOut1.append(np.nan)


conus1InOutDict = dict(
                 go.Scatter3d(x=x1RayData, y=y1RayData, z=z1RayData,
                 mode='marker',
                 name='rayIn',
                 line=dict(width=0.5, color='green')
                 ))
polarDictX1  = dict(
                go.Scatter3d(x=XxpolarDataIn1, y=YpolarDataIn1, z=XzpolarDataIn1,
                     mode='lines',
                     name='X1',
                     line=dict(width=2, color='blue')
                     ))
polarDictZ1  = dict(
                go.Scatter3d(x=ZxpolarDataIn1, y=YpolarDataIn1, z=ZzpolarDataIn1,
                     mode='lines',
                     name='Z1',
                     line=dict(width=2, color='blue')
                     ))
polarDictOutX1  = dict(
                go.Scatter3d(x=XxpolarDataOut1, y=YpolarDataOut1, z=XzpolarDataOut1,
                     mode='lines',
                     name='OutX1',
                     line=dict(width=2, color='red')
                     ))
polarDictOutZ1  = dict(
                go.Scatter3d(x=ZxpolarDataOut1, y=YpolarDataOut1, z=ZzpolarDataOut1,
                     mode='lines',
                     name='OutZ1 ',
                     line=dict(width=2, color='red')
                     ))

for i in range(20, 39):

    #  In DATA
    x2RayData.append(Xin[i])
    x2RayData.append(Xout[i])
    x2RayData.append(np.nan)

    y2RayData.append(Yin[i])
    # y1RayData.append(Zout[i])
    y2RayData.append(200)
    y2RayData.append(np.nan)

    z2RayData.append(Zin[i])
    z2RayData.append(Zout[i])
    z2RayData.append(np.nan)

    XxpolarDataIn2.append(Xin[i])
    XxpolarDataIn2.append(XeIn[i])
    XxpolarDataIn2.append(np.nan)

    XzpolarDataIn2.append(Zin[i])
    XzpolarDataIn2.append(0)
    XzpolarDataIn2.append(np.nan)

    YpolarDataIn2.append(0)
    YpolarDataIn2.append(0)
    YpolarDataIn2.append(np.nan)

    ZxpolarDataIn2.append(Xin[i])
    ZxpolarDataIn2.append(Xin[i])
    ZxpolarDataIn2.append(np.nan)

    ZzpolarDataIn2.append(Zin[i])
    ZzpolarDataIn2.append(ZeIn[i])
    ZzpolarDataIn2.append(np.nan)

    # XpolarDataOut1.append(Xout[i])
    # XpolarDataOut1.append(XeOut[i])
    # XpolarDataOut1.append(np.nan)

    XxpolarDataOut2.append(Xout[i])
    XxpolarDataOut2.append(XeOut[i])
    XxpolarDataOut2.append(np.nan)

    XzpolarDataOut2.append(Zout[i])
    XzpolarDataOut2.append(Zout[i])
    XzpolarDataOut2.append(np.nan)

    YpolarDataOut2.append(200)
    YpolarDataOut2.append(200)
    YpolarDataOut2.append(np.nan)

    ZxpolarDataOut2.append(Xout[i])
    ZxpolarDataOut2.append(Xout[i])
    ZxpolarDataOut2.append(np.nan)

    ZzpolarDataOut2.append(Zout[i])
    ZzpolarDataOut2.append(ZeOut[i])
    ZzpolarDataOut2.append(np.nan)

conus2InOutDict = dict(
    go.Scatter3d(x=x2RayData, y=y2RayData, z=z2RayData,
                 mode='marker',
                 name='rayIn',
                 line=dict(width=0.5, color='green')
                 ))
polarDictX2 = dict(
    go.Scatter3d(x=XxpolarDataIn2, y=YpolarDataIn2, z=XzpolarDataIn2,
                 mode='lines',
                 name='X2',
                 line=dict(width=2, color='blue')
                 ))
polarDictZ2 = dict(
    go.Scatter3d(x=ZxpolarDataIn2, y=YpolarDataIn2, z=ZzpolarDataIn2,
                 mode='lines',
                 name='Z2',
                 line=dict(width=2, color='blue')
                 ))
polarDictOutX2 = dict(
    go.Scatter3d(x=XxpolarDataOut2, y=YpolarDataOut2, z=XzpolarDataOut2,
                 mode='lines',
                 name='OutX2',
                 line=dict(width=2, color='red')
                 ))
polarDictOutZ2 = dict(
    go.Scatter3d(x=ZxpolarDataOut2, y=YpolarDataOut2, z=ZzpolarDataOut2,
                 mode='lines',
                 name='OutZ2',
                 line=dict(width=2, color='red')
                 ))

for i in range(40, 59):

    #  In DATA
    x3RayData.append(Xin[i])
    x3RayData.append(Xout[i])
    x3RayData.append(np.nan)

    y3RayData.append(Yin[i])
    # y1RayData.append(Zout[i])
    y3RayData.append(200)
    y3RayData.append(np.nan)

    z3RayData.append(Zin[i])
    z3RayData.append(Zout[i])
    z3RayData.append(np.nan)

    XxpolarDataIn3.append(Xin[i])
    XxpolarDataIn3.append(XeIn[i])
    XxpolarDataIn3.append(np.nan)

    XzpolarDataIn3.append(Zin[i])
    XzpolarDataIn3.append(Zin[i])
    XzpolarDataIn3.append(np.nan)

    YpolarDataIn3.append(0)
    YpolarDataIn3.append(0)
    YpolarDataIn3.append(np.nan)

    ZxpolarDataIn3.append(Xin[i])
    ZxpolarDataIn3.append(Xin[i])
    ZxpolarDataIn3.append(np.nan)

    ZzpolarDataIn3.append(Zin[i])
    ZzpolarDataIn3.append(ZeIn[i])
    ZzpolarDataIn3.append(np.nan)

    # XpolarDataOut3.append(Xout[i])
    # XpolarDataOut3.append(XeOut[i])
    # XpolarDataOut3.append(np.nan)

    XxpolarDataOut3.append(Xout[i])
    XxpolarDataOut3.append(XeOut[i])
    XxpolarDataOut3.append(np.nan)

    XzpolarDataOut3.append(Zout[i])
    XzpolarDataOut3.append(Zout[i])
    XzpolarDataOut3.append(np.nan)

    YpolarDataOut3.append(200)
    YpolarDataOut3.append(200)
    YpolarDataOut3.append(np.nan)

    ZxpolarDataOut3.append(Xout[i])
    ZxpolarDataOut3.append(Xout[i])
    ZxpolarDataOut3.append(np.nan)

    ZzpolarDataOut3.append(Zout[i])
    ZzpolarDataOut3.append(ZeOut[i])
    ZzpolarDataOut3.append(np.nan)

conus3InOutDict = dict(
    go.Scatter3d(x=x3RayData, y=y3RayData, z=z3RayData,
                 mode='marker',
                 name='rayIn',
                 line=dict(width=0.5, color='green')
                 ))
polarDictX3 = dict(
    go.Scatter3d(x=XxpolarDataIn3, y=YpolarDataIn3, z=XzpolarDataIn3,
                 mode='lines',
                 name='X3',
                 line=dict(width=2, color='blue')
                 ))
polarDictZ3 = dict(
    go.Scatter3d(x=ZxpolarDataIn3, y=YpolarDataIn3, z=ZzpolarDataIn3,
                 mode='lines',
                 name='Z3',
                 line=dict(width=2, color='blue')
                 ))
polarDictOutX3 = dict(
    go.Scatter3d(x=XxpolarDataOut3, y=YpolarDataOut3, z=XzpolarDataOut3,
                 mode='lines',
                 name='OutX3',
                 line=dict(width=2, color='red')
                 ))
polarDictOutZ3 = dict(
    go.Scatter3d(x=ZxpolarDataOut3, y=YpolarDataOut3, z=ZzpolarDataOut3,
                 mode='lines',
                 name='OutZ3',
                 line=dict(width=2, color='red')
                 ))

x1 = 40
x2 = 45
x3 = 53
x4RayData.append(Xin[x1])
x4RayData.append(Xout[x1])
x4RayData.append(np.nan)

x4RayData.append(Xin[x2])
x4RayData.append(Xout[x2])
x4RayData.append(np.nan)

x4RayData.append(Xin[x3])
x4RayData.append(Xout[x3])
x4RayData.append(np.nan)

y4RayData.append(Yin[x1])
y4RayData.append(200)
y4RayData.append(np.nan)

y4RayData.append(Yin[x2])
y4RayData.append(200)
y4RayData.append(np.nan)

y4RayData.append(Yin[x3])
y4RayData.append(200)
y4RayData.append(np.nan)

z4RayData.append(Zin[x1])
z4RayData.append(Zout[x1])
z4RayData.append(np.nan)

z4RayData.append(Zin[x2])
z4RayData.append(Zout[x2])
z4RayData.append(np.nan)

z4RayData.append(Zin[x3])
z4RayData.append(Zout[x3])
z4RayData.append(np.nan)

rotateLine = dict(
    go.Scatter3d(x=x4RayData, y=y4RayData, z=z4RayData,
                 mode='lines',
                 name='rotateline',
                 line=dict(width=3, color='black')
                 ))

layout = dict(width=1920, height=1200,
                      xaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                      yaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                      title='In from Source reflection from Mirror 2 ', hovermode='closest',
                      # updatemenus=[{'type': 'buttons',
                      #               'buttons': [{'label': 'Play',
                      #                            'method': 'animate',
                      #                            'args': [None]}]}]
                      )
data1.append(conus1Dict)
data1.append(conus2Dict)
data1.append(conus3Dict)



data2.append(conus1InOutDict)
data2.append(conus2InOutDict)
data2.append(conus3InOutDict)
# data2.append(rotateLine)
# data2.append(polarDictX1)
# data2.append(polarDictZ1)
# data2.append(polarDictX2)
# data2.append(polarDictZ2)
# data2.append(polarDictX3)
# data2.append(polarDictZ3)
# data2.append(polarDictOutX1)
# data2.append(polarDictOutZ1)
# data2.append(polarDictOutX2)
# data2.append(polarDictOutZ2)
# data2.append(polarDictOutX3)
# data2.append(polarDictOutZ3)

fig = dict(data=data1, layout=layout)
fig1 =  dict(data=data2, layout=layout)
py.offline.plot(fig, filename='conus_0_2.html')
py.offline.plot(fig1, filename='conus_InOut_0_2.html')


