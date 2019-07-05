# -*- coding: utf-8 -*-
'''
# Created on 七月-04-19 13:11
# day7_1.py
# @author: xyz
'''

# def triangles(rows=5):
#     L = [1]
#     S = []
#     for _ in range(rows):
#         yield L
#         L = [1] + S + [1]
#         S = []
#         for i in range(len(L) - 1):
#             S.append(L[i] + L[i + 1])

# for i in triangles(9):
#     print(i)

# from random import randint, sample


# def display(balls):
#     for index, ball in enumerate(balls):
#         if index == (len(balls) - 1):
#             print("|", end="")
#         print("%02d" % ball, end=" ")


# def ball_select():
#     red_balls = [x for x in range(1, 34)]
#     select_balls = []
#     select_balls = sample(red_balls, 6)
#     select_balls.sort()
#     select_balls.append(randint(1, 16))
#     return select_balls


# if __name__ == "__main__":
#     n = int(input('投注：'))
#     for _ in range(n):
#         display(ball_select())
#         print("")

"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中
15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报
数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海
里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开
始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()