#!/usr/bin/python
# -*- coding: utf-8 -*-


def maximumStones(arr):
    evnsum = 0
    odsum = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            evnsum = evnsum + arr[i]
        else:
            odsum = odsum + arr[i]
    if evnsum >= odsum:
        return 2 * odsum
    else:
        return 2 * evnsum
