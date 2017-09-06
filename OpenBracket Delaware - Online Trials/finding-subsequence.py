#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/contests/openbracket-2017/challenges/finding-subsequence
Finding Subsequence
"""


import sys
from collections import Counter

def solve(s, k):
    # k condition
    counts = Counter(s).most_common()
    alphabet = []
    for c in counts:
        if c[1] >=k:
            alphabet.append(c[0])
    dcounts = dict(counts)
    # print ('dcounts', dcounts)
    alphabet.sort(reverse=True) # get highest first
    # print ('alphabet', alphabet)
    # scan the s
    i = 0 # pointer
    n = len(s) # length
    result = []
    for ch in alphabet:
        while dcounts[ch] > 0: # still have word
            # print ('s[i] and ch ', s[i], ch)
            if s[i] == ch:
                dcounts[ch] -=1 # reduce the counter 
                result.append(ch)
            elif s[i] in dcounts:
                if dcounts[s[i]] <= k:
                    dcounts[s[i]] = 0
                else:
                    dcounts[s[i]] -= 1 
            i += 1
            if i >= n:
                return ''.join(result)
    return ''.join(result)

if __name__ == "__main__":
    s = raw_input().strip()
    k = int(raw_input().strip())
    result = solve(s, k)
    print result
