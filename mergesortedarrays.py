# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:13:08 2020

@author: Gautam_Pai
"""


def mergeSortedArrays(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    
    mergedArray = []    
    arrayItem1 = arr1[0]
    arrayItem2 = arr2[0]
    i = 1
    j = 1
    
    while True:    
        if arrayItem1 < arrayItem2:
            mergedArray.append(arrayItem1)
            
            if i != len(arr1):
                arrayItem1 = arr1[i]
                i = i+1
            else:
                mergedArray += arr2[j-1:]
                return mergedArray
        else:
            mergedArray.append(arrayItem2)
            
            if j != len(arr2):                
                arrayItem2 = arr2[j]
                j = j+1
            else:
                mergedArray += arr2[i-1:]
                return mergedArray


mergeSortedArrays([0,2,3,4], [0,5,6])