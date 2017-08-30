import pandas as pd
import numpy as np

import plotly as py
import plotly.tools as tls
import plotly.graph_objs  as go
import plotly.figure_factory as ff

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

# xa = np.zeros((1, Nx*Nz ))
xa = []
# za = np.zeros((1, Nx*Nz ))
za = []

paramFile = pd.ExcelFile(path)
dataSheet = paramFile.parse(sheetname='Sheet1')
print(dataSheet)

Z, X = np.meshgrid(x, z)
for xi in x:
    for zi in z:
        xa.append(xi)
        za.append(zi)

ExRe = dataSheet.ExRe
ExIm = dataSheet.ExIm
EzRe = dataSheet.EzRe
EzIm = dataSheet.EzIm

ExReSum = 0
ExImSum = 0
EzReSum = 0
EzImSum = 0

ExReSumArray = np.zeros((Nx, Nz))
ExImSumArray = np.zeros((Nx, Nz))
EzReSumArray = np.zeros((Nx, Nz))
EzImSumArray = np.zeros((Nx, Nz))
j= 0
cx = 0
cy = 0
for j in range (0, (Nx*Nz)):
    for i in range(j*(Nkx*Nkz), (j+1)*(Nkx*Nkz-1)):
        ExReSum = ExReSum + ExRe[i]
        ExImSum = ExImSum + ExIm[i]
        EzReSum = EzReSum + EzRe[i]
        EzImSum = EzImSum + EzIm[i]
    ExReSumArray[cy, cx] = ExReSum
    ExImSumArray[cy, cx] = ExImSum
    EzReSumArray[cy, cx] = EzReSum
    EzImSumArray[cy, cx] = EzImSum
    cx = cx + 1
    if cx == 5:
        cx = 0
        cy = cy + 1
    ExReSum = 0
    ExImSum = 0
    EzReSum = 0
    EzImSum = 0

# polarExRe  = dict(
#                 go.Surface(
#                 x=X, y=Z, z=ExReSumArray,
#                 showscale = True,
#                 opacity = 1,
#                 type = 'surface',
#                 name = 'I_0_1'))
# polarExIm  = dict(
#                 go.Surface(
#                 x=X, y=Z, z=ExImSumArray,
#                 showscale = True,
#                 opacity = 1,
#                 type = 'surface',
#                 name = 'I_0_1'))
# polarEzRe  = dict(
#                 go.Surface(
#                 x=X, y=Z, z=EzReSumArray,
#                 showscale = True,
#                 opacity = 1,
#                 type = 'surface',
#                 name = 'I_0_1'))
#
# polarEzIm  = dict(
#                 go.Surface(
#                 x=X, y=Z, z=EzImSumArray,
#                 showscale = True,
#                 opacity = 1,
#                 type = 'surface',
#                 name = 'I_0_1'))
#  layout = dict(width=1920, height=1200,
#                       xaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
#                       yaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
#                       title='Intensity Out from WIGLER EE mode - TE_01  ', hovermode='closest',
#                       # updatemenus=[{'type': 'buttons',
#                       #               'buttons': [{'label': 'Play',
#                       #                            'method': 'animate',
#                       #                            'args': [None]}]}]
#                       )
# data1 = []
# data1.append(polarExRe)
# data2 = []
# data2.append(polarExIm)
# data3 = []
# data3.append(polarEzRe)
# data4 = []
# data4.append(polarEzIm)
F = 100
fig1 = ff.create_quiver(X, Z, ExReSumArray/F, EzReSumArray/F,
                        scale=.1,
                        arrow_scale=.4,
                        name='Real',
                        line=dict(width=1)
                        )
fig2 = ff.create_quiver(X, Z, ExImSumArray/F, EzImSumArray/F,
                        scale=.1,
                        arrow_scale = 0.2,
                        name='Image',
                        line=dict(width=1)
                        )
points = go.Scatter(x=xa, y=za,
                    mode='markers',
                    marker=dict(size=12),
                    name='points')

# Add points to figure
fig1['data'].append(points)
fig2['data'].append(points)


py.offline.plot(fig1, filename='polarization_0_1_Re_Ex_Ez .html')
py.offline.plot(fig2, filename='polarization_0_1_IM_Ex_Ez .html')
