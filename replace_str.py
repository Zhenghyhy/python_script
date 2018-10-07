#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  replace_str.py
#  

import os
import re


def replace_str(input_file, str1, str2, output_file):
    f = open(input_file, "r")    #//´òļþ£¬ֻ¶Á    f2 = open(output_file, "w+")  #//´òļþ£¬²»´æ£¬Ô´´½¨
    line = f.readline()

    while line:
        line = f.readline()
        f2.write(line.replace(str1, str2)) #//дÈf2£¬str1Ì»»Ϊstr2
    print("Ì»»Í³É)
    f.close()
    f2.close()




if __name__ == '__main__':
    replace_str("./1.txt", ";", "\n", "./2.txt")

