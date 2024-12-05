# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:12:22 2022

@author: D. A. Palash
"""


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
loc = (r'H:\Education\3-1 3rd Year Odd Semester - ETE 18\Numerical Method\Lab\data.xls')


wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(4)

#creating matrix from the data 
for i in range(sheet.ncols):
    for j in range(sheet.nrows):
        #print(sheet.cell_value(1, i))
        a[j,i]=sheet.cell_value(j, i)
        print(a[j,i])
