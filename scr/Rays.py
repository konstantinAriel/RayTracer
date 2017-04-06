

import numpy as np
import pandas as pd
import scipy as sy

class Rays:
    def __init__(self):
       pass

    def calcRInNormal(self,kInArray):
        return (kInArray/(np.sqrt(np.dot(kInArray, kInArray.T))))

    #def findCrossPoint(self, Rin):


    def saveExecelRin(self, RinParamTable, FileName):
        RaysHeads = RinParamTable.columns
        RayCount = 0
        numberOfRays = len(RinParamTable.KxIn)
        KinNormalArray = np.zeros((numberOfRays, 3))
        XinArray = np.zeros((numberOfRays, 3))
        EinArray = np.zeros((numberOfRays, 4))
        for RinIndex in RinParamTable.index:
            #print(RinIndex)
            KinArray = np.array([RinParamTable.KxIn[RinIndex],
                                 RinParamTable.KyIn[RinIndex],
                                 RinParamTable.KzIn[RinIndex]
                                 ])

            XinArray[RinIndex, :] = np.array([RinParamTable.Xin[RinIndex],
                                              RinParamTable.Yin[RinIndex],
                                              RinParamTable.Zin[RinIndex]
                                              ])
            EinArray[RinIndex, :] = np.array([RinParamTable.ExIn[RinIndex],
                                              RinParamTable.EyIn[RinIndex],
                                              RinParamTable.EzIn[RinIndex],
                                              RinParamTable.Ain[RinIndex]
                                              ])
            #Kin = Rays(KinArray)
            KinNormal = self.calcRInNormal(KinArray)
            KinNormalArray[RinIndex, :] = KinNormal
            # print(KinNormalArray)
            # print(KinArray)
            # print(KinNormal)
            RayCount += 1
            # print('=========================')
        # print('XinArray=', XinArray)
        # print('*************')
        RaysInDF = pd.DataFrame({'Xin': XinArray[:, 0],
                              'Kxin': KinNormalArray[:, 0],
                              'Yin': XinArray[:, 1],
                              'Kyin': KinNormalArray[:, 1],
                              'Zin': XinArray[:, 2],
                              'Kzin': KinNormalArray[:, 2],
                              'Exin': EinArray[:, 0],
                              'Eyin': EinArray[:, 1],
                              'Ezin': EinArray[:, 2],
                              'Ain': EinArray[:, 3]
                              })
        RaysInDF.to_excel(FileName, sheet_name='Sheet2')
        # print('KinDF = ')
        # print(RaysInDF)
        return  RaysInDF

