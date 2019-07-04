# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 19:19
# chicken_money.py
# @author: xyz
'''
'''
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
'''
for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 101, 3):
            if x * 5 + y * 3 + z / 3 == 100 and x + y + z == 100:
                print('雄鸡{0}母鸡{1}雏鸡{2}'.format(x, y, z))
