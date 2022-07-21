# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:35:07 2022

@author: crazy
"""
import matplotlib.pyplot as plt
import numpy as np 

def function(N = 100):
    total = 0
    n_total=[]
    for i in range(1,N + 1):
        total += ((-1)**(i+1)) * (1/i)
        n_total.append(total)
    plt.plot(range(1,N+1), n_total)
  
print(function())

