# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:50:38 2023

@author: Dell 7490
"""

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)
    
    return A

def Partition(A, p, r):
    x = A[r]

    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1

            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

Arr = [1, 6, 3, 9, 6, 0, 2]

print(QuickSort(Arr, 0, len(Arr) - 1))
