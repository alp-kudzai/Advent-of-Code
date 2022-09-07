# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:44:57 2020

@author: User
"""

import re

in_file = 'day4.txt'
file_in = open(in_file, 'r')


d_list = file_in.read().split('\n\n')
print(len(d_list))

file_in.close()
#data_list = []
pattern = re.compile(r"\n") # Create the regular expression to match
data_list = [pattern.sub(" ", match ) for match in d_list] # Remove match on each element
data_len = len(data_list)
    
# print(data_list)
# by = 'byr:\d{4}'
# iy = 'iyr'
# ey = 'eyr'
# ht = 'hgt'
# hc = 'hcl'
# ec = 'ecl'
# pd = 'pid'
# cd = 'cid'


#mandatory1 = [by, iy, ey, ht, hc, ec, pd]
total_valid = 0
valid = 0
for ind in range(data_len):
    valid = 0
    a = re.search(r'byr:\d{4}', data_list[ind])
    if a:
        lst = a.group()
        sliced_lst = lst[4:8]
        if int(sliced_lst) >= 1920 and int(sliced_lst) <= 2002:
            valid += 1
            # valida = 1
    b = re.search(r'iyr:\d{4}', data_list[ind])
    if b:
        lst = b.group()
        sliced_lst = lst[4:8]
        if int(sliced_lst) >= 2010 and int(sliced_lst) <= 2020:
            valid += 1
            # validb = 1
            
    c = re.search(r'eyr:\d{4}', data_list[ind])
    if c:
        lst = c.group()
        sliced_lst = lst[4:8]
        if int(sliced_lst) >= 2010 and int(sliced_lst) <= 2030:
            valid += 1
            # validc = 1
            
    d = re.search(r'hgt:\d{3}cm|hgt:\d{2}in', data_list[ind])
    if d:
        lst = d.group()
        lst_len = len(lst)
        if re.search(r'hgt:[0-9]{3}cm',lst):
            sliced_lst = lst[4:7]
            if int(sliced_lst) >= 150 and int(sliced_lst) <= 193:
                valid += 1
                # validD1 = 1
        elif re.search(r'hgt:[0-9]{2}in',lst):
            sliced_lst = lst[4:6]
            if int(sliced_lst) >= 59 and int(sliced_lst) <= 76:
                valid += 1
                # validd2 = 1
    # [A-Za-z0-9]+
    # [0-9a-f]{6}|hcl:#(\d|[a-f]){6}
    e = re.search(r'hcl:#[A-Za-z0-9]+', data_list[ind])
    if e:
        # sliced_e = e[5:11]
        # for c in sliced_e:
            
        valid += 1
        # valide = 1
        
    f = re.search(r'ecl:amb|blu|brn|gry|grn|hzl|oth', data_list[ind])
    if f:
        valid += 1
        # validf = 1
    # [0-9]+ 
    # [0-9]{9}
    g = re.search(r'pid:\d{9}\b', data_list[ind])
    if g:
        sliced_g = g.group()[4:13]
        if len(sliced_g) == 9:
            valid += 1
        # validg = 1
        
        
    
    if valid == 7:
        total_valid += 1
        
   
        
print(total_valid)
        