# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 10:32
# area_of_circle.py
# @author: xyz
'''
import math
r = float(input('请输入半径:'))
area = (r**2) * math.pi
perimeter = 2 * math.pi * r
print('面积为%.3f 周长为%.3f' % (area, perimeter))