import numpy as np
import pandas as pd
import xarray as xr
import plotly.graph_objs  as go

import plotly as py

from numpy import nan
from scr.MainParam import Parametrs
from scr.Ploting import Ploting
from scr.Rays import Rays
from scr.MainParam import Parametrs
from scr.TestMatrix import TestMatrix  as tm, TestMatrix
from scr.getRaysFromMatrix import RaysFromMatrix

global mainPath, fExtend, sysParamFname, raysInFname, ray4test3pointFname, mainPathForMatrix

def pathName():
    global mainPath, fExtend, sysParamFname, raysInFname, ray4test3pointFname, mainPathForMatrix
    mainPath = "/home/konstantin/PycharmProjects/RayTracer/files/settingsfiles/"
    fExtend = '.xls'
    sysParamFname = 'sysParam_1'
    raysInFname = 'RaysIn'
    raysNormalisedFname = mainPath + 'raysNormalised_' + raysInFname + '_' + sysParamFname
    ray4test3pointFname = mainPath + 'ray4test3Point_'  + sysParamFname + fExtend
    mainPathForMatrix = '/home/konstantin/PycharmProjects/RayTracer/result/raysForMatrix/'