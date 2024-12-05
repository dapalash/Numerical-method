# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 14:43:55 2022

@author: D A Palash
"""
import numpy as np
import math

h = float(input("Enter the step size: "))
l = int(input("Enter the lower limit: "))
u = int(input("Enter the upper limit: "))

n = int((u-l)/h)
print(n)

def f(x):
    return (pow(x, 4))

# storing the value of x
x = np.zeros(n+1)
x[0] = l
value = 0
for i in range(0,n):
    value = value+h
    x[i+1] = value
print(x) 
    

# storing the value of y
y = np.zeros(n+1)

for i in range(0,n+1):
    a = x[i]
    y[i] = f(a)
print(y)


# forward differentiation
for i in range(0,n+1):
    if x[i] == 0.5:
        a = i
        break
print(a)

derivative = ((-f(x[a+2]))+(4*f(x[a+1]))-(3*f(x[a])))/(2*h)

print(derivative)

# center 
derivative = (-f(x[a+2])+8*f([a+1])-8*f([a-1])+f(x[a-2]))/(12*h)









