import plotly as py
import numpy as np
import pandas as pd
import plotly.tools as tls
import plotly.graph_objs  as go

from scr.MainParam import Parametrs

py.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

class Plotpolarization:
    def __init__(self, mirrorDataSheet, RinDF, Rreflected, rNormal, mirrorIndex, fileName):
        self.MirrorDF = mirrorDataSheet
        self.mirrorIndex= mirrorIndex
        self.plotFileName = fileName
        self.rayInDF = RinDF
        self.rayReflected = Rreflected
        self.rayNormal = rNormal
        self.L = 400
        # self.Rays4Plot_All = self.setRays4Plot_All()

        self.layout = self.setLayout()

    def setRays4Plot_All(self):

        dataInX1 = []
        dataInY1 = []
        dataInZ1 = []

        # Construct List of pairs of Rays
        for rIndex in self.rayInDF.index:
            if self.mirrorIndex == 'Mirror1':

                dataInX1.append(self.rayInDF.Xin[rIndex])
                dataInX1.append(self.rayReflected.Xin[rIndex])
                dataInX1.append(np.nan)

                dataInY1.append(0)
                dataInY1.append(self.L)
                dataInY1.append(np.nan)

                dataInZ1.append(self.rayInDF.Zin[rIndex])
                dataInZ1.append(self.rayReflected.Yin[rIndex])
                dataInZ1.append(np.nan)

            elif self.mirrorIndex == 'Mirror2':

                dataInX1.append(self.rayInDF.Xin[rIndex])
                dataInX1.append(self.rayReflected.Xin[rIndex])
                dataInX1.append(np.nan)

                dataInY1.append(0)
                dataInY1.append(self.L)
                dataInY1.append(np.nan)

                dataInZ1.append(self.rayInDF.Yin[rIndex])
                dataInZ1.append(self.rayReflected.Zin[rIndex])
                dataInZ1.append(np.nan)
            else:
                print('Mirror Name not Corrected')

        rayInDict = dict(
            go.Scatter3d(x=dataInX1, y=dataInY1, z=dataInZ1,
                         mode = 'line-markers',
                         name ='rayIn_' + str(self.mirrorIndex),
                         line=dict(width=2)
                         ))
        return rayInDict

    def setLayout(self):
        layout = dict(width=1920, height=1200,
                      xaxis=dict(range=[-100, 100], autorange=True, zeroline=True),
                      yaxis=dict(range=[-100, 100], autorange=True, zeroline=True),
                      title='Rayin vs RayOut_', hovermode='closest',
                      )
        return layout

    def setRays4plotSection(self,  iS, iF, color):

        xIndata1 = []
        yIndata1 = []
        zIndata1 = []
        dataIn1 = []

        xInOutData = []
        yInOutData = []
        zInOutData = []
        inOutData = []

        ExInData = []
        EyInData = []
        EzInData = []
        eInData = []

        ExOutData = []
        EyOutData = []
        EzOutData = []
        eOutData = []

        xOutdata1 = []
        yOutdata1 = []
        zOutdata1 = []
        dataOut1 = []

        ExInOutData = []
        EyInOutData = []
        EzInOutData = []
        eInDOutata = []


        Ain=50
        for i in range(iS, iF):
            if self.mirrorIndex == 'Mirror1':
               xIndata1.append(self.rayInDF.Xin[i])
               yIndata1.append(0)
               zIndata1.append(self.rayInDF.Zin[i])

               xOutdata1.append(self.rayReflected.Xin[i])
               yOutdata1.append(self.L)
               zOutdata1.append(self.rayReflected.Yin[i])

               xInOutData.append(self.rayInDF.Xin[i])
               xInOutData.append(self.rayReflected.Xin[i])
               xInOutData.append(np.nan)

               yInOutData.append(0)
               yInOutData.append(self.L)
               yInOutData.append(np.nan)

               zInOutData.append(self.rayInDF.Zin[i])
               zInOutData.append(self.rayReflected.Yin[i])
               zInOutData.append(np.nan)

               ExInData.append(self.rayInDF.Xin[i] )
               ExInData.append(self.rayInDF.Xin[i]  + Ain * self.rayInDF.Exin[i])
               ExInData.append(np.nan)

               EyInData.append(0)
               EyInData.append(Ain * self.rayInDF.Eyin[i])
               EyInData.append(np.nan)

               EzInData.append(self.rayInDF.Zin[i])
               EzInData.append(self.rayInDF.Zin[i] + Ain * self.rayInDF.Ezin[i])
               EzInData.append(np.nan)

            elif  self.mirrorIndex == 'Mirror2':
                xIndata1.append(self.rayInDF.Xin[i])
                yIndata1.append(0)
                zIndata1.append(self.rayInDF.Yin[i])

                xOutdata1.append(self.rayReflected.Xin[i])
                yOutdata1.append(400)
                zOutdata1.append(self.rayReflected.Zin[i])

                xInOutData.append(self.rayInDF.Xin[i])
                xInOutData.append(self.rayReflected.Xin[i])
                xInOutData.append(np.nan)

                yInOutData.append(self.L)
                yInOutData.append(2*self.L)
                yInOutData.append(np.nan)

                zInOutData.append(self.rayInDF.Yin[i])
                zInOutData.append(self.rayReflected.Zin[i])
                zInOutData.append(np.nan)

                ExOutData.append(self.rayReflected.Xin[i])
                ExOutData.append(self.rayReflected.Xe[i])
                ExOutData.append(np.nan)

                EyOutData.append(2*self.L)
                EyOutData.append(2*self.L +self.rayReflected.Ye[i])
                EyOutData.append(np.nan)

                EzOutData.append(self.rayReflected.Yin[i])
                EzOutData.append(self.rayReflected.Ze[i])
                EzOutData.append(np.nan)

        dataIn1.append(xIndata1)
        dataIn1.append(yIndata1)
        dataIn1.append(zIndata1)


        dataOut1.append(xOutdata1)
        dataOut1.append(yOutdata1)
        dataOut1.append(zOutdata1)

        rayInDict = dict()
        rayOutDict = dict()

        eInData.append(ExInData)
        eInData.append(EyInData)
        eInData.append(EzInData)

        eOutData.append(ExOutData)
        eOutData.append(EyOutData)
        eOutData.append(EzOutData)

        rayInDict = dict(
                        go.Scatter3d(   x=xIndata1,
                                        y=yIndata1,
                                        z=zIndata1,
                                        mode='markers',
                                        name='rayIn_' + str(self.mirrorIndex)  +'_' +str(iS) +'_' + str(iF),
                                        line=dict(width=2, color=color)
                                    ))
        rayOutDict = dict(
                        go.Scatter3d(   x=xOutdata1,
                                        y=yOutdata1,
                                        z=zOutdata1,
                                        mode='markers',
                                        name='Rout_' + str(self.mirrorIndex) +'_' +str(iS) +'_' + str(iF),
                                        line=dict(width=2, color=color)
                                      ))
        rayInOutDict = dict(
                        go.Scatter3d(   x=xInOutData,
                                        y=yInOutData,
                                        z=zInOutData,
                                        mode='line-markers',
                                        name='R_In_Out_' + str(self.mirrorIndex) +'_' +str(iS) +'_' + str(iF),
                                        line=dict(width=2, color=color)
                                     ))

        PeInDict = dict(
                            go.Scatter3d(x=ExInData,
                            y=EyInData,
                             z=EzInData,
                            mode='line-markers',
                            name='P_In_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                            line=dict(width=2, color = 'green')
                             ))
        PeOutDict = dict(
            go.Scatter3d(x=ExOutData,
                         y=EyOutData,
                         z=EzOutData,
                         mode='line-markers',
                         name='P_Out_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color = 'bue')
                         ))
        return rayInDict, rayOutDict, rayInOutDict, PeInDict, PeOutDict

    ##                 R 1 - R 2

    def setRays4plot_R1_R2_Section_markers(self, R1, R2, iS, iF, color):

        xIndata = []
        yIndata = []
        zIndata = []
        dataIn = []

        xOutdata = []
        yOutdata = []
        zOutdata = []
        dataOut = []

        Ain = 50
        for i in range(iS, iF):
            xIndata.append(R1.Xin[i])
            yIndata.append(0)
            zIndata.append(R1.Zin[i])

            xOutdata.append(R2.Xin[i])
            yOutdata.append(2*self.L)
            zOutdata.append(R2.Yin[i])

        dataIn.append(xIndata)
        dataIn.append(yIndata)
        dataIn.append(zIndata)

        dataOut.append(xOutdata)
        dataOut.append(yOutdata)
        dataOut.append(zOutdata)

        rayInDict = dict(
            go.Scatter3d(x=xIndata,
                         y=yIndata,
                         z=zIndata,
                         mode='markers',
                         name='rayIn_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))
        rayOutDict = dict(
            go.Scatter3d(x=xOutdata,
                         y=yOutdata,
                         z=zOutdata,
                         mode='markers',
                         name='Rout_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))
        return rayInDict, rayOutDict

    def setPolRays4Plot_R1_R2_Section_0_1(self, R1, R2, iS, iF):

        ExIndata = []
        EyIndata = []
        EzIndata = []

        ExOutdata = []
        EyOutdata = []
        EzOutdata = []

        Ain = 15
        for i in range(iS, iF):
            ##  Polarizaation IN

            ExIndata.append(R1.Xin[i])
            ExIndata.append(R1.Xin[i] + Ain*R1.Exin[i])
            ExIndata.append(np.nan)

            EyIndata.append(0)
            EyIndata.append(Ain * R1.Eyin[i])
            EyIndata.append(np.nan)

            EzIndata.append(R1.Zin[i])
            EzIndata.append(R1.Zin[i] + Ain * R1.Ezin[i])
            EzIndata.append(np.nan)

            ## Polarization OUT
            ExOutdata.append(R2.Xin[i])
            ExOutdata.append(R2.Xe[i])
            ExOutdata.append(np.nan)

            EyOutdata.append(2*self.L )
            EyOutdata.append(2*self.L + R2.Ze[i])
            EyOutdata.append(np.nan)

            EzOutdata.append(R2.Yin[i])
            EzOutdata.append(R2.Ye[i])
            EzOutdata.append(np.nan)

        PrayInDict = dict(
            go.Scatter3d(x=ExIndata,
                         y=EyIndata,
                         z=EzIndata,
                         mode='Lines',
                         name='PIn_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='red')
                         ))
        PrayOutDict = dict(
            go.Scatter3d(x=ExOutdata,
                         y=EyOutdata,
                         z=EzOutdata,
                         mode='Lines',
                         name='Pout_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='green')
                         ))
        return PrayInDict, PrayOutDict

    def setPolRays4Plot_R1_R2_Section_direction_0_1_loop(self, R1, R2, iS, iF):

        ExInOutdata = []
        EyInOutdata = []
        EzInOutdata = []

        Ain = 15
        for i in range(iS, iF):
            ##  Polarizaation IN

            ExInOutdata.append(R1.Xin[i] + Ain * R1.Exin[i])
            ExInOutdata.append(R2.Xe[i])
            ExInOutdata.append(np.nan)

            EyInOutdata.append(Ain * R1.Eyin[i])
            EyInOutdata.append(2 * self.L + R2.Ezin[i])
            EyInOutdata.append(np.nan)

            EzInOutdata.append(R1.Zin[i] + Ain * R1.Ezin[i])
            EzInOutdata.append(R2.Ye[i])
            EzInOutdata.append(np.nan)

            PrayInDict = dict(
                go.Scatter3d(x=ExInOutdata,
                             y=EyInOutdata,
                             z=EzInOutdata,
                             mode='Lines',
                             name='PIn_Out' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                             line=dict(width=2, color='blue')
                             ))
        return PrayInDict

    def setRays4plot_R1_R2_Section_Lines(self, R1,  R3, iS, iF, color):

        xInOutdata = []
        yInOutdata = []
        zInOutdata = []

        Ain = 50
        for i in range(iS, iF):
            xInOutdata.append(R1.Xin[i])
            xInOutdata.append(R3.Xin[i])
            xInOutdata.append(np.nan)

            yInOutdata.append(0)
            yInOutdata.append(self.L*2)
            yInOutdata.append(np.nan)


            zInOutdata.append(R1.Zin[i])
            zInOutdata.append(R3.Yin[i])
            zInOutdata.append(np.nan)

        rayInOutDict = dict(
            go.Scatter3d(x=xInOutdata,
                         y=yInOutdata,
                         z=zInOutdata,
                         mode='Lines',
                         name='rayIn_Out' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=1, color=color)
                         ))
        return rayInOutDict

    #############        R 1 - R 3

    def setRays4plot_R1_R3_Section_markers(self, R1, R2, iS, iF, color):

        xIndata = []
        yIndata = []
        zIndata = []
        dataIn = []

        xOutdata = []
        yOutdata = []
        zOutdata = []
        dataOut = []

        Ain = 50
        for i in range(iS, iF):
            xIndata.append(R1.Xin[i])
            yIndata.append(0)
            zIndata.append(R1.Zin[i])

            xOutdata.append(R2.Xin[i])
            yOutdata.append(2*self.L)
            zOutdata.append(R2.Zin[i])

        dataIn.append(xIndata)
        dataIn.append(yIndata)
        dataIn.append(zIndata)

        dataOut.append(xOutdata)
        dataOut.append(yOutdata)
        dataOut.append(zOutdata)

        rayInDict = dict(
            go.Scatter3d(x=xIndata,
                         y=yIndata,
                         z=zIndata,
                         mode='markers',
                         name='rayIn_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))
        rayOutDict = dict(
            go.Scatter3d(x=xOutdata,
                         y=yOutdata,
                         z=zOutdata,
                         mode='markers',
                         name='Rout_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))
        return rayInDict, rayOutDict

    def setPolRays4Plot_R1_R3_Section_0_2(self, R1, R2, iS, iF):

        ExIndata = []
        EyIndata = []
        EzIndata = []

        ExOutdata = []
        EyOutdata = []
        EzOutdata = []

        Ain = 15
        for i in range(iS, iF):
            ##  Polarizaation IN

            ExIndata.append(R1.Xin[i])
            ExIndata.append(R1.Xin[i] + Ain*R1.Exin[i])
            ExIndata.append(np.nan)

            EyIndata.append(0)
            EyIndata.append(Ain * R1.Eyin[i])
            EyIndata.append(np.nan)

            EzIndata.append(R1.Zin[i])
            EzIndata.append(R1.Zin[i] + Ain * R1.Ezin[i])
            EzIndata.append(np.nan)

            ## Polarization OUT
            ExOutdata.append(R2.Xin[i])
            ExOutdata.append(R2.Xe[i])
            ExOutdata.append(np.nan)

            EyOutdata.append(2*self.L )
            EyOutdata.append(2*self.L + R2.Ye[i])
            EyOutdata.append(np.nan)

            EzOutdata.append(R2.Zin[i])
            EzOutdata.append(R2.Ze[i])
            EzOutdata.append(np.nan)

        PrayInDict = dict(
            go.Scatter3d(x=ExIndata,
                         y=EyIndata,
                         z=EzIndata,
                         mode='Lines',
                         name='PIn_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='red')
                         ))
        PrayOutDict = dict(
            go.Scatter3d(x=ExOutdata,
                         y=EyOutdata,
                         z=EzOutdata,
                         mode='Lines',
                         name='Pout_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='green')
                         ))
        return PrayInDict, PrayOutDict

    def setPolRays4Plot_R1_R3_Section_direction_0_2(self, R1, R2, iS, iF):

        ExInOutdata = []
        EyInOutdata = []
        EzInOutdata = []

        Ain = 15
        for i in range(iS, iF):
            ##  Polarizaation IN

            ExInOutdata.append(R1.Xin[i] + Ain * R1.Exin[i])
            ExInOutdata.append(R2.Xe[i])
            ExInOutdata.append(np.nan)

            EyInOutdata.append(Ain * R1.Eyin[i])
            EyInOutdata.append(2 * self.L + R2.Ye[i])
            EyInOutdata.append(np.nan)

            EzInOutdata.append(R1.Zin[i] + Ain * R1.Ezin[i])
            EzInOutdata.append(R2.Ze[i])
            EzInOutdata.append(np.nan)

        PrayInDict = dict(
            go.Scatter3d(x=ExInOutdata,
                         y=EyInOutdata,
                         z=EzInOutdata,
                         mode='Lines',
                         name='PIn_Out' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='blue')
                         ))
        return PrayInDict

    def setRays4plot_R1_R3_Section_Lines(self, R1,  R3, iS, iF, color):

        xInOutdata = []
        yInOutdata = []
        zInOutdata = []

        Ain = 50
        for i in range(iS, iF):
            xInOutdata.append(R1.Xin[i])
            xInOutdata.append(R3.Xin[i])
            xInOutdata.append(np.nan)

            yInOutdata.append(0)
            yInOutdata.append(self.L*2)
            yInOutdata.append(np.nan)


            zInOutdata.append(R1.Zin[i])
            zInOutdata.append(R3.Zin[i])
            zInOutdata.append(np.nan)

        rayInOutDict = dict(
            go.Scatter3d(x=xInOutdata,
                         y=yInOutdata,
                         z=zInOutdata,
                         mode='Lines',
                         name='rayIn_Out' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=1, color=color)
                         ))
        return rayInOutDict

    ###########         R 1 - R 2  -  R 3

    def setPolRays4Plot_R1_R2_R3_Section_0_3(self, R1, R2, R3, iS, iF):

        Ex0data = []
        Ey0data = []
        Ez0data = []

        Ex1data = []
        Ey1data = []
        Ez1data = []

        # Ex2data = []
        # Ey2data = []
        # Ez2data = []

        pRay3Data = []
        Ain = 15
        for i in range(iS, iF):
        # Polarizaation App
            Ex2data = []
            Ey2data = []
            Ez2data = []
            Ex0data.append(R1.Xin[i])
            Ex0data.append(R1.Xin[i] + Ain*R1.Exin[i])
            Ex0data.append(np.nan)

            Ey0data.append(0)
            Ey0data.append(Ain * R1.Eyin[i])
            Ey0data.append(np.nan)

            Ez0data.append(R1.Zin[i])
            Ez0data.append(R1.Zin[i] + Ain * R1.Ezin[i])
            Ez0data.append(np.nan)

        # Polarization after M1

            Ex1data.append(R2.Xin[i])
            Ex1data.append(R2.Xe[i])
            Ex1data.append(np.nan)

            Ey1data.append(self.L)
            Ey1data.append(self.L + R2.Ze[i])
            Ey1data.append(np.nan)

            Ez1data.append(R2.Yin[i])
            Ez1data.append(R2.Ye[i])
            Ez1data.append(np.nan)

        ## Polarization After M2

            Ex2data.append(R3.Xin[i])
            Ex2data.append(R3.Xe[i])
            Ex2data.append(np.nan)

            Ey2data.append(2*self.L )
            Ey2data.append(2*self.L + R3.Ye[i])
            Ey2data.append(np.nan)

            Ez2data.append(R3.Zin[i])
            Ez2data.append(R3.Ze[i])
            Ez2data.append(np.nan)

            Pray3 = dict(
                        go.Scatter3d(x=Ex2data,
                            y=Ey2data,
                            z=Ez2data,
                            mode='Lines',
                            name='each Ray_' + str(i),
                            line=dict(width=2, color='red')
                            ))

            pRay3Data.append(Pray3)


        Pray0Dict = dict(
            go.Scatter3d(x=Ex0data,
                         y=Ey0data,
                         z=Ez0data,
                         mode='Lines',
                         name='PIn_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='red')
                         ))

        Pray1Dict = dict(
            go.Scatter3d(x=Ex1data,
                         y=Ey1data,
                         z=Ez1data,
                         mode='Lines',
                         name='PIn_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='red')
                         ))

        Pray2Dict = dict(
            go.Scatter3d(x=Ex2data,
                         y=Ey2data,
                         z=Ez2data,
                         mode='Lines',
                         name='Pout_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='red')
                         ))

        return Pray0Dict, Pray1Dict, Pray2Dict, pRay3Data

    def setPolRays4Plot_R1_R2_R3_Section_direction_0_3(self, R1, R2, R3, iS, iF):

        ExInOutdata = []
        EyInOutdata = []
        EzInOutdata = []

        Ain = 15
        for i in range(iS, iF):
            ##  Polarizaation IN

            ExInOutdata.append(R1.Xin[i] + Ain * R1.Exin[i])
            ExInOutdata.append(R2.Xe[i])
            ExInOutdata.append(R3.Xe[i])
            ExInOutdata.append(np.nan)

            EyInOutdata.append(Ain * R1.Eyin[i])
            EyInOutdata.append(self.L + R2.Ze[i])
            EyInOutdata.append(2 * self.L + R3.Ye[i])
            EyInOutdata.append(np.nan)

            EzInOutdata.append(R1.Zin[i] + Ain * R1.Ezin[i])
            EzInOutdata.append(R2.Ye[i])
            EzInOutdata.append(R3.Ze[i])
            EzInOutdata.append(np.nan)

        PrayInDict = dict(
            go.Scatter3d(x=ExInOutdata,
                         y=EyInOutdata,
                         z=EzInOutdata,
                         mode='Lines',
                         name='PIn_Out' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color='blue')
                         ))
        return PrayInDict

    def setRays4plot_R1_R2_R3_Section_Lines(self, R1, R2, R3, iS, iF, color):

        xInOutdata = []
        yInOutdata = []
        zInOutdata = []

        for i in range(iS, iF):
            xInOutdata.append(R1.Xin[i])
            xInOutdata.append(R2.Xin[i])
            xInOutdata.append(R3.Xin[i])
            xInOutdata.append(np.nan)

            yInOutdata.append(0)
            yInOutdata.append(self.L)
            yInOutdata.append(self.L * 2)
            yInOutdata.append(np.nan)

            zInOutdata.append(R1.Zin[i])
            zInOutdata.append(R2.Yin[i])
            zInOutdata.append(R3.Zin[i])
            zInOutdata.append(np.nan)

        rayInOutDict = dict(
            go.Scatter3d(x=xInOutdata,
                         y=yInOutdata,
                         z=zInOutdata,
                         mode='Lines',
                         name='rayIn_Out' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=1, color=color)
                         ))
        return rayInOutDict

    def setRays4plot_R1_R2_R3_Section_markers(self, R1, R2, R3, iS, iF, color):

        #  Plot markers of rays in Ap, Screen1, Screen2

        x0data = []
        y0data = []
        z0data = []

        x1data = []
        y1data = []
        z1data = []

        x2data = []
        y2data = []
        z2data = []

        for i in range(iS, iF):
            x0data.append(R1.Xin[i])
            y0data.append(0)
            z0data.append(R1.Zin[i])

            x1data.append(R2.Xin[i])
            y1data.append(self.L)
            z1data.append(R2.Yin[i])

            x2data.append(R3.Xin[i])
            y2data.append(2 * self.L)
            z2data.append(R3.Zin[i])

        ray0Dict = dict(
            go.Scatter3d(x=x0data,
                         y=y0data,
                         z=z0data,
                         mode='markers',
                         name='R0_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))

        ray1Dict = dict(
            go.Scatter3d(x=x1data,
                         y=y1data,
                         z=z1data,
                         mode='markers',
                         name='R1_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))

        ray2Dict = dict(
            go.Scatter3d(x=x2data,
                         y=y2data,
                         z=z2data,
                         mode='markers',
                         name='R2_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))
        return ray0Dict, ray1Dict, ray2Dict

    def plotIs(self, data, layout, filename):
        #print('Data = ', data)
        fig = dict(data=data, layout=layout)
        py.offline.plot(fig, filename=filename)

    def setRays4plot_R1_R2_R3_R4_R5_Section_markers(self, R1, R2, R3, R4, R5, iS, iF, color):

        #  Plot markers of rays in Ap, Screen1, Screen2

        x0data = []
        y0data = []
        z0data = []

        x1data = []
        y1data = []
        z1data = []

        x2data = []
        y2data = []
        z2data = []

        x3data = []
        y3data = []
        z3data = []

        x4data = []
        y4data = []
        z4data = []

        for i in range(iS, iF):
            x0data.append(R1.Xin[i])
            y0data.append(0)
            z0data.append(R1.Zin[i])

            x1data.append(R2.Xin[i])
            y1data.append(self.L)
            z1data.append(R2.Yin[i])

            x2data.append(R3.Xin[i])
            y2data.append(2 * self.L)
            z2data.append(R3.Zin[i])

            x3data.append(R4.Yin[i])
            y3data.append(3 * self.L)
            z3data.append(R4.Zin[i])

            x4data.append(R5.Yin[i])
            y4data.append(4 * self.L)
            z4data.append(R5.Xin[i])

        ray0Dict = dict(
            go.Scatter3d(x=x0data,
                         y=y0data,
                         z=z0data,
                         mode='markers',
                         name='R0_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))

        ray1Dict = dict(
            go.Scatter3d(x=x1data,
                         y=y1data,
                         z=z1data,
                         mode='markers',
                         name='R1_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))

        ray2Dict = dict(
            go.Scatter3d(x=x2data,
                         y=y2data,
                         z=z2data,
                         mode='markers',
                         name='R2_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))
        ray3Dict = dict(
            go.Scatter3d(x=x3data,
                         y=y3data,
                         z=z3data,
                         mode='markers',
                         name='R3_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))
        ray4Dict = dict(
            go.Scatter3d(x=x4data,
                         y=y4data,
                         z=z4data,
                         mode='markers',
                         name='R4_' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=2, color=color)
                         ))
        return ray0Dict, ray1Dict, ray2Dict, ray3Dict, ray4Dict

    def setRays4plot_R1_R2_R3_R4_R5_Section_Lines(self, R1, R2, R3, R4, R5, iS, iF, color):

        xInOutdata = []
        yInOutdata = []
        zInOutdata = []

        for i in range(iS, iF):
            xInOutdata.append(R1.Xin[i])
            xInOutdata.append(R2.Xin[i])
            xInOutdata.append(R3.Xin[i])
            xInOutdata.append(R4.Yin[i])
            xInOutdata.append(R5.Yin[i])
            xInOutdata.append(np.nan)

            yInOutdata.append(0)
            yInOutdata.append(self.L)
            yInOutdata.append(self.L * 2)
            yInOutdata.append(self.L * 3)
            yInOutdata.append(self.L * 4)
            yInOutdata.append(np.nan)

            zInOutdata.append(R1.Zin[i])
            zInOutdata.append(R2.Yin[i])
            zInOutdata.append(R3.Zin[i])
            zInOutdata.append(R4.Zin[i])
            zInOutdata.append(R5.Xin[i])
            zInOutdata.append(np.nan)

        rayInOutDict = dict(
            go.Scatter3d(x=xInOutdata,
                         y=yInOutdata,
                         z=zInOutdata,
                         mode='Lines',
                         name='rayIn_Out' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                         line=dict(width=1, color=color)
                         ))
        return rayInOutDict


def setRays4plot_R1_R2_Section_Lines(self, R1, R2, iS, iF, color):
    xInOutdata = []
    yInOutdata = []
    zInOutdata = []


    for i in range(iS, iF):
        xInOutdata.append(R1.Xin[i])
        xInOutdata.append(R2.Xin[i])
        xInOutdata.append(np.nan)

        yInOutdata.append(0)
        yInOutdata.append(self.L)
        yInOutdata.append(np.nan)

        zInOutdata.append(R1.Zin[i])
        zInOutdata.append(R2.Yin[i])
        zInOutdata.append(np.nan)

    rayInOutDict = dict(
        go.Scatter3d(x=xInOutdata,
                     y=yInOutdata,
                     z=zInOutdata,
                     mode='Lines',
                     name='rayIn_Out' + str(self.mirrorIndex) + '_' + str(iS) + '_' + str(iF),
                     line=dict(width=1, color=color)
                     ))
    return rayInOutDict