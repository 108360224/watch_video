# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:17:56 2020

@author: max
"""


def greet(name):
    print("--- hello,%s ---" % name)

def add(a,b):
    return a + b

def sub(count,a=0,b=0,c=0):
    return count - a - b -c

def get_list(a,b,c,d):
    return [[a,[b,c],d],[a,b,c,d]]

def print_list(data):
    print(type(data))
    # 遍历Java的ArrayList对象
    for i in range(data.size()):
        print(data.get(i))
