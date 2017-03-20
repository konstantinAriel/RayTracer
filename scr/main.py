import  numpy as np
from myPackages.readExelfile.ReadXls import ReadXls


path = "/home/kosta/RayTracer/RayTracer/files/settingsfiles/testSheets4py.xls"

xlsFile = ReadXls(path)
#print(xlsFile.path)

paramFile = xlsFile.readXlsFile(path)
lineParam = xlsFile.getLineParam(paramFile)
sysParam = xlsFile.getSysPAram(paramFile)
#print((sysParam.Rin))
raysIn = xlsFile.getSysPAram(paramFile)


def getMirrorList():
    count = 0
    mirrorDict = {}
    print(mirrorDict)
    for i in sysParam.Rin:
            if np.isnan(i):
              break
            else:
                mirrorList = []
                position = 0
                for j in range(int(sysParam.Rin[count]), int(sysParam.Rout[count]) + 1):
                    mirrorList.insert(position, 'mirror' + str(j))
                    position = position + 1
                mirrorDict['mirrorDict'+str(count+1)] = mirrorList
                count = count + 1
    return mirrorDict

mD = getMirrorList()
print('mdict = ', mD)

