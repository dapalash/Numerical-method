# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:33:30 2022

@author: D A Palash
"""

import math
import numpy as np


print("f(x)= e^x - x)")
xi = float(input("Enter the Guess:  "))

fxi = math.exp(-xi)-xi
fxib = -(math.exp(-xi))-1


err = float(input("enter the error value :"))
ite = int(input("enter the iteration :"))

x_a = np.zeros([ite])#making array 
x_c = np.zeros([ite])#making array 
f_a = np.zeros([ite])
f_c = np.zeros([ite])
real_err = np.zeros([ite])
itern = np.zeros([ite])

x_a[0]= xi

f_a[0]=fxi
 

for i in range(ite):
         itern[i]=i+1
       
         x_c[i]= xi[i]-((fxi[i])/(fxib[i]))
         fxib = -(math.exp(-xi))-1
         f_c[i] = math.exp(x_c[i])-x_c[i]
         
         if i>0:
             real_err[i]=((x_c[i]-x_c[i-1])/x_c[i])*100 # error estimation = ({xc[new]-xc(old)}/xc[new])x100
         
         if all ([i>0, abs(real_err[i])<err]):
             break 
         elif f_c[i]==0:
             break
    
         if i==ite-1:
             break
         
        ##something missing
         
          