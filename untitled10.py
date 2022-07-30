#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 
import Animals


def animate(frame_number):
    
    for an in pop:
        an.move(x_min,x_max,y_min,y_max)
    
    for an_prey in pop:
        for an_pred in pop:
            if an_pred.__class__ is Animals.predator and an_prey.__class__ is Animals.prey:
                an.attack(an_prey)
    
    for an in pop:
        if an.hitpoints <= 0:
            pop_dead.append(an)
            pop.remove(an)
            
            
    d.set_data([animal.x for animal in pop if animal.__class__ is Animals.prey],[animal.y for animal in pop if animal.__class__ is Animals.prey]) 
    c.set_data([animal.x for animal in pop if animal.__class__ is Animals.predator],[animal.y for animal in pop if      animal.__class__ is Animals.predator])
    e.set_data([animal.x for animal in pop_dead],[animal.y for animal in pop_dead])



## Set Space limits
x_max = 25
x_min = 0
y_max = 25
y_min = 0

## Number of frames to simulate
frames = 1000

## Population of our model
num_prey = 25
num_predator = 5
pop = [Animals.prey(x_max*np.random.uniform(0,1), y_max*np.random.uniform(0,1)) for i in range(num_prey)] \
       + [Animals.predator(x_max*np.random.uniform(0,1), y_max*np.random.uniform(0,1)) for i in range(num_predator)]

pop_dead = []
# Set Ax length and get current figure

ax  = plt.axes(xlim=(x_min,x_max), ylim=(y_min, y_max))
fig = plt.gcf()

## Plot first instance
d, = plt.plot([animal.x for animal in pop if animal.__class__ is Animals.prey],[animal.y for animal in pop if animal.__class__ is Animals.prey], 'bo', markersize = 5) 
c, = plt.plot([animal.x for animal in pop if animal.__class__ is Animals.predator],[animal.y for animal in pop if animal.__class__ is Animals.predator], 'ro', markersize = 5)
e, = plt.plot([animal.x for animal in pop_dead],[animal.y for animal in pop_dead], 'o', color = 'black', markersize = 5)


anim = animation.FuncAnimation(fig, animate, frames, interval=1, repeat=False)#, blit=True)