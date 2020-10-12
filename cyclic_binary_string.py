#!/usr/bin/python
# -*- coding: utf-8 -*-


def get_pow(k):
    count = 0
    m = 0
    for i in range(len(k)):
        if k[i] == '0':
            count = count + 1
        else:
            if m < count:
                m = count
            count = 0
    if m < count:
        m = count
    return m

def maximumPower(s):
    w = 0
    flag = 0
    n = len(s)
    k = list(s)
    for i in range(n):
        t = k.pop()
        k.insert(0, t)
        if k[0] == '1':
            w = get_pow(k)
            break
        flag = flag + 1
    if flag == n:
        return -1
    else:
        return w
