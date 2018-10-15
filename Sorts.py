#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

""" 
@author:Administrator 
@file: Sorts.py
@desc: 排序算法
@notice:    java 的Collections.sort方法底层就是调用的Arrays.sort方法，而Arrays.sort使用了两种排序方法，快速排序和优化的归并排序(效率高且稳定的算法。)。
            python 使用了 Timsort 是结合了归并排序（merge sort）和插入排序（insertion sort）而得出的排序算法
@time: 2018/10/11 
"""

needOrderList = [1, 2, 8, 2, 90, 50, 35, 11, 258, 25, 16, 54, 74, 25, 36, 16, 42, 51, 16, 34, 15, 82, 71, 46, 92, 154,
                 58, 25, 65, 18, 59, 56, 6, 65, 1, 2, 87, 52, 5, 12, 5, 484, 546, 5, 45]
print("需要排序的列表为\n%s" % needOrderList)
selfOrderList = needOrderList[:]
selfOrderList.sort(key=None, reverse=True)
print("系统方法排序后列表为\n%s" % selfOrderList)

"""
"""


# 交换x y的值
def change(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y


"""
===============================================================冒泡排序(递归)===============================================================
"""


# 普通排序
def normal_sort(begin_index, normal_sort_list):
    length = len(normal_sort_list)
    if begin_index >= length:  # 迭代终止条件
        return normal_sort_list
    for i in range(begin_index, length):
        if normal_sort_list[begin_index] < normal_sort_list[i]:
            (normal_sort_list[begin_index], normal_sort_list[i]) = change(normal_sort_list[begin_index],
                                                                          normal_sort_list[i])
    return normal_sort(begin_index + 1, normal_sort_list)


begin = int(time.time())
print("冒泡排序耗时%s后列表为\n%s" % (int(time.time() - begin), normal_sort(0, needOrderList[:])))

"""
===============================================================冒泡排序(for循环)===============================================================
"""


def bubble_sort(bubble_sort_list):
    bubble_sort_list_len = len(bubble_sort_list)
    for i in range(0, bubble_sort_list_len - 1):
        for j in range(0, bubble_sort_list_len - 1 - i):
            if bubble_sort_list[j] < bubble_sort_list[j + 1]:
                # 交换
                (bubble_sort_list[j], bubble_sort_list[j + 1]) = change(bubble_sort_list[j], bubble_sort_list[j + 1])
    return bubble_sort_list


print("冒泡排序后列表为\n%s" % bubble_sort(needOrderList[:]))

"""
===============================================================双定向冒泡排序(鸡尾酒排序)===============================================================
"""


def cocktail_sort(cocktail_sort_list):
    length = len(cocktail_sort_list)
    for i in range(0, length // 2):
        for j in range(i, length - 1 - i):
            if cocktail_sort_list[j] < cocktail_sort_list[j + 1]:
                (cocktail_sort_list[j], cocktail_sort_list[j + 1]) = change(cocktail_sort_list[j],
                                                                            cocktail_sort_list[j + 1])
        for k in range(length - 1 - i, i, -1):
            if cocktail_sort_list[k - 1] < cocktail_sort_list[k]:
                (cocktail_sort_list[k - 1], cocktail_sort_list[k]) = change(cocktail_sort_list[k - 1],
                                                                            cocktail_sort_list[k])
    return cocktail_sort_list


print("双定向冒泡排序后列表为\n%s" % cocktail_sort(needOrderList[:]))

"""
===============================================================选择排序===============================================================
===========================选择排序是不稳定的排序算法，不稳定发生在最小元素与A[i]交换的时刻。=========================================
"""


def selection_sort(selection_sort_list):
    length = len(selection_sort_list)
    for i in range(0, length):
        for j in range(i + 1, length):
            if selection_sort_list[i] < selection_sort_list[j]:
                (selection_sort_list[i], selection_sort_list[j]) = change(selection_sort_list[i],
                                                                          selection_sort_list[j])
    return selection_sort_list


print("选择排序排序后列表为\n%s" % selection_sort(needOrderList[:]))

"""
===============================================================插入排序(Insertion Sort)===============================================================
=========================================================插入排序不适合对于数据量比较大的排序应用=====================================================
对于未排序数据(右手抓到的牌)，在已排序序列(左手已经排好序的手牌)中从后向前扫描，找到相应位置并插入。
插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，
需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
具体算法描述如下：
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5
"""


def insertion_sort(insertion_sort_list):
    length = len(insertion_sort_list)
    for i in range(1, length):
        temp = insertion_sort_list[i]
        j = i
        for j in range(i, -1, -1):
            if temp > insertion_sort_list[j - 1]:  # 如果大,就得让位置,往后移动
                insertion_sort_list[j] = insertion_sort_list[j - 1]
            else:  # 找到了对应的位置,将j的值得到了
                break
        insertion_sort_list[j] = temp
    return insertion_sort_list


print("插入排序后列表为\n%s" % insertion_sort(needOrderList[:]))

"""
==================================================插入排序的改进：二分插入排序====================================================
当n较大时，二分插入排序的比较次数比直接插入排序的最差情况好得多，但比直接插入排序的最好情况要差，
所当以元素初始序列已经接近升序时，直接插入排序比二分插入排序比较次数少。二分插入排序元素移动次数
与直接插入排序相同，依赖于元素初始序列。
"""
def half_insertion_sort(half_insertion_sort_list):
    length=len(half_insertion_sort_list)
    for i in range(length):
        temp =half_insertion_sort_list
        left =0
        right=i
        while right-left<=1:

            left =(right -left) //2
