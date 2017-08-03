#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 諱ｯ 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/staircase
Stair Case
"""

if __name__ == '__main__':
    n = int(raw_input())
    base = [' ']*n
    for i in range(n):
        idx = n-i-1
        base[idx] = '#'
        s = ''.join(base)
        print(s)

