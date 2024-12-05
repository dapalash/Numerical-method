# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 15:56:46 2022

@author: WIN
"""
import numpy as np
import math


l = float(input("Enter the lower range of x: " ))
u = float(input("Enter the higher range of x: " ))
h = float(input("Enter the step size: "))

def f(x,y):
    return x+y

n = int(((u-l)/h)+1)
x = np.zeros(n)
y = np.zeros(n)
print(x)
print(y)

print("enter the intial condition:\n")
x[0] = input("x[0]: ")
y[0] = input("y[0]: ")

def heuns(h):
    for i in range(1,n):
        k1 = h*f(x[i-1],y[i-1])
        k2 = h*f(x[i-1]+h,y[i-1]+k1)
        k = .5*(k1+k2)
        y[i] = y[i-1]+k
        x[i] = x[i-1]+h
    print(x)
    print(y)
print(heuns(h))

def midpoint(h):
    for i in range(1,n):
        k1 = h*f(x[i-1],y[i-1])
        k2 = h*f(x[i-1]+h,y[i-1]+k1)
        
        y[i] = y[i-1]+k2[i]*h
        x[i] = x[i-1]+h
        print(x)
        print(y)
print(midpoint(h))

