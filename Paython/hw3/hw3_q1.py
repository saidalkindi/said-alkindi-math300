# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:11:05 2022

@author: crazy
"""

import numpy as np
from scipy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [8]])

display('matrix A:', A)
display('matrix b:', b)

x = np.linalg.solve(A, b)
display('matrix x:', x)