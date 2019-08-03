#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:Administrator
@file: .py
@time: 2018/09/10

"""

'''http://www.runoob.com/
http://www.runoob.com/python/python-100-examples.html
'''

''' Test 3 '''

'''一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
假设该数为 x。
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数 而m n 都为正整数 所以 m>n
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
7、接下来将 i 的所有数字循环计算即可。
'''
for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and i % 2 == 0 and j % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = m ** 2 - 168 - 100
            print("m = %d" % m, "n = %d" % n, "这个数是: %d" % x)

''' Test 4 '''
'''输入某年某月某日，判断这一天是这一年的第几天？'''


def myMethod():
    s = input("请输入年月日,中间以/分隔")
    dateArr = []
    allDate = 0
    try:
        for date in s.split("/"):
            dateArr.append(date)
        year = int(dateArr[0])
        month = int(dateArr[1])
        day = int(dateArr[2])
        '''是否是闰年'''
        for m in range(1, month):
            if m <= 7:
                if m % 2 == 1:
                    allDate += 31
                else:
                    if m == 2:
                        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
                            allDate += 29
                        else:
                            allDate += 28
                    else:
                        allDate += 30
            else:
                if m % 2 == 1:
                    allDate += 30
                else:
                    allDate += 31
        allDate += day
    except BaseException as e:
        print("输入非法引起了: %s" % e.__str__(), "  异常")
    print("这是%s年的第%s天" % (year, allDate))
    # myMethod()


myMethod()
