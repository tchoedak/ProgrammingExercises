# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 20:48:30 2014

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
@author: tenz
"""

def sum_of_squares(N):
    tot = 0
    for i in range(1,N+1):
        tot += i**2
    
    return tot

def square_of_sum(N):
    tot = 0
    for i in range(1,N+1):
        tot += i
    return tot**2

print square_of_sum(100) - sum_of_squares(100)