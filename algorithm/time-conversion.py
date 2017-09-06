#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 髣鯉ｽｫ驍ｵ竏ｬ險ｻ 2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/time-conversion
time conversion
"""

if __name__ == '__main__':
    # while True:
    
    s = raw_input()
    t = s[0:-2]
    ext = s[-2:]
    if ext == 'AM':
        h = t[0:2]
        h = int(h)
        if h == 12:
            hs = '00'
            ms = t[2:]
            t = ''.join([hs, ms])
        print (t)
    elif ext == 'PM':
        h = t[0:2]
        h = int(h)
        h+=12
        if h == 24: # not yet
            h = 12
        if h<10:
            hs = ''.join([str(0), str(h)])
        else:
            hs = str(h)
        ms = t[2:]
        t = ''.join([hs, ms])

        print (t)
    # print (t)
    # print (ext)
