# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:42:17 2022

@author: D A Palash
Ordinary Differential Equation
"""

import numpy as np
import math

l = float(input("Enter th5e lower range of x: " ))
u = float(input("Enter the higher range of x: " ))
h = float(input("Enter the step size: "))

def f(x,y):
    return x+y
n = int((u-l)/h)
x = np.zeros(n)
y = np.zeros(n)
print(x)
print(y)

print("enter the intial condition:\n")
x[0] = input("x[0]: ")
y[0] = input("y[0]: ")

k1 = h*f(x[0],y[0])
k2 = h*f(x[0]+h,y[0]+k1)
k = .5*(k1+k2)

for i in range(1,n):
    y[i] = y[i-1]+k[i]
    x[i] = x[i-1]+h
print(x)
print(y)