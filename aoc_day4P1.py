# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:23:20 2020

@author: User
"""
import re

in_file = 'day4.txt'
file_in = open(in_file, 'r')


data_list = file_in.read().split('\n\n')
data_len = len(data_list)
file_in.close()

by = 'byr'
iy = 'iyr'
ey = 'eyr'
ht = 'hgt'
hc = 'hcl'
ec = 'ecl'
pd = 'pid'
cd = 'cid'


mandatory1 = [by, iy, ey, ht, hc, ec, pd]
valid = 0
for d in range(data_len):
    tc = 0
    for m in range(len(mandatory1)):
        x = re.search(mandatory1[m], data_list[d])
        if x:
            tc += 1
    if tc == 7:
        valid += 1

# def find_each_and_replace_by(string, substring, separator='x'):
#     """
#     list(find_each_and_replace_by('8989', '89', 'x'))
#     # ['x89', '89x']
#     list(find_each_and_replace_by('9999', '99', 'x'))
#     # ['x99', '9x9', '99x']
#     list(find_each_and_replace_by('9999', '89', 'x'))
#     # []
#     """
#     index = 0
#     while True:
#         index = string.find(substring, index)
#         if index == -1:
#             return
#         yield string[:index] + separator + string[index + len(substring):]
#         index += 1

# def contains_all_without_overlap(string, numbers):
#     """
#     contains_all_without_overlap("45892190", [89, 90])
#     # True
#     contains_all_without_overlap("45892190", [89, 90, 4521])
#     # False
#     """
#     if len(numbers) == 0:
#         return True
#     substrings = [str(number) for number in numbers]
#     substring = substrings.pop()
#     return any(contains_all_without_overlap(shorter_string, substrings)
#                for shorter_string in find_each_and_replace_by(string, substring, 'x'))

# tc = 0
# true_counter = 0
# for i in range(data_len):
#     if contains_all_without_overlap(data_list[i],mandatory1):
#         true_counter += 1

# print(true_counter)
