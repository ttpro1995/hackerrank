#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 息 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/birthday-cake-candles
Birthday Cake Candles
"""
from collections import Counter

if __name__ == '__main__':
    n = int(raw_input())
    arr = raw_input().split()
    arr = map(int, arr)
    c = Counter(arr).most_common()
    print (c[0][1])

    
