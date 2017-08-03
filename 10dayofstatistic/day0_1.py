#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 茫縁蒐 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
Day 0: Weighted Mean
"""

if __name__ == '__main__':
    N = int(raw_input())
    nList = raw_input().split()
    wList = raw_input().split()
    nList = map(int, nList)
    wList = map(int, wList)

    nSum = 0
    wSum = 0
    wSum = sum(wList)
    for i in range(N):
        nSum += nList[i]*wList[i]

    weightedMean = float(nSum)/wSum
    print ('%.1f' %weightedMean)
