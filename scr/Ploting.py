
import plotly as py
import numpy as np
import pandas as pd
import plotly.tools as tls
import plotly.graph_objs  as go

from scr.MainParam import Parametrs
from scr.Rays import Rays

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

class Ploting:
    def __init__(self, path, mirrorDataSheet, mirrorList):
        self.mirrorList = mirrorList
        self.rayInDict, self.rayReflectedDict = self.setRays4Plot(path, mirrorDataSheet)
        self.layout = self.setLayout()
        self.Tline1, self.Tline2 = self.getTlineDict()

    def setRays4Plot(self, path, mirrorDataSheet):
        fName = path[1]
        pathInRay = path[0] + fName[0] + path[2]
        pathReflctedRay = path[0] + fName[1] + path[2]
        pathNormalRay = path[0] + fName[2] + path[2]

        RaysInObject = Parametrs(pathInRay, 'Sheet1')
        RayReflectedObject = Parametrs(pathReflctedRay, 'Sheet1')
        RaysNormalObject = Parametrs(pathNormalRay, 'Sheet1')
        ##RayPolarIn = Parametrs(pathInRay, 'Sheet1')
        ##RayPolarNormal = Parametrs(pathNormalRay, 'Sheet1')
        ##RayPolarDetector = Parametrs(pathReflctedRay, 'Sheet1')
        # print(RaysInObject.dataSheet)
        # print(RayReflectedObject.dataSheet)
        # print(RaysNormalObject.dataSheet)
        #print(mirrorDataSheet)

        xRayInData = []
        yRayInData = []
        zRayInData = []

        xRayInData2d = []
        yRayInData2d = []
        zRayInData2d = []

        xPolarInData = []
        yPolarInData = []
        zPolarInData = []

        xRayReflectedData = []
        yRayReflectedData = []
        zRayReflectedData = []

        xRayReflectedData2d = []
        yRayReflectedData2d = []
        zRayReflectedData2d = []

        xPolarReflectedData = []
        yPolarReflectedData = []
        zPolarReflectedData = []

        xRayNormalData = []
        yRayNormalData = []
        zRayNormalData = []
        xpolarNormalData = []
        ypolarNormalData = []
        zpolarNormalData = []
        rayInData2dDict = []
        rayReflectedDict2d = []
        #Construct List of pairs of Rays
        for  rIndex in RaysInObject.dataSheet.index:
            # print(rIndex)
            #  In DATA
            xRayInData.append(RaysInObject.dataSheet.Xin[rIndex] + mirrorDataSheet.Source[0])
            xRayInData.append(RaysNormalObject.dataSheet.Xin[rIndex])
            xRayInData.append(np.nan)

            xRayInData2d.append(RaysInObject.dataSheet.Xin[rIndex] + mirrorDataSheet.Source[0])
            yRayInData2d.append(RaysInObject.dataSheet.Yin[rIndex] + mirrorDataSheet.Source[1])
            zRayInData2d.append(RaysInObject.dataSheet.Zin[rIndex] + mirrorDataSheet.Source[2])

            xPolarInData.append(RaysInObject.dataSheet.Xin[rIndex] + mirrorDataSheet.Source[0])
            xPolarInData.append(RaysInObject.dataSheet.Xe[rIndex] + mirrorDataSheet.Source[0] )
            xPolarInData.append(np.nan)

            yRayInData.append(RaysInObject.dataSheet.Yin[rIndex] + mirrorDataSheet.Source[1])
            yRayInData.append(RaysNormalObject.dataSheet.Yin[rIndex])
            yRayInData.append(np.nan)

            yPolarInData.append(RaysInObject.dataSheet.Yin[rIndex] + mirrorDataSheet.Source[1])
            yPolarInData.append(RaysInObject.dataSheet.Ye[rIndex] + mirrorDataSheet.Source[1])
            yPolarInData.append(np.nan)

            zRayInData.append(RaysInObject.dataSheet.Zin[rIndex] + mirrorDataSheet.Source[2])
            zRayInData.append(RaysNormalObject.dataSheet.Zin[rIndex])
            zRayInData.append(np.nan)

            zPolarInData.append(RaysInObject.dataSheet.Zin[rIndex] + mirrorDataSheet.Source[2])
            zPolarInData.append(RaysInObject.dataSheet.Ze[rIndex] + mirrorDataSheet.Source[2])
            zPolarInData.append(np.nan)
            #  Reflected Data
            xRayReflectedData.append(RaysNormalObject.dataSheet.Xin[rIndex])
            xRayReflectedData.append(RayReflectedObject.dataSheet.Xin[rIndex] + mirrorDataSheet.Detector[0])
            xRayReflectedData.append(np.nan)

            xRayReflectedData2d.append(RayReflectedObject.dataSheet.Xin[rIndex] + mirrorDataSheet.Detector[0])
            yRayReflectedData2d.append(RayReflectedObject.dataSheet.Yin[rIndex] + mirrorDataSheet.Detector[1])
            zRayReflectedData2d.append(RayReflectedObject.dataSheet.Zin[rIndex] + mirrorDataSheet.Detector[2])

            xPolarReflectedData.append(RaysNormalObject.dataSheet.Xin[rIndex])
            xPolarReflectedData.append(RayReflectedObject.dataSheet.Xe[rIndex] )
            xPolarReflectedData.append(np.nan)

            yRayReflectedData.append(RaysNormalObject.dataSheet.Yin[rIndex])
            yRayReflectedData.append(RayReflectedObject.dataSheet.Yin[rIndex] + mirrorDataSheet.Detector[1])
            yRayReflectedData.append(np.nan)

            yPolarReflectedData.append(RaysNormalObject.dataSheet.Yin[rIndex])
            yPolarReflectedData.append(RayReflectedObject.dataSheet.Ye[rIndex])
            yPolarReflectedData.append(np.nan)

            zRayReflectedData.append(RaysNormalObject.dataSheet.Zin[rIndex])
            zRayReflectedData.append(RayReflectedObject.dataSheet.Zin[rIndex] + mirrorDataSheet.Detector[2])
            zRayReflectedData.append(np.nan)

            zPolarReflectedData.append(RaysNormalObject.dataSheet.Zin[rIndex])
            zPolarReflectedData.append(RayReflectedObject.dataSheet.Ze[rIndex])
            zPolarReflectedData.append(np.nan)
            #########################

        rayInDict = dict(
            go.Scatter3d(x=xRayInData, y=yRayInData, z=zRayInData,
                         mode='lines',
                         name='rayIn'+self.mirrorList,
                         line=dict(width=2, color='blue')
                         ))
        rayReflectedDict = dict(
            go.Scatter3d(x=xRayReflectedData, y=yRayReflectedData, z=zRayReflectedData,
                         mode = 'lines',
                         name = 'rayReflected' + self.mirrorList,
                         line = dict(width=2, color='red')
                         ))

        # PolarInDict = dict(
        #     go.Scatter3d(x=xPolarInData, y=yPolarInData, z=zPolarInData,
        #                  mode='lines',
        #                  name='PolarIn' + self.mirrorList,
        #                  line=dict(width=2, color='blue')
        #                  ))
        # PolarReflectedDict = dict(
        #     go.Scatter3d(x=xPolarReflectedData, y=yPolarReflectedData, z=zPolarReflectedData,
        #                  mode='lines',
        #                  name='PolarReflected' + self.mirrorList,
        #                  line=dict(width=2, color='blue')
        #                  ))
        # if self.mirrorList== 'Mirror1':
        #     rayInData2dDict =  dict(
        #                     go.Scatter(x=xRayInData2d, y=zRayInData2d,
        #                     mode='markers',
        #                     name='RayIn' + self.mirrorList,
        #                     ))
        #     rayReflectedDict2d =  dict(
        #                     go.Scatter(x=xRayReflectedData2d, y=yRayReflectedData2d,
        #                     mode='markers',
        #                     name='RayRef' + self.mirrorList,
        #                     ))
        #
        # elif self.mirrorList== 'Mirror2':
        #     rayInData2dDict = dict(
        #         go.Scatter(x=xRayInData2d, y=yRayInData2d,
        #                      mode='markers',
        #                      name='RayIn' + self.mirrorList,
        #                      ))
        #     rayReflectedDict2d = dict(
        #         go.Scatter(x=xRayReflectedData2d, y=zRayReflectedData2d,
        #                    mode='markers',
        #                    name='RayRef' + self.mirrorList,
        #                    ))

        return rayInDict, rayReflectedDict

    def setLayout(self):
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

    def plotIs(self, data, layout):
        #print('Data = ', data)
        fig = dict(data=data, layout=layout)
        py.offline.plot(fig, filename='result/htmlFiles/42RaysforTest MAtrix.html')

    def getTlineDict(self):
        xTLine1 = [-125, -125, -125, -125, -125, -125, -125, 3675, 3675, 3675]
        yTLine1 = [-400, 125, 125, 125, 125, 4125, 4125, 4125, 4125, 4125]
        zTLine1 = [-125, -125, -125, 1175, 1175, 1175, 1175, 1175, 1175, 600]

        xTLine2 = [125, 125, 125, 125, 125, 125, 125, 3925, 3925, 3925]
        yTLine2 = [-400, -125, -125, -125, -125, 3875, 3875, 3875, 3875, 3875]
        zTLine2 = [125, 125, 125, 1425, 1425, 1425, 1425, 1425, 1425, 600]

        tLine1 = dict(
            go.Scatter3d(x=xTLine1, y=yTLine1, z=zTLine1,
                         mode='lines',
                         name='Tline1',
                         line=dict(width=2, color='black')
                         ))
        tLine2 = dict(
            go.Scatter3d(x=xTLine2, y=yTLine2, z=zTLine2,
                         mode='lines',
                         name='TLine2',
                         line=dict(width=2, color='black')
                         ))
        return tLine1, tLine2

    def setMirrorSurf(self, mirroDataSheet):
        rayObject = Rays()

        v1 = mirroDataSheet.Vertex.x
        v2 = mirroDataSheet.Vertex.y
        v3 = mirroDataSheet.Vertex.z
        xDegree = mirroDataSheet.Direction.x
        yDegree = mirroDataSheet.Direction.y
        zDegree = mirroDataSheet.Direction.z

        xLim1 = mirroDataSheet.Lim1.x
        yLim1 = mirroDataSheet.Lim1.y
        zLim1 = mirroDataSheet.Lim1.z

        xLim2 = mirroDataSheet.Lim2.x
        yLim2 = mirroDataSheet.Lim2.y
        zLim2 = mirroDataSheet.Lim2.z

        x1Focus = mirroDataSheet.Focus.x
        x2Focus = mirroDataSheet.Focus.z

        a11 = 1 / (4 * mirroDataSheet.Focus[0])
        a22 = 1 / (4 * mirroDataSheet.Focus[2])
        a3 = 1

        MrNegativ = rayObject.getRotateMatrix(xDegree, yDegree, zDegree)
        M2Positive = rayObject.getRotateMatrix(-xDegree, -yDegree, -zDegree)

        # x3R = (xLim1 - v1) * Mr[2, 0] + (yLim1 - v2) * Mr[2, 1] + (zLim1 - v3) * Mr[2, 2]

        x1Lim1 = ((xLim1 - v1) * MrNegativ[0, 0] + (yLim1 - v2) * MrNegativ[0, 1] + (zLim1 - v3) * MrNegativ[0, 2]) + v1
        x1Lim2 = ((xLim2 - v1) * MrNegativ[0, 0] + (yLim2 - v2) * MrNegativ[0, 1] + (zLim2 - v3) * MrNegativ[0, 2]) + v1

        x2Lim1 = ((xLim1 - v1) * MrNegativ[1, 0] + (yLim1 - v2) * MrNegativ[1, 1] + (zLim1 - v3) * MrNegativ[1, 2]) + v2
        x2Lim2 = ((xLim2 - v1) * MrNegativ[1, 0] + (yLim2 - v2) * MrNegativ[1, 1] + (zLim2 - v3) * MrNegativ[1, 2]) + v2

        if x1Lim1 < x1Lim2:
            x1array = np.linspace(x1Lim1, x1Lim2,10)
        else:
            x1array = np.linspace(x1Lim2, x1Lim1, 10)

        if x2Lim1 < x2Lim2:
            x2array = np.linspace(x2Lim1, x2Lim2, 10)
        else:
            x2array = np.linspace(x2Lim2, x2Lim1, 10)


        X1Mesh, X2Mesh = np.meshgrid(x1array, x2array)

        X3Mesh = (a11*((X1Mesh-v1)**2) + a22*((X2Mesh-v2)**2)) + v3

        # x1R = ((X1Mesh - v1) * M2Positive[0, 0] + (X2Mesh - v2) * M2Positive[0, 1] + (X3Mesh - v3) * M2Positive[0, 2]) + v1
        # x2R = ((X1Mesh - v1) * M2Positive[1, 0] + (X2Mesh - v2) * M2Positive[1, 1] + (X3Mesh - v3) * M2Positive[1, 2]) + v2
        # x3R = ((X1Mesh - v1) * M2Positive[2, 0] + (X2Mesh - v2) * M2Positive[2, 1] + (X3Mesh - v3) * M2Positive[2, 2]) + v3

        x1R = ((X1Mesh - v1)*M2Positive[0, 0] +
               (X2Mesh - v2)*M2Positive[0, 1] +
               (X3Mesh - v3)*M2Positive[0, 2]) + v1

        x2R = ((X1Mesh - v1)*M2Positive[1, 0] +
               (X2Mesh - v2)*M2Positive[1, 1] +
               (X3Mesh - v3)*M2Positive[1, 2]) + v2

        x3R = ((X1Mesh - v1)*M2Positive[2, 0] +
               (X2Mesh - v2)*M2Positive[2, 1] +
               (X3Mesh - v3)*M2Positive[2, 2]) +v3

        return  dict(
                    go.Surface(x=x1R, y=x2R, z=x3R,
                            showscale = False,
                            opacity = 1,
                            type = 'surface',
                            surfacecolor = 'blue',
                            name = 'Mirror1'))