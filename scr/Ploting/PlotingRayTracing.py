import plotly as py
import numpy as np
from numpy import sin, cos, pi
import pandas as pd
import plotly.tools as tls
import plotly.graph_objs  as go
import scr.RayTracing.Rays as rt
from scr.MainParam import Parametrs
from scr.RayTracing.Rays import Rays

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

class PlotingRayTracing:
    def __init__(self, mirrorDataSheet, mirrorIndex, RinDF, Rreflected, rNormal, fileName):
        self.MirrorDF = mirrorDataSheet
        self.mirrorIndex = mirrorIndex
        self.plotFileName = fileName
        self.rayInDF = RinDF
        self.rayReflected = Rreflected
        self.rayNormal = rNormal
        #self.rayInDict, self.rayReflectedDict, self.pInData, self.rayInDictMarkers, self.rayReflectedDictMarkers = self.setRays4Plot(mirrorDataSheet)
        self.rayInDict, self.rayReflectedDict = self.setRays4Plot()
        self.layout = self.setLayout()
        self.Tline1, self.Tline2 = self.getTlineDict()

    def setRays4Plot(self):

        xRayInData = []
        yRayInData = []
        zRayInData = []

        xRayReflectedData = []
        yRayReflectedData = []
        zRayReflectedData = []

        #Construct List of pairs of Rays
        for  rIndex in self.rayInDF.index:

            #  In DATA
            xRayInData.append(self.rayInDF.X[rIndex] + self.MirrorDF.Source[0])
            xRayInData.append(self.rayNormal.X[rIndex])
            xRayInData.append(np.nan)

            yRayInData.append(self.rayInDF.Y[rIndex] + self.MirrorDF.Source[1])
            yRayInData.append(self.rayNormal.Y[rIndex])
            yRayInData.append(np.nan)

            zRayInData.append(self.rayInDF.Z[rIndex] + self.MirrorDF.Source[2])
            zRayInData.append(self.rayNormal.Z[rIndex])
            zRayInData.append(np.nan)

            #  Reflected Data
            xRayReflectedData.append(self.rayNormal.X[rIndex])
            xRayReflectedData.append(self.rayReflected.X[rIndex] + self.MirrorDF.Detector[0])
            xRayReflectedData.append(np.nan)

            yRayReflectedData.append(self.rayNormal.Y[rIndex])
            yRayReflectedData.append(self.rayReflected.Y[rIndex] + self.MirrorDF.Detector[1])
            yRayReflectedData.append(np.nan)

            zRayReflectedData.append(self.rayNormal.Z[rIndex])
            zRayReflectedData.append(self.rayReflected.Z[rIndex] + self.MirrorDF.Detector[2])
            zRayReflectedData.append(np.nan)

        rayInDict = dict(
            go.Scatter3d(x=xRayInData, y=yRayInData, z=zRayInData,
                         mode='lines',
                         name='rayIn' + str(self.mirrorIndex),
                         line=dict(width=2, color='blue')
                         ))

        rayReflectedDict = dict(
            go.Scatter3d(x=xRayReflectedData, y=yRayReflectedData, z=zRayReflectedData,
                         mode = 'lines',
                         name = 'rayReflected' + str(self.mirrorIndex),
                         line = dict(width=2, color='red')
                         ))
        return rayInDict, rayReflectedDict

    def setLayout(self):
        layout = go.Layout(width=1920, height=1200,
                            autosize=False,
                            margin=dict(
                            autoexpand=False),
                            xaxis=dict(autorange=False, range=[-130, 130],  zeroline=True),
                            yaxis=dict( anchor="x", scaleratio=1, domain = [0, 0.45], autorange=True, zeroline=False),
                            title='Ray Tracing ', hovermode='closest',
                            )
        return layout

    def plotIs(self, data, layout):
        fig = dict(data = data, layout = layout)
        print('plotFileName = ')
        print(self.plotFileName)
        py.offline.plot(fig, self.plotFileName)

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


    def setMirrorSurf(self):
        rayDFtemp = []

        v1 = self.MirrorDF.Vertex.x
        v2 = self.MirrorDF.Vertex.y
        v3 = self.MirrorDF.Vertex.z
        xDegree = self.MirrorDF.Direction.x
        yDegree = self.MirrorDF.Direction.y
        zDegree = self.MirrorDF.Direction.z

        xLim1 = self.MirrorDF.Lim1.x
        yLim1 = self.MirrorDF.Lim1.y
        zLim1 = self.MirrorDF.Lim1.z

        xLim2 = self.MirrorDF.Lim2.x
        yLim2 = self.MirrorDF.Lim2.y
        zLim2 = self.MirrorDF.Lim2.z

        x1Focus = self.MirrorDF.Focus.x
        x2Focus = self.MirrorDF.Focus.z

        a11 = 1 / (4 * self.MirrorDF.Focus[0])
        a22 = 1 / (4 * self.MirrorDF.Focus[2])
        a3 = 1

        MrNegativ = self.getRotateMatrix(xDegree, yDegree, zDegree)
        M2Positive = self.getRotateMatrix(-xDegree, -yDegree, -zDegree)

        # x3R = (xLim1 - v1) * Mr[2, 0] + (yLim1 - v2) * Mr[2, 1] + (zLim1 - v3) * Mr[2, 2]

        # x1Lim1 = ((xLim1 - v1) * MrNegativ[0, 0] + (yLim1 - v2) * MrNegativ[0, 1] + (zLim1 - v3) * MrNegativ[0, 2]) + v1
        # x1Lim2 = ((xLim2 - v1) * MrNegativ[0, 0] + (yLim2 - v2) * MrNegativ[0, 1] + (zLim2 - v3) * MrNegativ[0, 2]) + v1
        #
        # x2Lim1 = ((xLim1 - v1) * MrNegativ[1, 0] + (yLim1 - v2) * MrNegativ[1, 1] + (zLim1 - v3) * MrNegativ[1, 2]) + v2
        # x2Lim2 = ((xLim2 - v1) * MrNegativ[1, 0] + (yLim2 - v2) * MrNegativ[1, 1] + (zLim2 - v3) * MrNegativ[1, 2]) + v2

        x1Lim1 = ((xLim1 - v1) * MrNegativ[0, 0] + (yLim1 - v2) * MrNegativ[1, 0] + (zLim1 - v3) * MrNegativ[2, 0]) + v1
        x1Lim2 = ((xLim2 - v1) * MrNegativ[0, 0] + (yLim2 - v2) * MrNegativ[1, 0] + (zLim2 - v3) * MrNegativ[2, 0]) + v1

        x2Lim1 = ((xLim1 - v1) * MrNegativ[0, 1] + (yLim1 - v2) * MrNegativ[1, 1] + (zLim1 - v3) * MrNegativ[2, 1]) + v2
        x2Lim2 = ((xLim2 - v1) * MrNegativ[0, 1] + (yLim2 - v2) * MrNegativ[1, 1] + (zLim2 - v3) * MrNegativ[2, 1]) + v2

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

        x1R = ((X1Mesh - v1)*M2Positive[0, 0] +
               (X2Mesh - v2)*M2Positive[1, 0] +
               (X3Mesh - v3)*M2Positive[2, 0]) + v1

        x2R = ((X1Mesh - v1)*M2Positive[0, 1] +
               (X2Mesh - v2)*M2Positive[1, 1] +
               (X3Mesh - v3)*M2Positive[2, 1]) + v2

        x3R = ((X1Mesh - v1)*M2Positive[0, 2] +
               (X2Mesh - v2)*M2Positive[1, 2] +
               (X3Mesh - v3)*M2Positive[2, 2]) +v3
        SurfDict = dict(
                        go.Surface(x=x1R, y=x2R, z=x3R,
                        showscale=False,
                        opacity=1,
                        type='surface',
                        surfacecolor='blue',
                        name=str(self.mirrorIndex)))

        return  SurfDict

    def getRotateMatrix(self, xDegree, yDegree, zDegree):
        csX = self.cs(xDegree)
        csY = self.cs(yDegree)
        csZ = self.cs(zDegree)

        snX = self.sn(xDegree)
        snY = self.sn(yDegree)
        snZ = self.sn(zDegree)

        Rx = np.array([
            [1, 0, 0],
            [0, csX, -snX],
            [0, snX, csX]
        ])
        Ry = np.array([
            [csY, 0, -snY],
            [0, 1, 0],
            [snY, 0, csY]
        ])
        Rz = np.array([
            [csZ, -snZ, 0],
            [snZ, csZ, 0],
            [0, 0, 1]
        ])
        Mr = (Rx.dot(Ry)).dot(Rz)
        return Mr

    def cs(self, alphaDegree):
        alphaRadian = self.degree2Radian(alphaDegree)
        if np.abs(cos(alphaRadian)) < 1e-4:
            csAlpha = 0
        else:
            csAlpha = cos(alphaRadian)
        return csAlpha

    def sn(self, alphaDegree):
        alphaRadian = self.degree2Radian(alphaDegree)
        if np.abs(sin(alphaRadian)) < 1e-4:
            snAlpha = 0
        else:
            snAlpha = sin(alphaRadian)
        return snAlpha

    def degree2Radian(self, alphaDegree):
        return (alphaDegree * pi) / 180
