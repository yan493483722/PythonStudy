#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:Administrator
@file: First.py
@time: 2018/04/03
"""
import keyword

print(keyword.kwlist)

if True:
    print("true")
else:
    print("false")
# ! java  byte short int long float double boolean char
'''python  数据类型 int boolean  float complex '''
a = False
if a:
    print("a 的答案是 对的")
else:
    print("a 的答案是 错的")
一 = "我是汉字 "
print(一)
# inputString =input("请输入( 按enter 键退出):\n")
# print(inputString)
import sys

x = 'this is the Word '
sys.stdout.write(x + '\n')

a, b, c, d = 12, 21, 22, 'addsdaa'
sys.stdout.write(type(a) + " " + type(b) + " " + type(c) + " " + type(d))
import keyword

print(keyword.kwlist)
