# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 23:22:31 2022

@author: crazy
"""

import sympy as sp  
sp.init_printing()

x = sp.symbols('x')
f = x**3 - ((sp.cos(sp.pi*x)**2)/(2*x**2 + 1)) + (11/3) * x**2 - 1
derivative_f = sp.diff(f, x)
display(derivative_f) 