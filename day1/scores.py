# -*- coding: utf-8 -*-
'''
# Created on 6月-24-19 23:21
# scores.py
# @author: xyz
'''
score = int(input('输入成绩：'))
if score >= 100 or score < 0:
    level = '你吓唬谁呢'
elif score >= 90 and score <= 100:
    level = 'A'
elif score >= 80:
    level = 'B'
elif score >= 70:
    level = 'C'
elif score >= 60:
    level = 'D'
elif score >= 0:
    level = 'E'
print('你的成绩是:%s' % (level))
