#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 諱ｯ 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/array-left-rotation/problem
Left Rotation
"""

if __name__ == '__main__':
    n, d = raw_input().split()
    n = int(n)
    d = int(d)
    arr = raw_input().split()
    arr = map(int, arr)
    for i in range(d):
        x = arr.pop(0)# get the left value
        arr.append(x) # put to the end of the list
    arr = map(str, arr)
    s = ' '.join(arr)
    print (s)
