#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 髣鯉ｽｫ驍ｵ竏ｬ險ｻ 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/crush
Algorithmic Crush
"""
def query(arr, a, b, k):
    a= int(a)-1
    b = int(b)
    k = int(k)
    for i in range(a, b):
        arr[i] +=k

def create_tuple(a, b, k):
    b = b + 1
    return [(a, k), (b, -k)]

def evaluate(sorted_tup):
    max = 0
    cur = 0
    prev_idx = 0 # inclusive case
    # for tup in sorted_tup:
    for i in range(len(sorted_tup)):
        tup = sorted_tup[i]
        if i + 1 < len(sorted_tup):
            next = sorted_tup[i+1][0]
        else:
            next = -1
        cur += tup[1]
        if cur > max and next!= tup[0]:
            max = cur
        prev_idx = tup[0]
    return max

if __name__ == '__main__':
    N, M = raw_input().split()
    N = int(N)
    M = int(M)
    # arr = [0]*N
    arr_tup = []
    for i in range(M):
        a, b, k = raw_input().split()
        a = int(a)
        b = int(b)
        k = int(k)
        # query(arr, a, b, k)
        arr_tup += create_tuple(a,b,k)
    sorted_tup = sorted(arr_tup, key=lambda x: x[0])
    maxValue = evaluate(sorted_tup)
    print (maxValue)
