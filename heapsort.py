# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:30:12 2020

@author: Gautam_Pai
"""


def max_heapify(arr, heap_size, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if (left < heap_size) and (arr[largest] < arr[left]):
        largest = left
    if (right < heap_size) and (arr[largest] < arr[right]):
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)
    

def build_heap(arr):
    heap_size = len(arr);
    for i in range((heap_size//2), -1, -1):
        #print(i)
        max_heapify(arr, heap_size, i)
        
def heapsort(arr):
    heap_size = len(arr)
    build_heap(arr)
    
    print(arr)
    for i in range(heap_size-1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size-=1
        max_heapify(arr, heap_size, 0)
    
    return arr
    
A = [2,8,1,4,14,7,16,10,9,3]
heapsort(A)