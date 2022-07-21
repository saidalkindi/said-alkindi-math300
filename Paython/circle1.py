# -*- coding: utf-8 -*-

import math

class circle():
    def __init__(self, cx = 0, cy = 0, r = 1):
        self.cx = cx
        self.cy = cy
        self.r = r

    def area(self):
        return math.pi*(self.r**2)
        
    def circumference(self):
        return 2*math.pi*self.r
    
    def inside(self, x, y):
        if (x - self.cx)**2 * (y - self.cy)**2 <= self.r**2:
            print('point is in circle') 
        else:
            print('point is not circle')

a = circle()
print(a.area())
print(a.circumference())
print(a.inside(1, 1))
        
