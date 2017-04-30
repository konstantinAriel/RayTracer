import plotly as py
import numpy as np
import pandas as pd
import plotly.tools as tls

import plotly.graph_objs  as go
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

x_start = 125
x = np.linspace(-x_start, x_start, 50)
z = np.linspace(-x_start, x_start, 50)
X,Z = np.meshgrid(x, z)
#print (X)
a11 = 1/800
a22 = 1/800
Y = -(a11*(X**2) + a22*((Z-400)**2))+200;

xTLine1 = [-125, -125]
yTLine1 = [-400, 125]
zTLine1 = [-125, -125]

xTLine2 = [125, 125]
yTLine2 = [-400,-125]
zTLine2 = [125, 125]

xTLine3 = [-125, -125]
yTLine3 = [125,125]
zTLine3 = [-125, 1175]

xTLine4 = [125, 125]
yTLine4 = [-125, -125]
zTLine4 = [125, 1425]

xTLine5 = [-125, -125]
yTLine5 = [125,4125]
zTLine5 = [1175, 1175]

xTLine6 = [125, 125]
yTLine6 = [-125,3875]
zTLine6 = [1425, 1425]

xTLine7 = [-125, 3675]
yTLine7 = [4125,4125]
zTLine7 = [1175, 1175]

xTLine8 = [125, 3925]
yTLine8 = [3875,3875]
zTLine8 = [1425,1425 ]

xTLine9 = [3675, 3675]
yTLine9 = [4125,4125]
zTLine9 = [1175, 600]

xTLine10 = [3925, 3925]
yTLine10 = [3875,3875]
zTLine10 = [1425, 600]



trace1 = go.Scatter3d(x = xTLine1,
                         y = yTLine1,
                         z = zTLine1,
                         mode = 'lines',
                         name = 'TLine1')

trace2 = go.Scatter3d(x = xTLine2,
                         y = yTLine2,
                         z = zTLine2,
                         mode = 'lines',
                         name = 'TLine2')

trace3 = go.Scatter3d(   x = xTLine3,
                         y = yTLine3,
                         z = zTLine3,
                         mode = 'lines',
                         name = 'TLine3')

trace4 = go.Scatter3d(   x = xTLine4,
                         y = yTLine4,
                         z = zTLine4,
                         mode = 'lines',
                         name = 'TLine4')

trace5 = go.Scatter3d(   x = xTLine5,
                         y = yTLine5,
                         z = zTLine5,
                         mode = 'lines',
                         name = 'TLine5')
trace6 = go.Scatter3d(   x = xTLine6,
                         y = yTLine6,
                         z = zTLine6,
                         mode = 'lines',
                         name = 'TLine6')

trace7 = go.Scatter3d(   x = xTLine7,
                         y = yTLine7,
                         z = zTLine7,
                         mode = 'lines',
                         name = 'TLine7')
trace8 = go.Scatter3d(   x = xTLine8,
                         y = yTLine8,
                         z = zTLine8,
                         mode = 'lines',
                         name = 'TLine8')

trace9 = go.Scatter3d(   x = xTLine9,
                         y = yTLine9,
                         z = zTLine9,
                         mode = 'lines',
                         name = 'TLine9')

trace10 = go.Scatter3d(   x = xTLine10,
                         y = yTLine10,
                         z = zTLine10,
                         mode = 'lines',
                         name = 'TLine10')


trace20 = go.Surface(x=X, y=Y, z=Z, colorscale='')

data = go.Data([trace20, trace1, trace2, trace3, trace4,trace5, trace6,trace7, trace8,trace9, trace10])
fig = go.Figure(data=data)

py.offline.plot(fig, filename='5Main RaysMiror1-4.html')
#######################################################

data=[dict(
           go.Scatter3d(x=xl0, y=yl0, z=Zo,
           mode = 'lines',
           name = 'Axes not rotated',
           line = dict(width=2, color='red')
           )),
    dict (go.Scatter3d(x=xp0, y=yp0, z=x3,
          mode = 'lines',
          name = 'porabola rotated',
          line = dict(width=2, color = 'red')
          )),
    dict(go.Scatter3d(x=xl1, y=yl1, z=Zo,
           mode ='lines',
           name = 'Axes rotated',
           line = dict(width=2, color='blue')
          )),
    dict(go.Scatter3d(x=u, y=v, z=x3,
           mode ='lines',
           name = 'parabola rotated',
           line = dict(width=2, color='blue')
          ))
    ]
layout=dict(width=1200, height=900,
            xaxis=dict(range=[-10, 10], autorange=False, zeroline=False),
            yaxis=dict(range=[-10, 10], autorange=False, zeroline=False),
            title='rotated Vs not rotated', hovermode='closest',
            updatemenus= [{'type': 'buttons',
                           'buttons': [{'label': 'Play',
                                        'method': 'animate',
                                        'args': [None]}]}])


fig=dict(data=data, layout=layout)