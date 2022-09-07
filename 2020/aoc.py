# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:18:57 2020

@author: User
"""
file_in = open('aoc_input.txt', 'r')

content = file_in.read().splitlines()
leng = len(content)
print(f'lenght {leng}.')

running = True
sum_nums = []
fc = 0

while running:
    for n1 in range(leng):
        for n2 in range(leng):
            for n3 in range(leng):
                
                if (int(content[n1]) + int(content[n2]) + int(content[n3])) == 2020:
                    sum_nums += (content[n1], content[n2], content[n3] )
                    print(True)
                else:
                    fc += 1
    running = False
    
print(sum_nums)
print(fc)