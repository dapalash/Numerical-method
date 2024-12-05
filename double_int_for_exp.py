# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:06:48 2022

@author: D A Palash
"""

import numpy as np
import math

def givenFunction(x, y): 
    return (math.exp(x)*math.exp(y))

lx= 0 #float(input("Enter 1st Integrator's Lowest Limit:"))
ux= 1 #float(input("Enter 1st Integrator's Highest Limit:"))
ly= 0 #float(input("Enter 2nd Integrator's Lowest Limit:"))
uy= 1#float(input("Enter 2nd Integrator's Highest Limit:"))
N1= 4 #int(input("Enter 1st Integrator's  interval:"))
N2= 4 #int(input("Enter 2nd Integrator's  interval:"))
h=float((ux-lx)/N1) #1st Integrator
k=float((uy-ly)/N2) #2nd Integrator


# Creating the table with zeros
nx = round((ux - lx) / h + 1) 
ny = round((uy - ly) / k + 1)
z= np.zeros((nx,ny))  


# Calculating the values of the table 
for i in range(0, nx): 
    for j in range(0, ny): 
        z[i][j] = givenFunction(lx + i * h, ly + j * k) 
              
        
    answer = 0
    for i in range(0, nx): 
        for j in range(0, ny): 
            if (i==nx-1 and j==ny-1): # last corner
                answer += z[i][j]
            elif(i==0 and j==0): # 1st corner
                answer += z[i][j]
            elif (i==0 and j==ny-1): # 1st row, last col
                answer += z[i][j]
            elif (i==nx-1 and j==0): # last row, 1st col
                answer += z[i][j]
                
                
            elif (i==0 and j%2==0): # odd position on boundary
                answer +=2 * z[i][j]
            elif (i==nx-1 and j%2==0):
                answer +=2 * z[i][j]
            elif (j==0 and i%2==0):
                answer +=2 * z[i][j]
            elif (j==ny-1 and i%2==0):
                answer +=2 * z[i][j]
                
              
            elif (i==0 and j%2!=0):  # even position on boundary
                answer +=4 * z[i][j]
            elif (i==nx-1 and j%2!=0):
                answer +=4 * z[i][j]
            elif (j==0 and i%2!=0):
                answer +=4 * z[i][j]
            elif (j==ny-1 and i%2!=0):
                answer +=4 * z[i][j]
            
                
            
            elif (i%2==0 and j%2==0): # 𝒐𝒅𝒅 𝒑𝒐𝒔𝒊𝒕𝒊𝒐𝒏 on odd row 𝒆𝒙𝒄𝒆𝒑𝒕 𝒃𝒐𝒖𝒏𝒅𝒂𝒓𝒚
                answer +=4 * z[i][j]
            elif (i%2==0 and j%2!=0): # 𝒆𝒗𝒆𝒏 𝒑𝒐𝒔𝒊𝒕𝒊𝒐𝒏 on odd row 𝒆𝒙𝒄𝒆𝒑𝒕 𝒃𝒐𝒖𝒏𝒅𝒂𝒓𝒚
                answer +=8 * z[i][j]
                
                
                
            elif (i%2!=0 and j%2==0): # 𝒐𝒅𝒅 𝒑𝒐𝒔𝒊𝒕𝒊𝒐𝒏 on even row except boundary
                answer +=8 * z[i][j]
            else :
                answer +=16 * z[i][j] # 𝒆𝒗𝒆𝒏 𝒑𝒐𝒔𝒊𝒕𝒊𝒐𝒏 𝒐𝒏 𝒆𝒗𝒆𝒏 𝒓𝒐𝒘 𝒆𝒙𝒄𝒆𝒑t 𝒃𝒐𝒖𝒏𝒅𝒂𝒓𝒚
  
    answer *= (h*k)/9
    
print(answer) 