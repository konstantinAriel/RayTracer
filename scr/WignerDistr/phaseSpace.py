import scr.mainParamPakage as mp
import scr.RayTracing.Rays as rmain
import plotly.graph_objs  as go

import plotly as py
import numpy as np
import pandas as pd
import plotly.tools as tls
import plotly.graph_objs  as go


py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

m=1
n=0
a = 500
b = 600
Nx = 100
Nz = 100
K0x = (m*np.pi)/a
K0z = (n*np.pi)/b
x0 = a/2
z0 = b/2
dx = a/Nx
dz = b/Nz

# ExArray = np.zeros((N, 1))
ExArray = np.empty([Nx,1])
x = np.linspace(-x0, x0, Nx)
z = np.linspace(-z0, z0, Nz)

# EzArray = np.zeros((N,1))
EzArray = np.empty([Nx,1])
# xArray  = np.zeros((N,1))
xArray  = np.empty([Nx,1])
zArray  = np.empty([Nz,1])
xZData = []
yZData = []

xXData = []
yXData = []
xXZData = []
yXZData = []

for dx in x:
    FxX = (dx + np.sin((m*np.pi*dx)/a))

    xXData.append(dx)
    xXData.append(dx)
    xXData.append(np.nan)

    yXData.append(0)
    yXData.append(FxX)
    yXData.append(np.nan)

EXZDict = dict(
              go.Scatter(x=xXData,
              y=yXData,
              mode='Lines',
              name='Ex',
              line=dict(width=2, color='red')
                    ))
plotFileName = '/home/konstantin/PycharmProjects/RayTracer/result/htmlFiles/newDir/Fxy_X'  + '.html'
layout = dict(width=1920, height=1200,
              xaxis=dict(range=[-100, 100], autorange=True, zeroline=True),
              yaxis=dict(range=[-100, 100], autorange=True, zeroline=True),
              title='Rayin vs RayOut_', hovermode='closest',
                      )
data = []
data.append(EXZDict)
fig = dict(data=data, layout=layout)
py.offline.plot(fig, filename=plotFileName)

for dz in z:

    # Ex = (np.cos(K0x*(x+(a/2)))*np.sin(K0z*(z+(b/2))))
    #
    # Ey = (np.sin(K0x*(x + (a/2)))*np.cos(K0z*(z+(b/2))))
    #
    # ExArray[i, 0] = Ex
    # xArray[i, 0] = x
    # zArray[i, 0] = z
    FxyZ = (np.sin((n*np.pi*dz)/b))

    xZData.append(dz)
    xZData.append(dz)
    xZData.append(np.nan)

    yZData.append(0)
    yZData.append(FxyZ)
    yZData.append(np.nan)

EZDict = dict(
              go.Scatter(x=xZData,
              y=yZData,
              mode='Lines',
              name='EZ',
              line=dict(width=2, color='red')
             ))
plotFileName = '/home/konstantin/PycharmProjects/RayTracer/result/htmlFiles/newDir/Fxy_Z'  + '.html'
layout = dict(width=1920, height=1200,
              xaxis=dict(range=[-100, 100], autorange=True, zeroline=True),
              yaxis=dict(range=[-100, 100], autorange=True, zeroline=True),
              title='Rayin vs RayOut_', hovermode='closest',
                      )
data = []
data.append(EZDict)
fig = dict(data=data, layout=layout)
py.offline.plot(fig, filename=plotFileName)