#!/usr/bin/python
# -*- coding: utf-8 -*-
str = ['First', 'Second']


def whoIsTheWinner(arr):
    length = len(arr)
    nondup = 0
    dup = 0
    d = {}
    for i in range(length):
        t = arr.pop()
        if t in d:
            d[t] = d[t] + 1
            dup = dup + 1
        else:
            d[t] = 1
            nondup = nondup + 1
    if dup == 0:
        return str[0]
    else:
        k = nondup + dup - 1
        return str[k % 2]
