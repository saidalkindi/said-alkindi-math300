# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:54:15 2022

@author: crazy
"""
import matplotlib.pyplot as plt

def midpoint(f, a = 0, b = 1, n = 100):
    h = (b - a)/n
    total = 0
    
    for i in range(n-1):
        total += f((a + h/2) + i * h)
    total *= h
    return total 
    plt.plot(x,total)
    
def function(x):
    return x*x

midpoint(function(5))

