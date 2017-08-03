#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 髣鯉ｽｫ驍ｵ竏ｬ險ｻ 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
Mean median and Mode
"""
from collections import Counter

def calMean(arr, N):
    # sum and divide by N
    s = sum(arr)
    mean = float(s)/N
    return mean

def calMedian(arr, N):
    # get the middle 
    # odd case
    arr.sort()
    if N%2 == 1:
        middle = N/2
        return arr[middle]
    if N%2 == 0: # even case
        middle1 = N/2
        middle2 = N/2-1
        median = float(arr[middle1]+ arr[middle2])/2
        return median

def calMode(arr, N):
    arr.sort()
    c = Counter(arr).most_common()
    mode = c[0][0]
    num = c[0][1] # counting of most common 
    l = []
    for i in range(len(c)):
        # print (c[i])
        if c[i][1] == num: # most popular value
            l.append(c[i][0])
    l.sort()
    # print(c)
    # print(l)
    
    return l[0]
    



if __name__ == '__main__':
    N = raw_input()
    N = int(N)
    arr = raw_input().split()
    arr = map(int, arr)
    mean = calMean(arr, N)
    median = calMedian(arr, N)
    mode = calMode(arr, N)
    print (mean)
    print(median)
    print (mode)



