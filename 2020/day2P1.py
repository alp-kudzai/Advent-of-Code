# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:44:10 2020

@author: User
"""
#['1-30 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
file_in = open('day_two.txt', 'r')
contents = file_in.read().splitlines()
num_psswd = len(contents)
#print(contents)


#def valid_psswrds(file_contents):
    # '''
    # Input: the file contexts that have been striped
    #         of the "\n"
    # Output: the number of valid passwords
    # '''
#contents = file_contents

count = 0
inst_count = 0
for strng in contents: 
    split_str = strng.split()
    numbs = split_str[0].split('-')
    letter = split_str[1].strip(':')
    psswrd = split_str[2].strip()
    i1, i2 = (int(numbs[1])-1), (int(numbs[0])-1)
    b1 = (letter == psswrd[i1]) #(letter == psswrd[i1] and letter != psswrd[i2])
    b2 = (letter == psswrd[i2]) #(letter == psswrd[i2] and letter != psswrd[i1])
    
    if (b2 != b1) or (b1 != b2) :
        count += 1
    else:
        inst_count += 1
    # for c in psswrd:
    #     if c == letter:
    #         inst_count += 1
    # if inst_count >= low and inst_count <= high:
    #     count += 1
    # count 

print(count)
# print(f'The number of valid passwords: {valid_psswrds(contents)}')
# print(f'Out of a total of: {num_psswd}')