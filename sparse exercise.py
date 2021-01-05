# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:12:46 2020

@author: TokTam
"""

Rows = int(input("Enter the number of Rows:"))
Columns = int(input("enter the number of columns:"))

Matrix = []
print ("Enter the rowwise:")
for i in range(Rows):
    a =[]
    for j in range (Columns):
        a.append(int(input()))
        matrix.append(a)
        print("__")
for i in range(Rows):
    for j in range(Columns):
        print(matrix[i][j])
        print()
        
##
Rows = int(input("Enter the number of rows:"))
Columns = int(input("Enter the number of columns:"))
Matrix1=[]
print("Enter the rowwise:")
for i in range(Rows):
    a =[]
    for j in range(Columns):
        a.append(int(input()))
        Matrix1.append(a)
print("__")
for i in range(Rows):
    for j in range(Columns):
        if matrix1[i][j] !=0:
print(Matrix1[i][j], end = " ")
        
print()
        