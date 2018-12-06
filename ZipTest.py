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
    begin = int(time.time())
    time.sleep(10)
    words = "0123456879"
    # localtime = time.localtime(time.time())
    # print("本地时间为 :", localtime)
    # localtime = time.asctime(time.localtime(time.time()))
    # print("本地时间为 :", localtime)
    # for count in range(1, countNum + 1):
    #     r = its.product(words, repeat=count)
    #     print("试到了：" + str(count) + "位")
    #     pwd = ""
    #     for i in r:
    #         pwd = "".join(i)
    #         zFile = zipfile.ZipFile(file)
    #         try:
    #             print(pwd)
    #             zFile.extractall(pwd=pwd.encode("ascii"))
    #             print(pwd)
    #             return
    #         except Exception as ex:
    #             continue
    delay=(time.time()) - begin
    print(delay.strftime("%I:%M:%S"))
    print("耗时%d" % (int(delay)))


tryPwd(0)
