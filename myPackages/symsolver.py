import sympy as sp
from numpy import sin, cos,pi
from sympy import init_printing, pprint
import numpy as np
x1, x2, x3, dx1, dx2, dx3, a11, a22, a3, x01Ray, x02Ray, x03Ray, k1,k2,k3, t = sp.symbols('x1 x2 x3 '
                                                                                          'dx1 dx2 dx3 '
                                                                                          'a11 a22 a3 '
                                                                                          'x01Ray x02Ray x03Ray '
                                                                                          'k1 k2 k3'
                                                                                          ' t')
x1R, x2R, x3R, dx1R, dx2R, dx3R = sp.symbols('x1R x2R x3R dx1R dx2R dx3R')
xRad = pi/2
yRad = 0
zRad = 0
Rx = np.array([
              [1, 0, 0],
              [0, cos(xRad), sin(xRad)],
              [0, -sin(xRad), cos(xRad)]
            ])
Ry = np.array([
               [cos(yRad), 0, -sin(yRad)],
               [0, 1, 0],
               [sin(yRad), 0, cos(yRad)]
            ])
Rz = np.array([
               [cos(zRad), -sin(zRad), 0],
               [sin(zRad), cos(zRad), 0],
               [0, 0, 1]
            ])
print('******************************')
Mr = (Rx.dot(Ry)).dot(Rz)
print(Ry)
print(Rx)
print(Rz)
print('===================')
print('Mr = ')
print(Mr)
print('=======================')
Mc = sp.Matrix([[x1],
                [x2],
                [x3]])

x1R = x1*Mr[0,0] + x2*Mr[0,1] + x3*Mr[0,2]
x2R = x1*Mr[1,0] + x2*Mr[1,1] + x3*Mr[1,2]
x3R = x1*Mr[2,0] + x2*Mr[2,1] + x3*Mr[2,2]

print(x1R)
print(x2R)
print(x3R)

x1Ray = x01Ray + k1*t
x2Ray = x02Ray + k2*t
x3Ray = x03Ray + k3*t

mainExpr = a11*((x1R - dx1R)**2) +a22*((x2R-dx2R)**2) -a3*(x3R-dx3R)
pprint(mainExpr)
mainExpr = mainExpr.subs(x1, x1Ray)
mainExpr = mainExpr.subs(x2, x2Ray)
mainExpr = mainExpr.subs(x3, x3Ray)
# pprint(mainExpr)
mainExprExpanded = sp.expand(mainExpr)
#pprint(mainExprExpanded)
mainExprCollcted = sp.collect(mainExprExpanded, t)
pprint(mainExprCollcted)
