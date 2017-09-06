#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2017  <@ThaiThien>
#
# Distributed under terms of the MIT license.

"""
https://www.hackerrank.com/challenges/torque-and-development/problem
"""

def fullAccess(checker):
    s = sum(checker)
    t = len(checker)
    if s == t:
        return True
    return False


def make_adj_matrix(roadList, n):
    matrix = []
    for i in range(n):
        matrix.append([])

    for road in roadList:
        matrix[road[0]].append(road[1])
        matrix[road[1]].append(road[0])
    return matrix

def buildRoad(cityChecker, start, matrix):
    # builtList = []
    built = 0
    # print ('road list ')
    # print (roadList)
    n = len(matrix)
    for i in matrix[start]:
        if cityChecker[i] == 0:
            built+=1 
            cityChecker[i] = 1
            built+= buildRoad(cityChecker, i, matrix)
    return built

def query(n, m, cl, cr, roadList):
    if cl <= cr: # built lib cheaper, 1 per city
        return cl*n
    else: # road cheaper
        built_lib= 0 
        built_road= 0
        cityChecker = [0]*n # not access yet
        matrix = make_adj_matrix(roadList, n)
        # while not fullAccess(cityChecker): 
        for i in range(n):
            if not cityChecker[i]:
                cityChecker[i] = 1 # built lib
                built_lib+=1
                built_road+= buildRoad(cityChecker, i, matrix)
        return cl*built_lib + cr*built_road





if __name__ == '__main__':
    q = int(raw_input())
    for a in range(q):
        x = raw_input().split()
        x = map(int, x)
        n, m, cl, cr = x
        roadList = []
        for i in range(m):
            u, v = raw_input().split()
            u = int(u)-1
            v = int(v)-1
            roadList.append((u, v))
        result = query(n,m, cl, cr, roadList)
        print (result)
