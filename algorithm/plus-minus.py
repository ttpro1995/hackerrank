#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 息 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/plus-minus/problem
Plus Minus
"""

if __name__ == '__main__':
    n = int(raw_input())
    arr = raw_input().split()
    arr = map(int, arr)

    nPos = 0
    nNeg = 0
    nZ = 0
    for i in arr:
        if i > 0:
            nPos+=1
        elif i < 0:
            nNeg+=1
        else:
            nZ += 1
    total = nPos+nNeg+nZ
    fPos = float(nPos)/total
    fNeg = float(nNeg)/total
    fZ = float(nZ)/total
    print (fPos)
    print(fNeg)
    print(fZ)
