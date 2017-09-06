#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/tutorial-intro
"""
if __name__ == '__main__':
    V = int(raw_input())
    n = int(raw_input())
    arr = raw_input().split()
    arr = map(int, arr)
    idx = arr.index(V)
    print (idx)
