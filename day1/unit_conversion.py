# -*- coding: utf-8 -*-
'''
# Created on 6月-24-19 21:05
# unit_conversion.py
# @author: xyz
'''
length = float(input('请输入长度:'))
unit = str(input('请输入单位：'))
if unit == '英寸':
    conversion_length = length * 2.54
    print('%.1f' % (conversion_length))
elif unit == '厘米':
    conversion_length = length / 2.54
    print('%.1f' % (conversion_length))
else:
    print('please input correct unit')
