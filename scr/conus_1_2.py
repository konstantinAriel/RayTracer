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
pathOut = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/Ray_1_2.xls'

paramFileIn = pd.ExcelFile(pathIn)
paramFileOut = pd.ExcelFile(pathOut)
dataSheetIn = paramFileIn.parse(sheetname='circul')
dataSheetOut = paramFileOut.parse(sheetname='Sheet1')
# print(dataSheet)
t=200
data1 = []
data2 = []
rayInDict = []
rayOutDict = []
Xin = dataSheetIn.Xin
Yin = dataSheetIn.Yin
Zin = dataSheetIn.Zin
KxIn = dataSheetIn.Kxin
KyIn = dataSheetIn.Kyin
Kzin = dataSheetIn.Kzin

Xout = dataSheetOut.Xin
Yout = dataSheetOut.Yin
Zout = dataSheetOut.Zin
KxOut = dataSheetOut.Kxin
KyOut = dataSheetOut.Kyin
KzOut = dataSheetOut.Kzin

Xin1 = Xin + KxIn * t
Yin1 = Yin + KyIn * t
Zin1 = Zin + Kzin * t

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

xRayReflectedData = []
yRayReflectedData = []
zRayReflectedData = []

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
                     mode='lines',
                     name='rayIn',
                     line=dict(width=2, color='green')
                     ))


for i in range(20,39):
    print(i)
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
                     mode='lines',
                     name='rayIn',
                     line=dict(width=2, color='red')
                     ))


for i in range(40, 59):
    print(i)
    #  In DATA
    x3RayInData.append(Xin[i])
    x3RayInData.append(Xin1[i])
    x3RayInData.append(np.nan)

    y3RayInData.append(Yin[i])
    y3RayInData.append(Yin1[i])
    y3RayInData.append(Yin1[i])
    y3RayInData.append(np.nan)

    z3RayInData.append(Zin[i])
    z3RayInData.append(Zin1[i])
    z3RayInData.append(np.nan)

conus3Dict = dict(
    go.Scatter3d(x=x3RayInData, y=y3RayInData, z=z3RayInData,
                 mode='lines',
                 name='rayIn',
                 line=dict(width=2, color='blue')
                 ))
##############################################################################################################
for i in range(0, 19):
    print(i)
    #  In DATA
    x1RayData.append(Xin[i])
    x1RayData.append(Xout[i])
    x1RayData.append(np.nan)

    y1RayData.append(Yin[i])
    y1RayData.append(Zout[i])
    #y1RayData.append(200)
    y1RayData.append(np.nan)

    z1RayData.append(Zin[i])
    z1RayData.append(Yout[i])
    z1RayData.append(np.nan)

conus1InOutDict = dict(
    go.Scatter3d(x=x1RayData, y=y1RayData, z=z1RayData,
                 mode='lines',
                 name='rayIn',
                 line=dict(width=2, color='green')
                 ))

for i in range(20, 39):
    print(i)
    #  In DATA
    x2RayData.append(Xin[i])
    x2RayData.append(Xout[i])
    x2RayData.append(np.nan)

    y2RayData.append(Yin[i])
    y2RayData.append(Zout[i])
    y2RayData.append(np.nan)

    z2RayData.append(Zin[i])
    z2RayData.append(Yout[i])
    z2RayData.append(np.nan)

conus2InOutDict = dict(
    go.Scatter3d(x=x2RayData, y=y2RayData, z=z2RayData,
                 mode='lines',
                 name='rayIn',
                 line=dict(width=2, color='red')
                 ))

for i in range(40, 59):
    print(i)
    #  In DATA
    x3RayData.append(Xin[i])
    x3RayData.append(Xout[i])
    x3RayData.append(np.nan)

    y3RayData.append(Yin[i])
    y3RayData.append(Zout[i])
    y3RayData.append(np.nan)

    z3RayData.append(Zin[i])
    z3RayData.append(Yout[i])
    z3RayData.append(np.nan)

conus3InOutDict = dict(
    go.Scatter3d(x=x3RayData, y=y3RayData, z=z3RayData,
                 mode='lines',
                 name='rayIn',
                 line=dict(width=2, color='blue')
                 ))

layout = dict(width=1920, height=1200,
                      xaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                      yaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                      title='Mirror ', hovermode='closest',
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

fig = dict(data=data1, layout=layout)
fig1 =  dict(data=data2, layout=layout)
py.offline.plot(fig, filename='conus_01.html')
py.offline.plot(fig1, filename='conus_InOut_01.html')


