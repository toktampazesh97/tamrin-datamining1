# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 08:05:27 2020

@author: TokTam
"""

myList = input("Enter a List or Word: ")
str2 = ""
for i in range(len(myList)):
      if(i % 2 == 0):
          str2 = str2 + myList[i]
print("original string :  ", myList)
print("Final string :    ", str2)