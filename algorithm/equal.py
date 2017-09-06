#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/equal/problem
instead give chocolate, we take aways
"""

def f(x):
    total = 0
    cur = x
    total+= cur/5
    cur = cur%5
    total += cur/2
    cur = cur%2
    total+=cur
    return total


def solve(arr, n):
    arr.sort()
    smallest = arr[0]
    arr = [x-smallest for x in arr]
    total = [0, 0, 0, 0, 0]
    for i in range(5):
        for c in range(n):
            cur = arr[c] + i
            total[i]+= f(cur)
    return min(total)


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        N = int(raw_input())
        arr = raw_input().split()
        arr = map(int, arr)
        result = solve(arr, N)
        print (result)
