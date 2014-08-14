# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 23:03:52 2014

A game is being played with the following rules : 
The first player says 1, the next 2 and so on. 
If a number is a multiple of 4 or 7 then that number is skipped and the next number is spoken. 
However if the number is a multiple of both 4 and 7 then the number is not skipped. 
Define a function which taken a number n as input and returns the nth number which will be spoken. 
nthNumber(10) = 15 (the order of numbers spoken is 1,2,3,5,6,9,10,11,13,15)

@author: tenz
"""

def nthNumber(N):
    Nlist = []
    for i in range(1,100):
        if i % 4 == 0 and i % 7 == 0:
            Nlist.append(i)
        if i % 4 == 0 or i % 7 == 0:
            next
        else:
            Nlist.append(i)
    print Nlist[len(Nlist)-1]
            
