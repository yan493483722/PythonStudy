#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: ZipTest.py
@time: 2018/11/23 
"""
import itertools as its
import time

zFile = ""
file = r"C:/Users/Administrator/Desktop/test.zip"


def tryPwd(countNum):
    begin = int(time.time())
    # words = "0123456879"
    words = "0123456879ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for count in range(1, countNum + 1):
        r = its.product(words, repeat=count)
        m, s = divmod(int(time.time()) - begin, 60)
        h, m = divmod(m, 60)
        print("前%1s位耗时%2d时%2d分%2d秒" % (count - 1, h, m, s))
        print("正在尝试第：" + str(count) + "位")
        for i in r:
            pwd = "".join(i)
            try:
                #     # do you work here
                print("正在尝试密码:%s" % pwd)
            except Exception:
                print("尝试密码:%s 出错了" % pwd)
                continue
    m, s = divmod(int(time.time()) - begin, 60)
    h, m = divmod(m, 60)
    print("总共耗时%2d时%2d分%2d秒" % (h, m, s))


tryPwd(6)
