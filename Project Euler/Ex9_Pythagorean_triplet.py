# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 18:52:13 2014

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Method:
-algebraicly solve to get a = (500000 - 1000b)/(1000-b)
-if a is an integer, we assume we have found a,b

@author: tenz
"""

def make_triplet():
    
    found = False
    i = 1
    while found == False:
        a = (500000 - 1000*float(i))/(1000-i) 
        if a == int(a):
            if a**2 + i**2 == (1000-a-i)**2:
                found = True
        else:
            i+=1
    return a,i, (1000-a-i), a*i*(1000-a-i)

#375.0, 201, 424.0
