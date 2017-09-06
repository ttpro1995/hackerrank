#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""

https://www.hackerrank.com/contests/openbracket-2017/challenges/because-owlery-is-too-lazy
Hogwarts Email Address
"""

def islowerall(ss):
    for s in ss:
        if not s.islower():
            return False
    return True

if __name__ =='__main__':
    fullmail = raw_input().rstrip().strip()
    if len(fullmail) < 18:
        print('No')
        quit()
    name_part = fullmail[0:5]
    if not islowerall(name_part):
        print('No')
        quit()
    domain_part = fullmail[5:]
    if domain_part != '@hogwarts.com':
        print ('No')
        quit()
    print ('Yes')
