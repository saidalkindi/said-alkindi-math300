#!/usr/bin/env python3

## Write a program for predator prey interactions in a small space 

import random

class animal():
    def __init__(self,x=0,y=9):
        
        self.x = x
        self.y = y
        self.hitpoints = 100

    
    def move(self,x_min,x_max,y_min,y_max):
        a = random.randint(1,4)
        
        if a == 1:
            self.y += 1
        elif a == 2:
            self.x += 1
        elif a == 3:
            self.y -= 1
        elif a == 4:
            self.x -= 1
    
        if self.x <= x_min:
            self.x = x_min
        if self.x >= x_max:
            self.x = x_max
        if self.y <= y_min:
            self.y = y_min
        if self.y >= y_max:
            self.y = y_max

class predator(animal):
    pass

    
    def attack(self,person):
        
        distance = (self.x - person.x)**2 + (self.y - person.y)**2
        
        if distance < 1:
            damage_roll = random.randint(1,20)
            person.check_damage(damage_roll)
        

class prey(animal):
    pass

    def check_damage(self,b):
        
        if b == 20:
            self.hitpoints -= 100
        elif b > 15:
            self.hitpoints -= b*3
        elif b < 15:
            self.hitpoints += 0
            
