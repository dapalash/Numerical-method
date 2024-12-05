# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:05:38 2022

@author: D A Palash
"""
import numpy as np

def givenFunction(x, y): 
    return (pow(x, 4) + pow(y, 5)) 

lx= 2.3 #float(input("Enter 1st Integrator's Lowest Limit:"))
ux= 2.5 #float(input("Enter 1st Integrator's Highest Limit:"))
ly= 3.7 #float(input("Enter 2nd Integrator's Lowest Limit:"))
uy= 4.3 #float(input("Enter 2nd Integrator's Highest Limit:"))
N1= 2 #int(input("enter 1st Integrator's  interval:"))
N2=4 #int(input("enter 2nd Integrator's  interval:"))
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
            if (i==nx-1 and j==ny-1):
                answer += z[i][j]
            elif(i==0 and j==0):
                answer += z[i][j]
            elif (i==0 and j==ny-1):
                answer += z[i][j]
            elif (i==nx-1 and j==0):
                answer += z[i][j]
                
                
            elif (i==0 and j%2==0):
                answer +=2 * z[i][j]
            elif (i==nx-1 and j%2==0):
                answer +=2 * z[i][j]
            elif (j==0 and i%2==0):
                answer +=2 * z[i][j]
            elif (j==ny-1 and i%2==0):
                answer +=2 * z[i][j]
                
              
            elif (i==0 and j%2!=0):
                answer +=4 * z[i][j]
            elif (i==nx-1 and j%2!=0):
                answer +=4 * z[i][j]
            elif (j==0 and i%2!=0):
                answer +=4 * z[i][j]
            elif (j==ny-1 and i%2!=0):
                answer +=4 * z[i][j]
            
                
            
            elif (i%2==0 and j%2==0):
                answer +=4 * z[i][j]
            elif (i%2==0 and j%2!=0):
                answer +=8 * z[i][j]
                
                
                
            elif (i%2!=0 and j%2==0):
                answer +=8 * z[i][j]
            else :
                answer +=16 * z[i][j]
  
    answer *= (h*k)/9
    
print(answer) 
