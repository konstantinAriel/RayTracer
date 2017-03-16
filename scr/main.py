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

count = 0
mirrorList = []
print(mirrorList)
for i in sysParam.Rin:
    print('count = ', count)
    print('i = ', i)
    if  np.isnan(i):
        break
    else:
        for j in range(int(sysParam.Rin[count]), int(sysParam.Rout[count])+1):
            print('j= ', j)
        mirrorList.insert(j, )
        count = count+1
