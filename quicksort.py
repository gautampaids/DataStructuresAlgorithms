# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:13:12 2020

@author: Gautam_Pai
"""

def quicksort(numbers):
    if len(numbers) < 2:
        return numbers
    
    leftIndex, rightIndex = 0, len(numbers) - 1
    
    if leftIndex < rightIndex:
        partitionIndex = partition(numbers)
        left = quicksort(numbers[:partitionIndex])
        right = quicksort(numbers[partitionIndex+1:])
        
        return left + [numbers[partitionIndex]] + right


def partition(arr):
    leftindex = 0
    rightindex = len(arr)-1    
    pivotValue = arr[rightindex]
    while (rightindex > leftindex):
        
        while arr[leftindex] > pivotValue:
            #Swap the two values
            swap(arr,leftindex,rightindex)
            
            #partitionIndex -=1
            rightindex -=1
        leftindex += 1
    return rightindex


def swap(arr, i, pivotIndex):
    movethisnumbertotheright = arr[i]
    for j in range(i, pivotIndex): #shifting the numbers to left in left side of pivot
        arr[j] = arr[j+1]
    arr[pivotIndex] = movethisnumbertotheright


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
quicksort(numbers)