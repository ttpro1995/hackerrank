#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/s10-quartiles
"""

def median(arr):
    n = len(arr)
    idxl = []
    if n%2 == 0:
        idx2 = n/2
        idx1 = (n-1)/2
        result = (arr[idx1] + arr[idx2])/2
        idxl.append(idx1)
        idxl.append(idx2)
    elif n%2 == 1:
        idx = (n-1)/2
        idx1 = idx-1
        idx2 = idx+1
        result = arr[idx]
        idxl.append(idx1)
        idxl.append(idx2)
        
    return result, idxl


if __name__ == '__main__':
    n = raw_input()
    n = int(n)
    arr = raw_input().split()
    arr = map(int, arr)
    arr.sort()
    q2, idxl = median(arr)
    arr1 = arr[0:idxl[0]+1]
    arr2 = arr[idxl[1]:]
    #print(arr)
    #print(arr1)
    #print(arr2)
    q1, _ = median(arr1)
    q3, _ = median(arr2)
    print(q1)
    print(q2)
    print(q3)

