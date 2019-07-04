# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 18:14
# img_triangle.py
# @author: xyz
'''
row = int(input('请输入行数：'))
for i in range(1, row + 1):
    print('*' * i)

for i in range(1, row + 1):
    print(" " * (row - i), '*' * i)
for i in range(1, row + 1):
    print(" " * (row - i), end='')
    print("*" * (i * 2 - 1))
