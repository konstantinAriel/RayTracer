import pandas as pd
import numpy as np

import plotly as py
import plotly.tools as tls
import plotly.graph_objs  as go

from scr.MainParam import Parametrs
from scr.Rays import Rays

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
path = '/home/konstantin/PycharmProjects/RayTracer/result/FromWigner/RinWignerDis_0_1.xls'
m = 0
n = 1

Nx = 5
Nz = 5
Nkx = 11
Nkz = 11
Z0 = 377
L = 0.3
a = 12
b = 6

k0 = (2)/L
k0Z = (m)/a
k0X = (n)/b
xs = b/2
x = np.linspace(-xs, xs, Nx)
zs = a/2
z = np.linspace(-zs, zs, Nz)
kxs = 0.15
kx = np.linspace(-kxs, kxs, Nkx)
kzs = 0.15
kz = np.linspace(-kxs, kxs, Nkz)



paramFile = pd.ExcelFile(path)
dataSheet = paramFile.parse(sheetname='Sheet1')
print(dataSheet)


Z, X = np.meshgrid(x, z)
Wx = dataSheet.Wx
WxSum = 0
WxSumArray = np.zeros((Nx, Nz))
j= 0
cx = 0
cy = 0
for j in range (0, (Nx*Nz)):

    for i in range(j*(Nkx*Nkz), (j+1)*(Nkx*Nkz-1)):
        WxSum = WxSum + Wx[i]
    WxSumArray[cy, cx] = WxSum
    cx = cx + 1
    if cx == 5:
        cx = 0
        cy = cy + 1
    WxSum = 0

Intensity  = dict(
                go.Surface(
                x=X, y=Z, z=WxSumArray,
                showscale = True,
                opacity = 1,
                type = 'surface',
                name = 'I_0_1'))
print(Intensity)
layout = dict(width=1920, height=1200,
                      xaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                      yaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                      title='Intensity Out from WIGLER EE mode - TE_01  ', hovermode='closest',
                      # updatemenus=[{'type': 'buttons',
                      #               'buttons': [{'label': 'Play',
                      #                            'method': 'animate',
                      #                            'args': [None]}]}]
                      )
data = []
data.append(Intensity)
fig = dict(data=data, layout=layout)
py.offline.plot(fig, filename='intensity_0_1.html')