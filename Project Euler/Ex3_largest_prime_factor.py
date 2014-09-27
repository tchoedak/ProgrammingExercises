# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 17:58:56 2014

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Method:
- Take in an input prime number
- find all prime factors from 1 to sqrt(N)
* N*N are potentially the biggest factors
* primes can only exist below N (since if N*N = our number, there are at least
 divisors 1, and N)
* We can optimize by removing even numbers (even numbers are always divisible by 2)
* All primes are of the form (6k+i)
- generate an array of primes up to N-1
- for each prime added, check whether it is a factor of our number
- return the last number in our array

@author: tenz
"""

def is_prime(m):
    isprime = True    
    if m % 2 == 0:
        isprime = False
    for i in range(3,long(m**.5)):
        if m % i == 0:
            return False
    return isprime
    
def primes_sieve(m):
    not_prime = []
    primes = []
    
    for i in range(2,m):
        if i in not_prime:
            continue
        for f in range(i*2,m,i):
            not_prime.append(f)
        primes.append(i)
    
    return primes

def largestPrimeFactorFast(num):
    primes = []
    for i in range(2,int(num**.5)):
        if num % i == 0 and is_prime(i):
            primes.append(i)
    return primes

largestPrimeFactorFast(600851475143)

