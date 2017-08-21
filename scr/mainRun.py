import scr.mainParamPakage as mp
import scr.RayTracing.Rays as rmain

# import numpy as np

tLine = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, "LineParam")
sysParam = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, "SysParam")
Rin = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.rInDir +  mp.raysInFname + mp.fExtend, 'KonusFrom1Point')

mirrorSheetName = 'Mirror' + str(int(sysParam.DataSheet.Rin[0]))
raysSheetName = 'Ray_' + str(int(sysParam.DataSheet.Rin[0] - 1)) + '_' + str(int(sysParam.DataSheet.Rin[0]))


mirrorObj = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, 'Mirror1')
rInObj = rmain.Rays(mirrorObj.DataSheet, Rin.DataSheet)  # Create object of Rays

raysInDFn = rInObj.RaysDFnormal
# save to Excel
rOutFname = 'Ray'+'_' + \
           str(int(sysParam.DataSheet.Rin[0]-1)) + '_' + \
           str(int(sysParam.DataSheet.Rin[0]))


mirrorList = sysParam.getMirrorList(sysParam.DataSheet)
raysInDFn.to_excel(mp.mainPath + mp.xlsDir + mp.rOutDir  + mp.rReflectedDir + rOutFname + mp.fExtend)

#==============  Get List of Section for calculation ========================#

for mIndex in mirrorList:
    print(mIndex)

def mirrorLoop(mirrorList):
        countMirror = int(sysParam.DataSheet.Rin[0])
        for mirrorIndex in mirrorList:
            print('====================================================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++        Mirror Loop         ',  mirrorIndex)
            Mirror = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.systemSettingsDir + mp.sysParamFilename + mp.fExtend, mirrorIndex)  ## mirror List - The name of Sheets in Exel file
            raysFName = ['Ray_' + (str(countMirror - 1)) + '_' + str(countMirror),
                         'Ray_' + str(countMirror) + '_' + str(countMirror + 1),
                         'normalRay_' + str(countMirror) + '_' + str(countMirror)]
            RaysObject = mp.Parametrs(mp.mainPath + mp.xlsDir + mp.rOutDir +  raysFName[0] + mp.fExtend, 'Sheet1' )
            print(RaysObject.DataSheet)
            pathList = [mp.mainPath + mp.xlsDir + mp.rOutDir, raysFName, mp.fExtend]
            rmain.Rays.getReflectedRays()
            countMirror += 1
        print('============== ++++++++++++++++++++++++++++++++++++++++++++++++++++++   END   Mirror Loop         ',  mirrorIndex)