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

zFile = ""
file = r"C:/Users/Administrator/Desktop/test.zip"


def tryPwd(countNum):
    begin = time.time()
    words = "0123456879"
    print("开始时间%f" % begin)
    localtime = time.localtime(time.time())
    print("本地时间为 :", localtime)
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)
    for count in range(1, countNum + 1):
        r = its.product(words, repeat=count)
        print("试到了：" + str(count) + "位")
        pwd = ""
        for i in r:
            pwd = "".join(i)
            zFile = zipfile.ZipFile(file)
            try:
                print(pwd)
                zFile.extractall(pwd=pwd.encode("ascii"))
                print(pwd)
                return
            except Exception as ex:
                continue
    print("耗时%f" % (time.time() - begin))


tryPwd(0)
