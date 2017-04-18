
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

        # print(RaysInObject.dataSheet)
        # print(RayReflectedObject.dataSheet)
        # print(RaysNormalObject.dataSheet)
        #print(mirrorDataSheet)

        rayReflectedDict = {}
        xRayInData = []
        yRayInData = []
        zRayInData = []

        xRayReflectedData = []
        yRayReflectedData = []
        zRayReflectedData = []

        xRayNormalData = []
        yRayNormalData = []
        zRayNormalData = []
        #Construct List of pairs of Rays
        for  rIndex in RaysInObject.dataSheet.index:
            # print(rIndex)
            xRayInData.append(RaysInObject.dataSheet.Xin[rIndex] + mirrorDataSheet.Source[0])
            xRayInData.append(RaysNormalObject.dataSheet.Xin[rIndex])

            yRayInData.append(RaysInObject.dataSheet.Yin[rIndex] + mirrorDataSheet.Source[1])
            yRayInData.append(RaysNormalObject.dataSheet.Yin[rIndex])

            zRayInData.append(RaysInObject.dataSheet.Zin[rIndex] + mirrorDataSheet.Source[2])
            zRayInData.append(RaysNormalObject.dataSheet.Zin[rIndex])
            ##########################
            xRayReflectedData.append(RaysNormalObject.dataSheet.Xin[rIndex])
            xRayReflectedData.append(RayReflectedObject.dataSheet.Xin[rIndex] + mirrorDataSheet.Detector[0])

            yRayReflectedData.append(RaysNormalObject.dataSheet.Yin[rIndex])
            yRayReflectedData.append(RayReflectedObject.dataSheet.Yin[rIndex] + mirrorDataSheet.Detector[1])

            zRayReflectedData.append(RaysNormalObject.dataSheet.Zin[rIndex])
            zRayReflectedData.append(RayReflectedObject.dataSheet.Zin[rIndex] + mirrorDataSheet.Detector[2])
            #########################

        rayInDict = dict(
            go.Scatter3d(x=xRayInData, y=yRayInData, z=zRayInData,
                         mode='lines',
                         name='rayIn'+self.mirrorList,
                         line=dict(width=2, color='blue')
                         ))
        rayReflectedDict = dict(
            go.Scatter3d(x=xRayReflectedData, y=yRayReflectedData, z=zRayReflectedData,
                         mode='lines',
                         name='rayReflected' + self.mirrorList,
                         line=dict(width=2, color='red')
                         ))

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
        py.offline.plot(fig, filename='line-mode.html')

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

        MrNegativ = rayObject.getRotateMatrix(-xDegree, -yDegree, -zDegree)
        M2Positive = rayObject.getRotateMatrix(xDegree, yDegree, zDegree)

        # x3R = (xLim1 - v1) * Mr[2, 0] + (yLim1 - v2) * Mr[2, 1] + (zLim1 - v3) * Mr[2, 2]

        x1Lim1 = ((xLim1 - v1) * MrNegativ[0, 0] + (yLim1 - v2) * MrNegativ[0, 1] + (zLim1 - v3) * MrNegativ[0, 2]) + v1
        x1Lim2 = ((xLim1 - v1) * MrNegativ[0, 0] + (yLim1 - v2) * MrNegativ[0, 1] + (zLim1 - v3) * MrNegativ[0, 2]) + v1

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

        x1R = (X1Mesh - v1) * M2Positive[0, 0] + (X2Mesh- v2) * M2Positive[0, 1] + (X3Mesh - v3) * M2Positive[0, 2]
        x2R = (X1Mesh - v1) * M2Positive[1, 0] + (X2Mesh- v2) * M2Positive[1, 1] + (X3Mesh - v3) * M2Positive[1, 2]
        x3R = (X1Mesh - v1) * M2Positive[2, 0] + (X2Mesh- v2) * M2Positive[2, 1] + (X3Mesh - v3) * M2Positive[2, 2]