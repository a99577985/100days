# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 12:53
# income_tax.py
# @author: xyz
'''
salary = float(input('pelease input your salary:'))
insurance = float(input('pelease input your insurance:'))
actual_salary = salary - insurance
tax = 0
income_more = actual_salary - 5000
if actual_salary <= 5000:
    pass
elif income_more < 3000:
    tax = income_more * 0.03
elif income_more > 3000 and income_more <= 12000:
    tax = income_more * 0.1 - 210
elif income_more > 12000 and income_more <= 25000:
    tax = income_more * 0.2 - 1410
elif income_more > 25000 and income_more <= 35000:
    tax = income_more * 0.25 - 2660
elif income_more > 35000 and income_more <= 55000:
    tax = income_more * 0.3 - 4410
elif income_more > 35000 and income_more <= 55000:
    tax = income_more * 0.3 - 4410
elif income_more > 55000 and income_more <= 80000:
    tax = income_more * 0.35 - 7160
elif income_more > 80000:
    tax = income_more * 0.45 - 15160
print('应缴税：%s' % (tax))
print('实际到手收入：%f' % (actual_salary - tax))
