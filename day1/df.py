# -*- coding: utf-8 -*-
'''
# Created on 6月-28-19 13:41
# df.py
# @author: xyz
'''
# def is_palindrome(num):
#     if num<0:
#         return False
#     temp=str(num)
#     if temp.__len__


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


if __name__ == "__main__":
    print(is_palindrome(121121))