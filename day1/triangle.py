# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 09:51
# triangle.py
# @author: xyz
'''
import math
a = float(input('边1：'))
b = float(input('边2：'))
c = float(input('边3：'))
if a + b > c and a + c > b and b + c > a:
    tri_perimeter = a + b + c
    half_perimeter = tri_perimeter / 2
    # 面积公式周长的一半p=1/2(a+b+c)
    # S = math.sqrt(p*(p-a)(p-b)(p-c))
    tri_area = math.sqrt(half_perimeter * (half_perimeter - a) *
                         (half_perimeter - b) * (half_perimeter - c))
    print(("周长为：%s") % (tri_perimeter))
    print(str("面积为：%s") % (tri_area))
else:
    print('该条件无法构成三角形')
