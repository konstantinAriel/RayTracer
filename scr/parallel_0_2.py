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

paramFileIn = pd.ExcelFile(pathIn)
paramFileOut = pd.ExcelFile(pathOut)

dataSheetIn = paramFileIn.parse(sheetname ='circlParalel')
dataSheetOut = paramFileOut.parse(sheetname ='Sheet1')


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

Exin = dataSheetIn.Exin
Eyin = dataSheetIn.Eyin
Ezin = dataSheetIn.Ezin
Ain = dataSheetIn.Ain

Xout = dataSheetOut.Xin
Yout = dataSheetOut.Yin
Zout = dataSheetOut.Zin

KxOut = dataSheetOut.Kxin
KyOut = dataSheetOut.Kyin
KzOut = dataSheetOut.Kzin


x1RayDataIn = []
y1RayDataIn = []
z1RayDataIn = []

x1RayDataOut = []
y1RayDataOut = []
z1RayDataOut = []

x2RayDataIn = []
y2RayDataIn = []
z2RayDataIn = []

x2RayDataOut = []
y2RayDataOut = []
z2RayDataOut = []

x3RayDataIn = []
y3RayDataIn = []
z3RayDataIn = []

x3RayDataOut = []
y3RayDataOut = []
z3RayDataOut = []

x1PointIn = []
x2PointIn = []
x3PointIn = []
x4PointIn = []

z1PointIn = []
z2PointIn = []
z3PointIn = []
z4PointIn = []

x1PointOut = []
x2PointOut = []
x3PointOut = []
x4PointOut = []

z1PointOut = []
z2PointOut = []
z3PointOut = []
z4PointOut = []

x1PointIn.append(Xin[0])
x1PointIn.append(Xin[20])
x1PointIn.append(Xin[40])
x1PointIn.append(np.nan)
x1PointIn.append(Xin[10])
x1PointIn.append(Xin[30])
x1PointIn.append(Xin[50])

z1PointIn.append(Zin[0])
z1PointIn.append(Zin[20])
z1PointIn.append(Zin[40])
z1PointIn.append(np.nan)
z1PointIn.append(Zin[10])
z1PointIn.append(Zin[30])
z1PointIn.append(Zin[50])
x1DictIn = dict(
            go.Scatter(x=x1PointIn,  y=z1PointIn,
                     mode='line',
                     name='Line 1 In',
                     line=dict(width=1, color='black')
                     ))

x2PointIn.append(Xin[3])
x2PointIn.append(Xin[23])
x2PointIn.append(Xin[43])
x2PointIn.append(np.nan)
x2PointIn.append(Xin[13])
x2PointIn.append(Xin[33])
x2PointIn.append(Xin[53])

z2PointIn.append(Zin[3])
z2PointIn.append(Zin[23])
z2PointIn.append(Zin[43])
z2PointIn.append(np.nan)
z2PointIn.append(Zin[13])
z2PointIn.append(Zin[33])
z2PointIn.append(Zin[53])

x2DictIn = dict(
            go.Scatter(x=x2PointIn,  y=z2PointIn,
                     mode='line',
                     name='Line 2 In',
                     line=dict(width=1, color='blue')
                     ))

x3PointIn.append(Xin[5])
x3PointIn.append(Xin[25])
x3PointIn.append(Xin[45])
x3PointIn.append(np.nan)
x3PointIn.append(Xin[15])
x3PointIn.append(Xin[35])
x3PointIn.append(Xin[55])

z3PointIn.append(Zin[5])
z3PointIn.append(Zin[25])
z3PointIn.append(Zin[45])
z3PointIn.append(np.nan)
z3PointIn.append(Zin[15])
z3PointIn.append(Zin[35])
z3PointIn.append(Zin[55])
x3DictIn = dict(
            go.Scatter(x=x3PointIn,  y=z3PointIn,
                     mode='line',
                     name='Line 3 In',
                     line=dict(width=1, color='green')
                     ))

x4PointIn.append(Xin[7])
x4PointIn.append(Xin[27])
x4PointIn.append(Xin[47])
x4PointIn.append(np.nan)
x4PointIn.append(Xin[17])
x4PointIn.append(Xin[37])
x4PointIn.append(Xin[57])

z4PointIn.append(Zin[7])
z4PointIn.append(Zin[27])
z4PointIn.append(Zin[47])
z4PointIn.append(np.nan)
z4PointIn.append(Zin[17])
z4PointIn.append(Zin[37])
z4PointIn.append(Zin[57])
x4DictIn = dict(
            go.Scatter(x=x4PointIn,  y=z4PointIn,
                     mode='line',
                     name='line 4 In',
                     line=dict(width=1, color='red')
                     ))

x1PointOut.append(Xout[0])
x1PointOut.append(Xout[20])
x1PointOut.append(Xout[40])
x1PointOut.append(np.nan)
x1PointOut.append(Xout[10])
x1PointOut.append(Xout[30])
x1PointOut.append(Xout[50])

z1PointOut.append(Zout[0])
z1PointOut.append(Zout[20])
z1PointOut.append(Zout[40])
z1PointOut.append(np.nan)
z1PointOut.append(Zout[10])
z1PointOut.append(Zout[30])
z1PointOut.append(Zout[50])
x1DictOut = dict(
    go.Scatter(x=x1PointOut, y=z1PointOut,
               mode='line',
               name='Line 1 Out',
               line=dict(width=1, color='black')
               ))

x2PointOut.append(Xout[3])
x2PointOut.append(Xout[23])
x2PointOut.append(Xout[43])
x2PointOut.append(np.nan)
x2PointOut.append(Xout[13])
x2PointOut.append(Xout[33])
x2PointOut.append(Xout[53])

z2PointOut.append(Zout[3])
z2PointOut.append(Zout[23])
z2PointOut.append(Zout[43])
z2PointOut.append(np.nan)
z2PointOut.append(Zout[13])
z2PointOut.append(Zout[33])
z2PointOut.append(Zout[53])

x2DictOut = dict(
                go.Scatter(x=x2PointOut, y=z2PointOut,
               mode='line',
               name='Line 2 Out',
               line=dict(width=1, color='blue')
               ))

x3PointOut.append(Xout[5])
x3PointOut.append(Xout[25])
x3PointOut.append(Xout[45])
x3PointOut.append(np.nan)
x3PointOut.append(Xout[15])
x3PointOut.append(Xout[35])
x3PointOut.append(Xout[55])

z3PointOut.append(Zout[5])
z3PointOut.append(Zout[25])
z3PointOut.append(Zout[45])
z3PointOut.append(np.nan)
z3PointOut.append(Zout[15])
z3PointOut.append(Zout[35])
z3PointOut.append(Zout[55])
x3DictOut = dict(
                go.Scatter(x=x3PointOut, y=z3PointOut,
               mode='line',
               name='Line 3 Out',
               line=dict(width=1, color='green')
               ))

x4PointOut.append(Xout[7])
x4PointOut.append(Xout[27])
x4PointOut.append(Xout[47])
x4PointOut.append(np.nan)
x4PointOut.append(Xout[17])
x4PointOut.append(Xout[37])
x4PointOut.append(Xout[57])

z4PointOut.append(Zout[7])
z4PointOut.append(Zout[27])
z4PointOut.append(Zout[47])
z4PointOut.append(np.nan)
z4PointOut.append(Zout[17])
z4PointOut.append(Zout[37])
z4PointOut.append(Zout[57])
x4DictOut = dict(
    go.Scatter(x=x4PointOut, y=z4PointOut,
               mode='line',
               name='line 4 Out',
               line=dict(width=1, color='red')
               ))

for i in range(0,19):

    #  In DATA
    x1RayDataIn.append(Xin[i])
    # x1RayDataIn.append(np.nan)

    z1RayDataIn.append(Zin[i])
    # z1RayDataIn.append(np.nan)


    x1RayDataOut.append(Xout[i])
    # x1RayDataOut.append(np.nan)

    z1RayDataOut.append(Zout[i])
    # z1RayDataOut.append(np.nan)

x1RayDataIn.append(Xin[0])
z1RayDataIn.append(Zin[0])
x1RayDataOut.append(Xout[0])
z1RayDataOut.append(Zout[0])

In1Dict = dict(
        go.Scatter(x=x1RayDataIn,  y=z1RayDataIn,
                     mode='lines+markers',
                     name='rayIn1',
                     line=dict(width=3, color='blue')
                     ))
Out1Dict = dict(
        go.Scatter(x=x1RayDataOut, y=z1RayDataOut,
                     mode='lines+markers',
                     name='rayOut1',
                     line=dict(width=3, color='blue', dash = 'dash', shape='spline')
                     ))

for i in range(20,39):
    #  In DATA
    x2RayDataIn.append(Xin[i])
    # x2RayDataIn.append(np.nan)

    z2RayDataIn.append(Zin[i])
    # z2RayDataIn.append(np.nan)


    x2RayDataOut.append(Xout[i])
    # x2RayDataOut.append(np.nan)

    z2RayDataOut.append(Zout[i])
    # z2RayDataOut.append(np.nan)

x2RayDataIn.append(Xin[20])
z2RayDataIn.append(Zin[20])
x2RayDataOut.append(Xout[20])
z2RayDataOut.append(Zout[20])
In2Dict = dict(
        go.Scatter(x=x2RayDataIn, y=z2RayDataIn,
                     mode='lines+markers',
                     name='rayIn2',
                     line=dict(width=3, color='red')
                     ))
Out2Dict = dict(
        go.Scatter(x=x2RayDataOut, y=z2RayDataOut,
                     mode='lines+markers',
                     name='rayOut2',
                     line=dict(width=3, color='red', dash = 'dash', shape='spline')
                     ))

for i in range(40, 59):
    #  In DATA
    x3RayDataIn.append(Xin[i])
    # x3RayDataIn.append(np.nan)

    z3RayDataIn.append(Zin[i])
    # z3RayDataIn.append(np.nan)


    x3RayDataOut.append(Xout[i])
    # x3RayDataOut.append(np.nan)

    z3RayDataOut.append(Zout[i])
    # z3RayDataOut.append(np.nan)
x3RayDataIn.append(Xin[40])
z3RayDataIn.append(Zin[40])
x3RayDataOut.append(Xout[40])
z3RayDataOut.append(Zout[40])
In3Dict = dict(
        go.Scatter(x=x3RayDataIn, y=z3RayDataIn,
                     mode='lines+markers',
                     name='rayIn3',
                     line=dict(width=3, color='green')
                     ))
Out3Dict = dict(
        go.Scatter(x=x3RayDataOut, y=z3RayDataOut,
                     mode='lines+markers',
                     name='rayOut3',
                     line=dict(width=3, color='green', dash = 'dash', shape='spline')
                     ))

##############################################################################################################

layout = dict(width=1920, height=1200,
                      xaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                      yaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                      title='In from Source reflection from Mirror 2 ', hovermode='closest',
                      # updatemenus=[{'type': 'buttons',
                      #               'buttons': [{'label': 'Play',
                      #                            'method': 'animate',
                      #                            'args': [None]}]}]
                      )
data1.append(In1Dict)
data1.append(Out1Dict)
data1.append(In2Dict)
data1.append(Out2Dict)
data1.append(In3Dict)
data1.append(Out3Dict)
data1.append(x1DictIn)
data1.append(x2DictIn)
data1.append(x3DictIn)
data1.append(x4DictIn)
data1.append(x1DictOut)
data1.append(x2DictOut)
data1.append(x3DictOut)
data1.append(x4DictOut)

fig = dict(data=data1, layout=layout)
py.offline.plot(fig, filename='paralel_0_2.html')



