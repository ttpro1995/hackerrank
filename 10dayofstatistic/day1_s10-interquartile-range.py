#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 茫縁蒐 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/s10-interquartile-range
"""
def median(arr):
    n = len(arr)
    idxl = []
    if n%2 == 0:
        idx2 = n/2
        idx1 = (n-1)/2
        result = float(arr[idx1] + arr[idx2])/2
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
    n = int(raw_input())
    s = raw_input().split()
    w = raw_input().split()
    s = map(int, s)
    w = map(int, w)
    arr = zip(s, w)
    
    # arr.sort(key= lambda x: x[0])
    arr = []
    for i in range(n):     
        t = [s[i]]*w[i]
        arr+=t
    arr.sort()
    n = len(arr)
    if n%2 == 0:
        idx1 = (n-1)/2
        idx2 = n/2
    elif n%2 == 1:
        idx = (n-1)/2
        idx1 = idx-1
        idx2 = idx+1
    # print(idx1)
    # print(idx2)
    arr1 = arr[:idx1+1]
    arr2 = arr[idx2:]
    # print(arr)
    # print(arr1)
    # print(arr2)
    
    q1, _ = median(arr1)
    q3, _ = median(arr2)
    q = q3 - q1
    print('%.1f'%q)
    
