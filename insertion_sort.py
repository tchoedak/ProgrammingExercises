# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 16:04:28 2014
Insertion Sort
Input: Array
Output: Sorted Array

Method:
- Start with an n item array
- Start from index i=1 (not 0)
- Compare against index j(i-1, len())
- Swap if i=1 is less than i-1
- now compare j = i-1 with each preceding element
- Perform more swaps if j > j-1

complexity analysis:
    - there are theta(n) steps
    - each step has theta(n) comparisons and swaps
    - comparison can become very expensive for large arrays
    - worst case complexity is theta(n^2)
    - quick but expensive for large datasets


@author: tenz
"""

a = [3,4,1,5,2,6]

def insertion_sort(a):
    
    for i in range(1,len(a)):
        if a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            if i > 1:
                # check backwards 
                for j in range(i-1, 0,-1): 
                    if a[j] < a[j-1]:
                        a[j], a[j-1] = a[j-1], a[j]
    return a

a = insertion_sort(a)