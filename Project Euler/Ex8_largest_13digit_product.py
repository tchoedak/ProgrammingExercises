# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 15:46:32 2014
problem 8
Largest product in a series

The four adjacent digits in the 1000-digit number that have the 
greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have 
the greatest product. What is the value of this product?

Method:

- read the entire series as a string
- starting from 0, find the product of the 13 adjacent digits
- store this product as a variable
- move each digit + 1
- calculate new product and compare
- if new product is greater, replace older product, continue
- end when reaching end of list

@author: tenz
"""


num_string = ''.join(
'''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
70172427121883998797908792274921901699720888093776
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''.split('\n'))


def product_of_digits(string_number):
    m = len(string_number)
    product = long(1)
    for i in range(m):
        product *= long(string_number[i])
    return product
    
def find_largest_product(string, digits):
    i = 0
    max_ind = len(string) - digits
    largest_product = product_of_digits(string[0:digits])
    while i < max_ind:
        i += 1
        new_product = product_of_digits(string[i:i+digits])
        if new_product > largest_product:
            largest_product = new_product
    
    return largest_product

def find_nonzeros(string):
    max_ind = len(string) - 13
    nonzeros = []
    i = 0
    while i < max_ind:
        if '0' not in string[i:i+13]:
            nonzeros.append(string[i:i+13])
        i += 1
    return nonzeros