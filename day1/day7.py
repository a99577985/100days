# -*- coding: utf-8 -*-
'''
# Created on 七月-03-19 17:50
# day7.py
# @author: xyz
'''
# import os
# import time

# def main():
#     content = 'hello,five.......'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.1)
#         content = content[1:] + content[0]

# if __name__ == "__main__":
#     main()
# import random

# def generate_code(lenth=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(lenth):
#         index = random.randint(0, last_pos)
#         code = all_chars[index] + code
#     return code

# if __name__ == "__main__":
#     print(generate_code(10))

# def get_suffix(filename, has_dot=False):
#     index = filename.find('.')
#     if has_dot is False:
#         suffix = filename[index:]
#     else:
#         suffix = filename[index + 1:]
#     return suffix

# if __name__ == "__main__":
#     print(get_suffix('asdjk.jpg', True))

# def max2(x):
#     a = x[0]
#     b = x[1]
#     if a < b:
#         (a, b) = (b, a)
#     for i in range(2, len(x) - 1):
#         if x[i] > a and x[i] > b:
#             b = a
#             a = x[i]
#         elif x[i] <= a and x[i] > b:
#             b = x[i]
#     print(a, b)

# if __name__ == "__main__":
#     max2([9, 8, 1, 51, 24, 523, 63, 4, 129, 2])


# def is_leap_year(year):
#     # if year % 100 == 0:
#     #     if year % 400 == 0:
#     #         return True
#     #     else:
#     #         return False
#     # elif year % 4 == 0:
#     #     return True
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def which_day(year, mouth, date):
#     days_of_month1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days_of_month2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days = 0
#     if is_leap_year(year):
#         for i in range(mouth - 1):
#             days += days_of_month2[i]
#     else:
#         for i in range(mouth - 1):
#             days += days_of_month1[i]
#     return days + date


# if __name__ == "__main__":
#     print(which_day(2000, 3, 1))
