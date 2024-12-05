# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:25:56 2022

@author: Palash
"""

##Import libraries as necessary
import numpy as np
import xlrd

n=int(input ('Enter number of unknown variables: '))   #number of unknown variables
#print(n) 

#Initialize variables
a=np.zeros([n,n+1])
b=np.zeros([n,n+1])
B=np.zeros([n,n+1])
C=np.zeros([n,n+1])
X=np.zeros([n])
p=np.zeros([n])

#Reading data from excel file
loc = (r'H:\Education\3-1 3rd Year Odd Semester - ETE 18\Numerical Method\Lab\Lab 4\data.xlsx')


wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(4)

#creating matrix from the data 
for i in range(sheet.ncols):
    for j in range(sheet.nrows):
        #print(sheet.cell_value(1, i))
        a[j,i]=sheet.cell_value(j, i)
        
#a=np.array([[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]])       
#n=sheet.ncols-1   #number of unknown variables

#Forward Elimination
for i in range(n):
    for j in range(n+1):
        if i==0:
            b[i,j]=a[i,j]
        if i>0:
            b[i,j]=a[i,j]-(a[0,j]*(a[i,0]/a[0,0]))
            
if n<3:
    C=b

if n>2:
    B=b 
        
    for k in range(n-1):
        for i in range(n):
            for j in range(n+1):
                
                if all ([i>k+1, j<k+1]):
                    C[i,j]=B[i,j]-(B[k,j]*(B[i,k]/B[k,k]))
        
                if all ([i>k+1, j>k]):
                     C[i,j]=B[i,j]-(B[k+1,j]*(B[i,k+1]/B[k+1,k+1]))
        
                if i<k+2:
                    C[i,j]=B[i,j]
            
        B=C

#Backward Substitution
X[n-1]=C[n-1,n]/C[n-1,n-1]
for i in range(n-2,-1,-1):
    summation=0
    for k in range(i+1,n):
        summation=summation+C[i,k]*X[k]
        
    X[i]=(C[i,n]-summation)/C[i,i]  
    
print('The values of the unknown variables are respectively:')
print(X)

#Result Verification    
for i in range(n):
    summation=0
    for j in range(n):
        summation=summation+a[i,j]*X[j]
    
    p[i]=summation-a[i,j+1]

#The implementation is corrct if verification results are all zero
print('The verification results are:')
print(p)
print('The implementation is corrct if verification results are all zero')