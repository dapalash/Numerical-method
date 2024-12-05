# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 15:33:54 2022

@author: D A Palash
"""

# Defining the function
def f(x):
    return ((400*x**5)-(900*x**4)+(675*x**3)-(200*x**2)+(25*x)+(0.2))

# Input section
x0= float(input("Enter lower limit of integration: ")) # a
xn= float(input("Enter upper limit of integration: ")) # b
n= int(input("Enter number of sub intervals: "))  # n

# calculating step size
h=((xn-x0)/n)
 
 # Finding sum 
integration = f(x0) + f(xn)
 
for i in range(1,n):
      xi = x0 + i*h # xi = a+i*h
     
      if i%2 == 0:
         integration = integration + 2 * f(xi)
      else:
          integration = integration + 4 * f(xi)
 
 # Finding final integration value
integration = integration * h/3

print("Integration result by Simpson's 1/3 method is: %0.6f" % (integration) )