# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 15:17:34 2014

Given a list of numbers in random order write a linear time 
algorithm to find the kth smallest number in the list. 
Explain why your algorithm is linear.

@author: tenz
"""

def find_kth(k, randlist):
    pos = 0
    # O(1)
    ordered_list = []
    
    # total cost of this operation:
    # O(n) * O(1) = O(n)
    while len(ordered_list) < k:
        # O(n) operation
        if pos in randlist:
            #O(1) operation
            ordered_list.append(pos)
            pos += 1
        else:
            pos += 1
    
    # O(1) operation
    return ordered_list[k-1]
