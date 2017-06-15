
import numpy as np
import scipy.linalg as sl

from scr.MainParam import Parametrs

# a = np.array([[-1, 2, 3], [2,3,4], [4,5,6]])
# b = np.array([[1], [2], [3]])
# c = sl.solve(a, b)
# print('c = ')
# print(c)

pathIn = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/Ray_0_1.xls'
pathOut = '/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/Ray_1_2.xls'
rInObject = Parametrs(pathIn, 'Sheet1')
rOutObject = Parametrs(pathOut, 'Sheet1')
rInDF = rInObject.dataSheet
rOutDF = rOutObject.dataSheet
# print('rInDF')
# print(rInDF)

xIn = 5
Kxin = 0.02

r11 = rInDF.Xin[0]
r12 = (r11**2)
r13 = r11**3
r14 = rInDF.Kxin[0]
r15 = r13**2
r16 = r13**3
r17 = r11*r14
r18 = r12*r14
r19 = r11*r15

r21 = rInDF.Xin[1]
r22 = (r11**2)
r23 = r11**3
r24 = rInDF.Kxin[1]
r25 = r13**2
r26 = r13**3
r27 = r11*r14
r28 = r12*r14
r29 = r11*r15

r31 = rInDF.Xin[1]
r32 = (r11**2)
r33 = r11**3
r34 = rInDF.Kxin[1]
r35 = r13**2
r36 = r13**3
r37 = r11*r14
r38 = r12*r14
r39 = r11*r15

r41 = rInDF.Xin[1]
r42 = (r11**2)
r43 = r11**3
r44 = rInDF.Kxin[1]
r45 = r13**2
r46 = r13**3
r47 = r11*r14
r48 = r12*r14
r49 = r11*r15

r51 = rInDF.Xin[1]
r52 = (r11**2)
r53 = r11**3
r54 = rInDF.Kxin[1]
r55 = r13**2
r56 = r13**3
r57 = r11*r14
r58 = r12*r14
r59 = r11*r15

r61 = rInDF.Xin[1]
r62 = (r11**2)
r63 = r11**3
r64 = rInDF.Kxin[1]
r65 = r13**2
r66 = r13**3
r67 = r11*r14
r68 = r12*r14
r69 = r11*r15

r71 = rInDF.Xin[1]
r72 = (r11**2)
r73 = r11**3
r74 = rInDF.Kxin[1]
r75 = r13**2
r76 = r13**3
r77 = r11*r14
r78 = r12*r14
r79 = r11*r15

r81 = rInDF.Xin[1]
r82 = (r11**2)
r83 = r11**3
r84 = rInDF.Kxin[1]
r85 = r13**2
r86 = r13**3
r87 = r11*r14
r88 = r12*r14
r89 = r11*r15

r91 = rInDF.Xin[1]
r92 = (r11**2)
r93 = r11**3
r94 = rInDF.Kxin[1]
r95 = r13**2
r96 = r13**3
r97 = r11*r14
r98 = r12*r14
r99 = r11*r15

RinMatrix = np.array([[r11, r12, r13, r14, r15, r16, r17, r18, r19],
                      [r21, r22, r23, r24, r25, r26, r27, r28, r29],
                      [r31, r32, r33, r34, r35, r36, r37, r38, r39],
                      [r41, r42, r43, r44, r45, r46, r47, r48, r49],
                      [r51, r52, r53, r54, r55, r56, r57, r58, r59],
                      [r61, r62, r63, r64, r65, r66, r67, r68, r69],
                      [r71, r72, r73, r74, r75, r76, r77, r78, r79],
                      [r81, r82, r83, r84, r85, r86, r87, r88, r89],
                      [r91, r92, r93, r94, r95, r96, r97, r98, r99]])
print('RinMatrix = ')
print(RinMatrix)

boolValue = RinMatrix.shape[0] == RinMatrix.shape[1] and np.linalg.matrix_rank(RinMatrix) == RinMatrix.shape[0]

print('boolValue = ')
print(boolValue)

RoutVector = np.array([[rOutDF.Xin[0]],
                       [rOutDF.Xin[0]],
                       [rOutDF.Xin[0]],
                       [rOutDF.Xin[0]],
                       [rOutDF.Xin[0]],
                       [rOutDF.Xin[0]],
                       [rOutDF.Xin[0]],
                       [rOutDF.Xin[0]],
                       [rOutDF.Xin[0]]
                        ])

A = sl.solve(RinMatrix, RoutVector)