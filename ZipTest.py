#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: ZipTest.py
@time: 2018/11/23 
"""
import itertools as its
import zipfile

zFile = ""
file = r"C:/Users/Administrator/Desktop/test.zip"


def tryPwd(countNum):
    words = "0123456879"
    for count in range(1, countNum):
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


tryPwd(20)
