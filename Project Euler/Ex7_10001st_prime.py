# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 23:22:00 2014

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?

Method:
- keep record of primes by doing primes_found += 1 each time one is found
- use is_prime to determine if prime
- is_prime builds an array i from 2, up to the sqrt of a number
- once sufficient number of primes have been found, stop
@author: tenz
"""
import timeit


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

start = timeit.timeit()
find_prime(10001)
end = timeit.timeit()

print end-start
