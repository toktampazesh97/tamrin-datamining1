# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 08:19:03 2020

@author: TokTam
"""

myList = input("Enter a string: ")
abcList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,26):
    print(myList[i]," is: " ,myList.count(abcList[i]))