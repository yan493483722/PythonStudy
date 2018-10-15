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

''' Test 5 '''

'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

可手写冒泡排序
'''


def max(x, y, z):
    if x > y:
        if x > z:
            if y > z:
                print("三个数从大到小排列为 %s %s %s" % (x, y, z))
            else:
                y = y + z
                z = y - z
                y = y - z
                max(x, y, z)
        else:
            x = x + z
            z = x - z
            x = x - z
            max(x, y, z)
    else:
        # xy 交换值
        x = x + y
        y = x - y
        x = x - y
        max(x, y, z)


s = input("输入x,y,z中间以逗号(,)区分")
dataArr = s.split(",")
resultArray = []
for s in dataArr:
    resultArray.append(s)
max(int(resultArray[0]), int(resultArray[1]), int(resultArray[2]))

'''
排序  @link
'''

'''
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：

'''
