# -*- coding: utf-8 -*-
'''
# Created on 6月-25-19 15:03
# prime.py
# @author: xyz
'''
# import math
num = int(input('please input number:'))
is_prime = True
if num == 1 or num == 2:
    pass
else:
    for i in range(2, int(num / 2)):
        if num % i == 0:
            is_prime = False
if is_prime:
    print('%d is prime' % (num))
else:
    print('%d is not prime' % (num))
