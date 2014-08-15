# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 20:24:17 2014
Anagram Checker

is_anagram:
for n characters, this function is O(n^2)

is_anagram2:
O(nlogn)

is_anagram3:
O(n)

@author: tenz
"""

def is_anagram(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    
    matches = 0
    for i in s1:
        if i in s2:
            matches += 1
    
    if matches == len(s1):
        return True
    else:
        return False
        

def is_anagram2(s1,s2):
    
    s1 = list(s1)
    s2 = list(s2)
    
    s1.sort() # 2*nlogn
    s2.sort()
    
    matches = True
    pos = 0
    
    while pos < len(s1) and matches == True:
        if s1[pos] == s2[pos]: #worst case n comparisons
            pos += 1
        else:
            matches = False
    
    return matches

def is_anagram3(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    
    count1 = {}
    for i in s1:
        if i in count1:
            count1[i] += 1
        else:
            count1[i] = 1
            
    count2 = {}
    for i in s2:
        if i in count2:
            count2[i] += 1
        else:
            count2[i] = 1
    #
    is_anagram = True
    for char in s1:
        # 'in' with dictionaries is O(1)
        if char in count2:
            # also O(1)
            if count1[char] != count2[char]:
                is_anagram = False
        else:
            is_anagram = False
    
    return is_anagram

def is_anagram4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

