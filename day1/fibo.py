# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 19:49
# fibo.py
# @author: xyz
'''


def fibo(n):
    (a, b) = (0, 1)
    fibo_arr = []
    fibo_arr.append(b)
    for i in range(1, n):
        fibo_arr.append(a + b)
        a = fibo_arr[i - 1]
        b = fibo_arr[i]
    return fibo_arr


print(fibo(10))
