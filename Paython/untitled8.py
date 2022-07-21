# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
import circle1 
        
circle = circle1.circle(cx = random.randint(1,25), cy = random.randint(1,25), r = random.randint(1,10))

circle_plot = plt.Circle((circle.cx, circle.cy), circle.r, fill = False)

fig, ax = plt.subplots()
ax.axis([-50,50,-50,50])

ax.add_artist(circle_plot)
plt.show()                          
        
