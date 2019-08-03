#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: ZipTest.py
@time: 2018/11/23 
"""
import itertools as its
import time
import zipfile

file = r"C:/Users/z7/Desktop/test.zip"
zResult = r"C:/Users/z7/Desktop/zResult"
zInput = zipfile.ZipFile(file)


def tryPwd(countNum):
    begin = int(round(time.time() * 1000))
    print("开始是 {} 毫秒", begin)
    # words = "0123456789"
    words = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for count in range(1, countNum + 1):
        r = its.product(words, repeat=count)
        s, ms = divmod(int(round(time.time() * 1000)) - begin, 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        print("前%1s位耗时%2d时%2d分%2d秒%d毫秒" % (count - 1, h, m, s, ms))
        print("正在尝试第：" + str(count) + "位")
        find = False
        for i in r:
            pwd = "".join(i)
            try:
                #     # do you work here
                zInput.extractall(zResult, members=zInput.namelist(),
                                  pwd=pwd.encode("ascii"))
                zInput.close()
                print("破解的密码是:%s" % pwd)
                find = True
                break
            except Exception as e:
                # print("尝试密码:%s 出错了" % pwd)
                continue
        if find:
            break
    s, ms = divmod(int(round(time.time()) * 1000) - begin, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("总共耗时%3d天%2d时%2d分%2d秒%d毫秒" % (d, h, m, s, ms))


tryPwd(5)
