# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 20:25
# craps.py
# @author: xyz
'''
from random import randint
a1 = randint(1, 6)
a2 = randint(1, 6)
first_sum = a1 + a2
i = 1
while True:
    a3 = randint(1, 6)
    a4 = randint(1, 6)
    sum = a3 + a4
    if i == 1:
        if first_sum == 7 or first_sum == 11:
            print('点数为%s玩家赢' % (first_sum))
            break
        elif first_sum == 2 or first_sum == 3 or first_sum == 12:
            print('点数为%s庄家赢' % (first_sum))
            break
        i = 0
    else:
        if sum == first_sum:
            print('点数为%s,与第一次相同,玩家赢' % (sum))
            break
        elif sum == 7:
            print('点数为%s庄家赢' % (sum))
            break