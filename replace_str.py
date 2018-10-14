#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  replace_str.py
#  

import os
import re


def replace_str(input_file, str1, str2, output_file):
    f = open(input_file, "r")    #//打开文件，只读
    f2 = open(output_file, "w+")  #//打开文件，不存在，则创建
    line = f.readline()

    while line:
        line = f.readline()
        f2.write(line.replace(str1, str2)) #//写入f2，str1替换为str2
    print("替换完成")
    f.close()
    f2.close()




if __name__ == '__main__':
    replace_str("./1.txt", ";", "\n", "./2.txt")

