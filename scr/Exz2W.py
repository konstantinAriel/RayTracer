import numpy as np
import plotly as py
import pandas as pd
import plotly.tools as tls
import plotly.graph_objs  as go



py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
########################################################3
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


totalSize = Nx*Nz*Nkx*Nkz
fcosXArray = np.zeros((totalSize, 1))
fcosZArray = np.zeros((totalSize, 1))
fsinXArray = np.zeros((totalSize, 1))
fsinZArray = np.zeros((totalSize, 1))
WxTEmode = np.zeros((totalSize,1))
WzTEmode = np.zeros((totalSize, 1))

XinArray = np.zeros((totalSize,3))
KinArray = np.zeros((totalSize,3))
EinArray = np.zeros((totalSize,11))

kyArray = np.zeros((totalSize,1))
ExArray = np.zeros((totalSize, 1))
EyArray = np.zeros((totalSize, 1))
ExReArray = np.zeros((totalSize, 1))
ExImArray = np.zeros((totalSize, 1))
EzReArray = np.zeros((totalSize, 1))
EzImArray = np.zeros((totalSize, 1))
EzArray = np.zeros((totalSize, 1))
eXArray = np.zeros((totalSize, 1))
eYArray = np.zeros((totalSize, 1))
eZArray = np.zeros((totalSize, 1))
zImpedance = 377
print(WxTEmode)
def fCos (ai, xi, k0i, ki):
    res =   ((ai / 2 - np.abs(xi)) *
             (2 * np.cos(2 * np.pi*k0i * (xi + (ai / 2)))) *
             (np.sinc(2 * ki * (ai / 2 - np.abs(xi)))) +
             (np.sinc(2 * (ki + k0i) * (ai / 2 - np.abs(xi)))) +
             (np.sinc(2 * (ki - k0i) * (ai / 2 - np.abs(xi))))
             )
    return  res

def fSin (ai, xi, k0i, ki):
    res = ((ai / 2 - np.abs(xi)) *
           (2 * np.cos(2 * np.pi * k0i * (xi + (ai / 2)))) *
           (np.sinc(2 * ki * (ai / 2 - np.abs(xi)))) -
           (np.sinc(2 * (ki + k0i) * (ai / 2 - np.abs(xi)))) -
           (np.sinc(2 * (ki - k0i) * (ai / 2 - np.abs(xi))))
           )
    return res

def setData4Plot(x0, z0, y0, kx, ky, kz, Wx, Wz):
    x = x0 + Wx*kx
    y = y0 + np.sqrt(Wx**2 + Wz**2)*ky
    z = z0 + Wz*kz
    trace = go.Scatter3d(x=x, y=y, z=z,
                          mode='lines',
                          name='rayIn' ,
                          line=dict(width=2, color='blue')
                          )
    return trace

def getReE(x, kx, W):
    eX = x*kx
    Ex = W *np.cos(eX)
    return Ex, eX
def getImE(x,  kx, W):
    eX = x * kx
    Ex = W * np.sin(eX)
    return Ex


def setRaysDataFrame(XinArray,  KinArray, EinArray):
    raysDF = pd.DataFrame({'Xin': XinArray[:, 0],
                           'Yin': XinArray[:, 1],
                           'Zin': XinArray[:, 2],
                           'Kxin': KinArray[:, 0],
                           'Kyin': KinArray[:, 1],
                           'Kzin': KinArray[:, 2],
                           'ExRe': EinArray[:, 0],
                           'ExIm': EinArray[:, 1],
                           'EyRe': EinArray[:, 2],
                           'EyIm': EinArray[:, 3],
                           'EzRe': EinArray[:, 4],
                           'EzIm': EinArray[:, 5],
                           'eX': EinArray[:, 6],
                           'eY': EinArray[:, 7],
                           'ez': EinArray[:, 8],
                           'Wx': EinArray[:, 9],
                           'Wz': EinArray[:, 10]
                           })
    return raysDF
def saveRays2Execel(fileName, raysDataFrame):
        raysDataFrame.to_excel(fileName)

data = []
data2d = []
xPoint = []
yPoint = []
zPoint = []
x2dPoint = []
z2dPoint = []

y0 = 0
c = 0
kxCount = 0
zCount = 0
xCount = 0

for xi in  x:
    for zi in z:
        for kxi in kx:
            for kzi in kz:
                fcosXArray[c, 0] = fCos(a, xi, k0X, kxi)
                fcosZArray[c, 0] = fCos(b, zi, k0Z, kzi)
                fsinXArray[c, 0] = fSin(a, xi, k0X, kxi)
                fsinZArray[c, 0] = fSin(b, zi, k0Z, kzi)

                fcosXi = fCos(a, xi, k0X, kxi)
                fcosZi = fCos(b, zi, k0Z, kzi)
                fsinXi = fSin(a, xi, k0X, kxi)
                fsinZi = fSin(b, zi, k0Z, kzi)
                WxTEmode[c, 0] =  ((1/(k0X**2 + k0Z**2))**2)*fcosXi*fsinZi
                Wxi =  ((1/(k0X**2 + k0Z**2))**2)*fcosXi*fsinZi
                WzTEmode[c, 0] =  ((1/(k0X**2 + k0Z*2))**2)*fcosXi*fsinZi
                Wzi =  ((1/(k0X**2 + k0Z*2))**2)*fcosXi*fsinZi
                kyi = np.sqrt(1 - (kxi**2 + kzi**2))

                x1 = xi + (Wxi * kxi)
                y1 = y0 + np.sqrt(Wxi ** 2 + Wzi ** 2) * kyi
                z1 = zi + (Wzi * kzi)

                xPoint.append(xi)
                xPoint.append(x1)
                xPoint.append(np.nan)
                x2dPoint.append(xi)

                # print('xi = ')
                # print(xi)
                yPoint.append(y0)
                yPoint.append(y1)
                yPoint.append(np.nan)
                zPoint.append(zi)
                zPoint.append(z1)
                zPoint.append(np.nan)
                z2dPoint.append(zi)
                ExiRe, eXi = getReE(xi, kxi, Wxi)
                ExiIm = getImE(xi, kxi, Wxi)
                EziRe, eZi = getReE(zi, kzi, Wzi)
                EziIm = getImE(zi, kzi, Wzi)
                ExReArray[c,0], eXArray[c,0] = getReE(xi, kxi,  Wxi)
                ExImArray[c,0] = getImE(xi, kxi, Wxi)
                EzReArray[c,0], eZArray[c,0] = getReE(zi, kzi, Wzi)
                EzImArray[c,0] = getImE(zi, kzi, Wzi)
                eYi = -(kxi*eXi + kzi*eZi)/kyi

                XinArray[c, 0] = xi
                XinArray[c, 1] = y0
                XinArray[c, 2] = zi
                KinArray[c, 0] = kxi
                KinArray[c, 1] = kyi
                KinArray[c, 2] = kzi
                EinArray[c, 6] = eXi
                EinArray[c, 7] = eYi
                EinArray[c, 8] = eZi
                EinArray[c, 9] = Wxi
                EinArray[c, 8] = Wzi

                c = c + 1
                # print('c = ', c)
            kxCount = kxCount + 1
            # print('kxCount = ', kxCount)

        zCount = zCount + 1
        # print('zCount = ', zCount)
        kxCount = 0

    xCount = xCount+1
    zCount = 0
    # print('xCount = ', xCount)

ExReMax = abs(ExReArray).argmax(0)
ExImMax = abs(ExImArray).argmax(0)
EzReMax = abs(EzReArray).argmax(0)
EzImMax = abs(EzImArray).argmax(0)


ExReArrayN = ExReArray/ExReMax
ExImArrayN = ExImArray/ExImMax
EzReArrayN = EzReArray/EzReMax
EzImArrayN = EzImArray/EzImMax
for i in  range(0,totalSize) :
    print(i)
    EinArray[i, 0] = ExReArrayN[i]
    EinArray[i, 1] = ExImArrayN[i]
    EinArray[i, 2] = 1
    EinArray[i, 3] = 1
    EinArray[i, 4] = EzReArrayN[i]
    EinArray[i, 5] = EzImArrayN[i]

raysDF = setRaysDataFrame(XinArray, KinArray, EinArray)

pathRay  =  '/home/konstantin/PycharmProjects/RayTracer/result/FromWigner/RinWignerDis_0_1.xls'
saveRays2Execel(pathRay, raysDF)

trace_Rays = dict(
            go.Scatter3d(x=xPoint, y=yPoint, z=zPoint,
                         mode='lines',
                         name='rayIn',
                         line=dict(width=1, color='blue')
                         )
                    )
trace_2d = dict(
                go.Scatter(
                x=x2dPoint,
                y=z2dPoint,
                mode='markers'
                 )
                )
data.append(trace_Rays)
data2d.append(trace_2d)

Wxmax = np.abs(WxTEmode).argmax(0)
WxmaxN = WxTEmode/Wxmax
Wzmax = np.abs(WzTEmode).argmax(0)
WzmaxN = WzTEmode/Wzmax


def setLayout():
    layout = dict(width=1920, height=1200,
                  xaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                  yaxis=dict(range=[-10, 10], autorange=True, zeroline=False),
                  title='Mirror ', hovermode='closest',
                  # updatemenus=[{'type': 'buttons',
                  #               'buttons': [{'label': 'Play',
                  #                            'method': 'animate',
                  #                            'args': [None]}]}]
                  )
    return layout

# print(WzTEmode)

#######################################################################################################
# Ploting

layout = setLayout()
fig = dict(data=data, layout=layout)
fig1 = dict(data = data2d, layout = layout)
py.offline.plot(fig, filename='E.html')
py.offline.plot(fig1, filename='Ein.html')
