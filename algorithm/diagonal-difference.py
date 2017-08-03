#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 髣鯉ｽｫ驍ｵ竏ｬ險ｻ 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/diagonal-difference
Diagonal Difference
"""

import sys

def get_diagonal(arr, mode, n):
    result = []

    if mode == 0:
        for i in range(n):
            # print('%i %d'%(i, arr[i][i]))
            result.append(arr[i][i])
    if mode == 1:
        for i in range(n):
            result.append(arr[i][n-i-1])
    return result





if __name__ == '__main__':
    n = int(raw_input())
    arr = []
    for i in range(n):
        tmp = raw_input().split()
        tmp = map(int, tmp)
        arr.append(tmp)
    a = arr
    # print (a)

    d1 = get_diagonal(a, 0, n)
    d2 = get_diagonal(a, 1, n)
    s1 = sum(d1)
    s2 = sum(d2)
    print(abs(s1 - s2))


