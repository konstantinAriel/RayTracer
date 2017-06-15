import numpy as np

c = np.array([[1,1,0], [0, 1, 0], [0, 0, 1]])
c11 = c[0, 0]
c12 = c[0, 1]
c13 = c[0, 2]
c21 = c[1, 0]
c22 = c[1, 1]
c23 = c[1, 2]
c31 = c[2, 0]
c32 = c[2, 1]
c33 = c[2, 2]
rout = np.array([[1], [2], [3]])
aTemp1 = c11 * rout[0] + c12 * rout[1] + c13 * rout[2]
aTemp2 = c21 * rout[0] + c22 * rout[1] + c23 * rout[2]
aTemp3 = c31 * rout[0] + c32 * rout[1] + c33 * rout[2]
print(aTemp1)
print(aTemp2)
print(aTemp3)