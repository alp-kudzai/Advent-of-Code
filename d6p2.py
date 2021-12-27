# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:46:33 2020

@author: User
"""


import re
from collections import Counter

def find_dup_char(input): 
  
    # now create dictionary using counter method 
    # which will have strings as key and their  
    # frequencies as value 
    WC = Counter(input) 
    j = -1
      
      
    # Finding no. of  occurrence of a character 
    # and get the index of it. 
    for i in WC.values(): 
        j = j + 1
        if( i > 1 ): 
            return WC.keys()

in_file = 't6.txt'
file_in = open(in_file, 'r')


d_list = file_in.read().split('\n\n')
print(len(d_list))

file_in.close()

pattern = re.compile(r"\n") # Create the regular expression to match
data_list = [pattern.sub(" ", match ) for match in d_list] # Remove match on each element
data_len = len(data_list)

# print('Data:',data_list)
print('Data length:',data_len)

new_data = []
for line in data_list:
   spaceless = line.replace(' ', '')
   new_data.append(spaceless)

print(new_data)
print(data_list)
yes_list = []
for line in data_list:
    if ' ' in line:
        dup_yes = find_dup_char(line)
    else:
        yes_list.append(line)

        
    

            
    







# yes_list = []
# for line in new_data:
#     container_yes = []
#     for c in line:
#         if c not in container_yes:
#             container_yes.append(c)
#     yes_list.append(container_yes)

# yes_number = []
# for line in yes_list:
#     yes_number.append(len(line))
    
# #print(yes_number)

# total_yes = sum(yes_number)
# print('Total yes:', total_yes)