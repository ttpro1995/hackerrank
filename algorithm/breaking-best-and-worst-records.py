#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 茫縁蒐 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records
Breaking the Records
"""
import sys
if __name__ == '__main__':
    n = int(raw_input())
    arr = raw_input().split()
    arr = map(int, arr)
    maxScore = -1
    minScore = sys.maxint
    breakmax = -1
    breakmin = -1
    for i in arr:
        if i > maxScore:
            # print ('max i %d'%i)
            maxScore = i
            breakmax += 1
        if i < minScore:
            minScore = i
            breakmin += 1
    print ('%d %d'%(breakmax, breakmin))


