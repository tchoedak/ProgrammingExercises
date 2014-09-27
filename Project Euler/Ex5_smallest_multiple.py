# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 18:46:39 2014
2520 is the smallest number that can be divided by each 
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
@author: tenz
"""

# we know that most numbers are divisble by 2 or 3
# the one's that are more rare are prime numbers
# 11, 13, 17, 19
# one way to tackle this problem is to
# find all divisible by both 2 and 3, then check
# 11, 13, 17, and 19
def smallest_multiple():
    
    # start from 2520
    N = 1
    found = False
    while found == False:
        N += 1
        if N % 11 == 0:
            if N % 13 == 0:
                if N % 14 == 0:
                    if N % 15 == 0:
                        if N % 17 == 0:
                            if N % 18 == 0:
                                if N % 19 == 0:
                                    found = True
    return N

def smallest_multiple2():
    
    N = 2520
    i = 10
    while i < 20:
        if N % i == 0:
            i += 1
        else:
            N *= i
    return N
    # best answer is 1862340480 (not true)

def smallest_multiple3():
    N = 2520
    # use primes this time
    found = False
    while found == False:
        N += 20
        if N % 11 == 0:
            if N % 12 == 0:
                if N % 13 == 0:
                    if N % 17 == 0:
                        if N % 19 == 0:
                            if N % 15 == 0:
                                if N % 16 == 0:
                                    if N % 14 == 0:
                                        if N % 18 == 0:
                                            found = True
    return N