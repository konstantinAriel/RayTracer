import pandas as pd
import numpy as np

class Mirror:
    def __init__(self, columns):
        self.vertex = columns.Vertex
        self.focus = columns.Focus
        self.deltaF = columns.deltaF
        self.direction = columns.direction
