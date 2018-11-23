#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author:Administrator 
@file: ZipMultiTest.py 
@time: 2018/11/23 
"""
import threading
import zipfile

file = r"C:/Users/Administrator/Desktop/test.zip"
zFile = zipfile.ZipFile(file)


def getPassword(password):
    try:
        zFile.extractall(pwd=password.encode("ascii"))
        print(password)
        return
    except Exception as ex:
        pass


def main():
    zFile = zipfile.ZipFile(r'D:\PycharmProjects\PythonStudy\dict.zip')
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
        for line in temp.readlines():
            password = line.strip('\n')
            # print(password)
            t = threading.Thread(target=getPassword,args=(password))
            t.start()


if __name__ == '__main__':
    main()
