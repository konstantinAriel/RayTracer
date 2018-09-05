import plotly as py
import numpy as np
import pandas as pd
import plotly.tools as tls

import plotly.graph_objs  as go
py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')


# xTLine1 = [-125, -125, -125,  -125,  -125, -125, -125, 3675, 3675, 3675]
# yTLine1 = [-400,  125,  125,   125,  125,4125, 4125,4125, 4125,4125]
# zTLine1 = [-125, -125, -125,   1175,1175, 1175, 1175, 1175, 1175, 600]
#
# xTLine2 = [125, 125, 125, 125, 125, 125, 125, 3925, 3925, 3925]
# yTLine2 = [-400,-125, -125, -125, -125,3875, 3875, 3875, 3875,3875]
# zTLine2 = [125, 125, 125, 1425, 1425, 1425, 1425,1425, 1425, 600]


# x = [[0, 0], [10, 10], [50, 50]]
# y = [[0, 0], [10, 10], [50, 50]]
# z = [[0, 0], [10, 10], [50, 50]]

x = [[0, 0], [0, 10], [50, 50]]
y = [[0, 10], [20, 10], [50, 50]]
z = [[0, 0], [10, 10], [0, 50]]

def rMatrix(alpha, beta, gama):
    global R11, R12, R13, R21, R22, R23, R31, R32, R33

#################################################################
data=[dict(
           go.Scatter3d(x=x, y=y, z=z,
           mode = 'lines',
           name = 'T line 1',
           line = dict(width=2, color='black')
           )),
    # dict (go.Scatter3d(x = xTLine2 , y = yTLine2, z = zTLine2,
    #       mode = 'lines',
    #       name = 'T line 2',
    #       line = dict(width=2, color = 'black')
    #       )),
    # dict(go.Scatter3d(x=x1, y=x2, z=x3,
    #         # name = 'Axes rotated',
    #         # colorscale='',
    #         # lighting=dict(fresnel = 0.9)
    #                   mode='lines',
    #                   name='Not rotated',
    #                   line=dict(width=2, color='Red')
    #       )),
    # dict(go.Scatter3d(x=x1, y=x3r1Positive, z=x2,
    #                   # name = 'Axes rotated',
    #                   # colorscale='blue',
    #                   # lighting=dict(fresnel = 0.9)
    #                   mode='lines',
    #                   name='Rotated',
    #                   line=dict(width=2, color='blue')
    #                   )),
    # dict(go.Scatter3d(x=x1, y=x3r2Positive, z=x2,
    #               # name = 'Axes rotated',
    #                   # colorscale='blue',
    #                   # lighting=dict(fresnel = 0.9)
    #                   mode='lines',
    #               name='Rotated',
    #               line=dict(width=2, color='blue')
    #               )),
    # dict(go.Scatter3d(x=x1, y=x2, z=x3r1Negative,
    #               # name = 'Axes rotated',
    #                   # colorscale='blue',
    #                   # lighting=dict(fresnel = 0.9)
    #                   mode='lines',
    #               name='Positive',
    #               line=dict(width=2, color='blue')
    #               )),
    # dict(go.Scatter3d(x=x1, y=x2, z=x3r2Negative,
    #               # name = 'Axes rotated',
    #                   # colorscale='blue',
    #                   # lighting=dict(fresnel = 0.9)
    #                   mode='lines',
    #               name='Negative',
    #               line=dict(width=2, color='blue')
    #               )),
    ]
layout=dict(width=1920, height=1200,
            xaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
            yaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
            title='Mirror ', hovermode='closest',
            updatemenus= [{'type': 'buttons',
                           'buttons': [{'label': 'Play',
                                        'method': 'animate',
                                        'args': [None]}]}])
# frames=[dict(data=[dict(x=x1r,
#                         y=x2r],
#                         mode='markers',
#                         marker=dict(color='red', size=10)
#                         )
#                   ]) for k in range(N)]



fig=dict(data=data, layout=layout)

py.offline.plot(fig, filename='42RaysforTest MAtrix.html')
