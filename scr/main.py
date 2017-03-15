
from myPackages.readExelfile.ReadXls import ReadXls


path = "/home/kosta/RayTracer/files/settingsfiles/testSheets4py.xls"

xlsFile = ReadXls(path)
#print(xlsFile.path)

paramFile = xlsFile.readXlsFile(path)
lineParam = xlsFile.getLineParam(paramFile)
sysParam = xlsFile.getSysPAram(paramFile)
#print((sysParam.Rin))
raysIn = xlsFile.getSysPAram(paramFile)

count = 0

for i in sysParam.Rin:
    if i>=0:
        print("i = ", i)
        print("sysParam  = ", sysParam.Rout[count])

        for j in range (i,sysParam.Rout[count]):
            mirror = xlsFile.getMirrorParam(paramFile, j+3)
            print("j = ", j)
            print("mirror = ", mirror)
        count = count+1
vbnvncnbcvnb