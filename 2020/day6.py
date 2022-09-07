# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 08:26:49 2020

@author: User
"""

import re

in_file = 't6.txt'
file_in = open(in_file, 'r')


d_list = file_in.read().split('\n\n')
print((d_list))

file_in.close()

pattern = re.compile(r"\n") # Create the regular expression to match
data_list = [pattern.sub(" ", match ) for match in d_list] # Remove match on each element
data_len = len(data_list)

# print('Data:',data_list)
print('Data length:',data_len)
print(data_list)

new_data = []
for line in data_list:
   spaceless = line.replace(' ', '')
   new_data.append(spaceless)

# print(new_data)
yes_list = []
for line in new_data:
    container_yes = []
    for c in line:
        if c not in container_yes:
            container_yes.append(c)
    yes_list.append(container_yes)

yes_number = []
for line in yes_list:
    yes_number.append(len(line))
    
print(yes_number)

total_yes = sum(yes_number)
print('Total yes:', total_yes)