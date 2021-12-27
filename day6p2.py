# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:42:27 2020

@author: User
"""

from functools import reduce
groups = open("day6.txt").read().split("\n\n")
def count(group):
    return reduce(set.intersection, map(set, group.split()))
questions = map(count, groups)
print(sum(map(len, questions)))