#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: ZipMultiTest.py 
@time: 2018/11/23 
"""
import threading
import time
import datetime
import zipfile

file = r'D:\PycharmProjects\PythonStudy\dict.zip'
zFile = zipfile.ZipFile(file)
realPassword = 0


def getPassword(temp):
    global isFindPassword
    global realPassword
    try:
        for line in temp.readlines():
            if realPassword != 0:
                break
            password = line.strip('\n')
            print("当前线程是：%s 尝试的密码为 %s" % (threading.current_thread().getName(), password))
            try:
                zFile.extractall(path=r'D:\PycharmProjects\zipTest', members=zFile.namelist(),
                                 pwd=password.encode("ascii"))
                zFile.close()
                isFindPassword = True
                realPassword = password
                print("耗时  %1d  密码是：%2s" % (int(time.time()) - begin, realPassword))
            except Exception as ex:
                continue
    finally:
        temp.close()


def main():
    password_file1 = open(r'D:\PycharmProjects\PythonStudy\dict\1pass00.txt')
    password_file2 = open(r'D:\PycharmProjects\PythonStudy\dict\1pass01.txt')
    password_file3 = open(r'D:\PycharmProjects\PythonStudy\dict\1pass02.txt')
    password_file4 = open(r'D:\PycharmProjects\PythonStudy\dict\1pass03.txt')
    password_file5 = open(r'D:\PycharmProjects\PythonStudy\dict\eng_top_3000.txt')
    password_file6 = open(r'D:\PycharmProjects\PythonStudy\dict\password.txt')
    password_file7 = open(r'D:\PycharmProjects\PythonStudy\dict\pinyin2.txt')
    list = {password_file1, password_file2, password_file3,
            password_file4, password_file5, password_file6,
            password_file7}
    for temp in list:
        print(temp)
        t = threading.Thread(target=getPassword, args=(temp,))
        t.start()


begin = int(time.time())
if __name__ == '__main__':
    main()
