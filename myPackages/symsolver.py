import sympy as sp
from numpy import sin, cos,pi
from sympy import init_printing, pprint
import numpy as np





xDegree = -90
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
    # pprint(mainExpr)
    mainExpr = mainExpr.subs(x1, x1Ray)
    mainExpr = mainExpr.subs(x2, x2Ray)
    mainExpr = mainExpr.subs(x3, x3Ray)
    pprint(mainExpr)
    mainExprExpanded = sp.expand(mainExpr)
    #pprint(mainExprExpanded)
    mainExprCollcted = sp.collect(mainExprExpanded, t)
    print('Expr Collected = ')
    pprint(mainExprCollcted)
    tSolver = sp.solveset(mainExprCollcted, t)
    print('t = ')
    pprint(tSolver)
