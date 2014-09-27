# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 03:40:05 2014

A palindromic number reads the same both ways. 
The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99. 
Find the largest palindrome made from the product of two 3-digit numbers.

Method:
- use a palindrome checker that checks half the string against the other half
  in reverse
- start i from 999 and compare against an iterator j from 999 down to 900
- (this assumes that a palindrome exists between 900 and 999)
- if no palindrome is found, iterate again against i-1, iterate
- if a palindrome is found, the program stops

This program has the advantage of stopping iteration immediately after
the largest palindrome is found. 

Complexity
Worst case: O(n^2)
Best case: O((999-i)+(999-k))

@author: tenz
"""
# 3 digits
max = 999 * 999

def is_palindrome(num):
    palin = str(num)
    if palin[:len(palin)/2] == palin[:len(palin)/2 -1:-1]:
        return True
    else:
        return False

def digit_palindrome():
    
    # go downwards instead from 999 onwards and stop at the first palindrome
    
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            if is_palindrome(i*j):
                return i*j
    