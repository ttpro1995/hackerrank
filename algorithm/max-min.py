#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/mini-max-sum
Mini-Max Sum
"""

if __name__ == '__main__':
    arr = raw_input().split()
    arr = map(int, arr)
    arr.sort()
    s = sum(arr)
    maxV = s - arr[0]
    minV = s - arr[4]
    print ('%d %d'%(minV, maxV))
