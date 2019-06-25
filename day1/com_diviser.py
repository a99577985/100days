# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 17:04
# com_diviser.py
# @author: xyz
'''
x = int(input('please input x:'))
y = int(input('please input y:'))
if x > y:
    (x, y) = (y, x)
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print('最大公约数为{0}'.format(i))
        print('最小公倍数为：%d' % (x * y // i))
        break