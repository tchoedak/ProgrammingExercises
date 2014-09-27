# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 15:03:12 2014

@author: tenz
"""
def ThreeOrFive(N = 1000):
    num = N-1
    factors = []
    total = 0

    while num > 2:
        if num % 3 == 0 or num % 5 == 0:
            factors.append(num)
            total += num
        num -= 1
    
    return total