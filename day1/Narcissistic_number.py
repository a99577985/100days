# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 18:28
# Narcissistic_number.py
# @author: xyz
'''
'''
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
'''
for i in range(100, 1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i - b * 10 - a * 100
    if (a**3 + b**3 + c**3) == i:
        print(i)