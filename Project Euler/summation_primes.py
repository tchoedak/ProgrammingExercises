# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 19:43:03 2014

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

@author: tenz
"""

def is_prime(m):
    isprime = True
    for i in range(2,long(m**.5) + 1):
        if m % i == 0 or m % long(m**.5) == 0:
            return False
    return isprime

def find_prime(num):
    primes_found = 0
    i = 2
    while primes_found < num:
        if is_prime(i):
            primes_found += 1
            if primes_found == num:
                return i
        i += 1



def summation_primes(N):
    i = 3
    tot_primes = 2
    while i < N:
        if is_prime(i):
            tot_primes += i
        i += 2
    return tot_primes