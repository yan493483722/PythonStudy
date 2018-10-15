#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: Games.py 
@time: 2018/08/27 
"""
"""
pythonchallenge
http://www.pythonchallenge.com/
"""
# 第一关
middle = 2 ** 38
webset = "http://www.pythonchallenge.com/pc/def/%s.html"
print(webset % middle)
# 第二关
info = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
# K-M  O-Q E-G
print(info)
for i in info:
    if 'a' <= i <= 'Z':
        i = chr(i + 2)
    else:
        continue


print(info)
