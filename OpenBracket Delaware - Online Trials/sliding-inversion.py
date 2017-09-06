#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/contests/openbracket-2017/challenges/sliding-inversion
Sliding Inversion
"""
import sys

def inversionCount(n, m, a):
    # Complete this function
    # n length
    # m sublength
    result = 0 # counter
    for i in range(n): # iterating the array
        for j in range(i+1, min(n, i+m)): # iterating the sublength
            if a[i] > a[j]:
                distance = j-i # total length of inversions (including i and j)
                result += min(i+1, m-distance, n-j) 
                # print(a[i], a[j], distance, min(i+1, m-distance+1, n-j))
    return result

if __name__ == "__main__":
    n, m = raw_input().split()
    m = int(m)
    n = int(n)
    a = raw_input().split()
    a = map(int, a)
    result = inversionCount(n, m, a)
    print (result)
