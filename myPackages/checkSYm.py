import sympy as sp
from numpy import sin, cos, pi
from sympy import init_printing, pprint
import numpy as np
import pandas as pd
import scipy as sy


a1, a2, a3, a4, a5, a6, a7, a8, a9 = sp.symbols('a1 a2 a3 a4 a5 a6 a7 a8 a9')
M = sp.Matrix([[a1, a2, a3], [a4, a5, a6], [a7, a8, a9]])

MT = M.T
print('M = ')
print(M)
print('MT = ')
print(MT)