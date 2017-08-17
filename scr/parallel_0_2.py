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

dataSheetIn = paramFileIn.parse(sheetname ='circul')
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


for i in range(0,19):
    print(i)
    #  In DATA
    x1RayDataIn.append(Xin[i])
    x1RayDataIn.append(np.nan)

    z1RayDataIn.append(Zin[i])
    z1RayDataIn.append(np.nan)


    x1RayDataOut.append(Xout[i])
    x1RayDataOut.append(np.nan)

    z1RayDataOut.append(Zout[i])
    z1RayDataOut.append(np.nan)


In1Dict = dict(
        go.Scatter3d(x=x1RayDataIn, y=y1RayDataIn, z=z1RayDataIn,
                     mode='marker',
                     name='rayIn1',
                     line=dict(width=1, color='green')
                     ))
Out1Dict = dict(
        go.Scatter3d(x=x1RayDataOut, y=y1RayDataOut, z=z1RayDataOut,
                     mode='marker',
                     name='rayIn1',
                     line=dict(width=1, color='green')
                     ))

for i in range(20,39):
    #  In DATA
    x2RayDataIn.append(Xin[i])
    x2RayDataIn.append(np.nan)

    z2RayDataIn.append(Zin[i])
    z2RayDataIn.append(np.nan)


    x2RayDataOut.append(Xout[i])
    x2RayDataOut.append(np.nan)

    z2RayDataOut.append(Zout[i])
    z2RayDataOut.append(np.nan)

In2Dict = dict(
        go.Scatter3d(x=x2RayDataIn, y=y2RayDataIn, z=z2RayDataIn,
                     mode='marker',
                     name='rayIn1',
                     line=dict(width=1, color='green')
                     ))
Out2Dict = dict(
        go.Scatter3d(x=x2RayDataOut, y=y2RayDataOut, z=z2RayDataOut,
                     mode='marker',
                     name='rayIn1',
                     line=dict(width=1, color='green')
                     ))

for i in range(40, 59):
    #  In DATA
    x3RayDataIn.append(Xin[i])
    x3RayDataIn.append(np.nan)

    z3RayDataIn.append(Zin[i])
    z3RayDataIn.append(np.nan)


    x3RayDataOut.append(Xout[i])
    x3RayDataOut.append(np.nan)

    z3RayDataOut.append(Zout[i])
    z3RayDataOut.append(np.nan)

In3Dict = dict(
        go.Scatter3d(x=x3RayDataIn, y=y3RayDataIn, z=z3RayDataIn,
                     mode='marker',
                     name='rayIn1',
                     line=dict(width=1, color='green')
                     ))
Out3Dict = dict(
        go.Scatter3d(x=x3RayDataOut, y=y3RayDataOut, z=z3RayDataOut,
                     mode='marker',
                     name='rayIn1',
                     line=dict(width=1, color='green')
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
data1.append(In2Dict)
data1.append(In3Dict)
data1.append(Out1Dict)
data1.append(Out2Dict)
data1.append(Out3Dict)


fig = dict(data=data1, layout=layout)

py.offline.plot(fig, filename='paralel_0_2.html')



