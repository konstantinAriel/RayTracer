import scipy.io as sio
import datetime
import numpy as np

import plotly as py

import pandas as pd
import plotly.tools as tls
import plotly.graph_objs  as go

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

dirPathInDataW = '/home/konstantin/rt/RayTracer/files/inDataWxWz/'
modeDir = 'm_1_n_2/'

WxDir = 'wx/'
WyDir = 'wy/'

XinZinMat   = sio.loadmat(dirPathInDataW + modeDir + 'xyPoints')
KxKzMat     = sio.loadmat(dirPathInDataW + modeDir + 'KxKyPoints')
wXMat       = sio.loadmat(dirPathInDataW + modeDir + WxDir + 'wx_X_1_Y_ 1' )
wZMat       = sio.loadmat(dirPathInDataW + modeDir + WyDir + 'wy_X_1_Y_ 1')


XinZin  =  XinZinMat['XY']
KxKz    =  KxKzMat['KxKy']

wX      =  wXMat['wX_xyKxKy_TM']
wZ      =  wZMat['wY_xyKxKy_TM']

# print('XY = ',  XinZin)
# print('KxKy = ',   KxKz)
# print('wx = ', wX)
# print('wY = ', wZ)

X1Mesh, X2Mesh = np.meshgrid(wX, wZ)
dict(go.Surface(x=x1R, y=x2R, z=x3R,
                    showscale = False,
                    opacity = 1,
                    type = 'surface',
                    surfacecolor = 'blue',
                    name = str(self.mirrorIndex)))

fig = dict(data=data, layout=layout)
        py.offline.plot(fig, filename=filename)