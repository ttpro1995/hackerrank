#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 諱ｯ 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/sparse-arrays
Sparse Arrays
"""

if __name__ == '__main__':
    N = int(raw_input())
    sList = []
    for i in range(N):
        s = raw_input()
        sList.append(s)
    Q = int(raw_input())
    qList = []
    for q in range(Q):
        q = raw_input()
        qList.append(q)
    
    # go for every query
    for q in qList:
        ans = 0 
        for s in sList:
            if q == s:
                ans+=1
        print (ans)

