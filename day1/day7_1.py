# -*- coding: utf-8 -*-
'''
# Created on 七月-04-19 13:11
# day7_1.py
# @author: xyz
'''


def triangles(rows=5):
    L = [1]
    S = []
    for _ in range(rows):
        yield L
        L = [1] + S + [1]
        S = []
        for i in range(len(L) - 1):
            S.append(L[i] + L[i + 1])


for i in triangles(9):
    print(i)
