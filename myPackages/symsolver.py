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
xDegree = 90
yDegree = 0
zDegree = 0

a11 = 1/800
a22 = 1/800
a3 =1
dx1 = 0
dx2 = 200
dx3 = 400
x01Ray = 0
x02Ray = -400
x03Ray = 0
k1 = 0
k2 = 1
k3 = 0

def degree2Rarian(alphaDegree):
    return (alphaDegree*pi)/180

def cs(alphaDegree):
    alphaRadian = degree2Rarian(alphaDegree)
    if np.abs(cos(alphaRadian)) < 1e-4:
        csAlpha = 0
    else:
        csAlpha =  cos(alphaRadian)
    return csAlpha


def sn(alphaDegree):
    alphaRadian = degree2Rarian(alphaDegree)
    if np.abs(sin(alphaRadian)) < 1e-4:
            snAlpha = 0
    else:
            snAlpha = sin(alphaRadian)
    return snAlpha


def getRotateMatrix(xDegree,yDegree, zDegree):
    csX = cs(xDegree)
    snX = sn(xDegree)
    csY = cs(yDegree)
    print(csY)
    snY = sn(yDegree)
    print(snY)
    csZ = cs(zDegree)
    snZ = sn(zDegree)
    Rx = np.array([
        [1, 0, 0],
        [0, csX, -snX],
        [0, snX, csX]
    ])
    Ry = np.array([
        [csY, 0, snY],
        [0, 1, 0],
        [-snY, 0, csY]
    ])
    Rz = np.array([
        [csZ, -snZ, 0],
        [snZ, csZ, 0],
        [0, 0, 1]
    ])
    print('******************************')
    Mr = (Rx.dot(Ry)).dot(Rz)
    print(Rx)
    print(Ry)
    print(Rz)
    print('===================')
    print('Mr = ')
    print(Mr)
    print('=======================')
    return  Mr

Mr = getRotateMatrix(xDegree, yDegree, zDegree)
x1Ray = x01Ray + k1*t
x2Ray = x02Ray + k2*t
x3Ray = x03Ray + k3*t

# x1 = x1Ray
# x2 = x2Ray
# x3 = x3Ray

x1R = (x1-dx1)*Mr[0,0] + (x2-dx2)*Mr[0,1] + (x3-dx3)*Mr[0,2]
x2R = (x1-dx1)*Mr[1,0] + (x2-dx2)*Mr[1,1] + (x3-dx3)*Mr[1,2]
x3R = (x1-dx1)*Mr[2,0] + (x2-dx2)*Mr[2,1] + (x3-dx3)*Mr[2,2]


print(x1R)
print(x2R)
print(x3R)

Expr_A11 = x1R**2
Expr_A22 = x2R**2
Expr_A3 = x3R

mainExpr = a11*Expr_A11 + a22*Expr_A22 - a3*Expr_A3
print('mainExpr = ')
pprint(mainExpr)
# mainExpr = mainExpr.subs(x1, x1Ray)
# mainExpr = mainExpr.subs(x2, x2Ray)
# mainExpr = mainExpr.subs(x3, x3Ray)
# pprint(mainExpr)
mainExprExpanded = sp.expand(mainExpr)
#pprint(mainExprExpanded)
mainExprCollcted = sp.collect(mainExprExpanded, t)
print('Expr Collected = ')
pprint(mainExprCollcted)
tSolver = sp.solveset(mainExprCollcted, t)

pprint(tSolver)
