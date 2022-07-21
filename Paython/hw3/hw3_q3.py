# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:04:14 2022

@author: crazy
"""
import matplotlib.pyplot as plt
import numpy as np 

def function(x = [1,2,3], N = 10):
    
    x_total = []
    for k in range(len(x)):
        total = 0
        for i in range(1, N + 1):
            total += (x[k]**i)/i
        x_total.append(total)
    plt.plot(x,x_total)

function(x=[1,2,3,4,5], N=5)
