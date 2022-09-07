# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:29:56 2020

@author: User
"""
import re

def find_bags(colr_bags, bag_rules):
    '''
    
    '''
    collector = []
    collector2 = []
    
    for i in range(len(colr_bags)):
        for lines in bag_rules:
            z = re.search(('.') + str(colr_bags[i]), lines)
            if z:
                collector.append(z.string)
    collector = list(dict.fromkeys(collector)) 
           
    if collector != collector2 :
        colr_lines = find_1st2(collector)
        for i in range(len(colr_lines)):
            for lines in bag_rules:
                z = re.search(('.') + str(colr_lines[i]), lines)
                if z:
                    collector2.append(z.string)
    collector2 = list(dict.fromkeys(collector2))
        
    return collector

def find_1st2(bag_list):
    '''
    Finds the first two word in a string(colours of bags)
    and Returns a list of colours
    '''
    collector = []
    for lines in bag_list:
        z = re.search(r'^((?:\S+\s){2})', lines)
        collector.append(z.group())
    return collector

def fcolor_bag(colour ,rules):
    '''
    Finds the bags that can fit at least one bag of given colurs
    '''
    
    collector = []
    for lines in rules:
        z = re.search((('.')+str(colour)), lines)
        if z:
            collector.append(z.string)
    
    return collector
        
in_file = 't7.txt'
file_in = open(in_file, 'r')

rules = file_in.read().split('\n')
len_rules = len(rules)
# print(rules)
# print(len_rules)



running = True
ind = 0
bag_coll = []

while running:
    if ind > 1:
        bagsC = fcolor_bag('shiny gold', rules)
        ind += 1
    else:
        #cut the first two colours
        colr1 = find_1st2(bagsC)
        found_bags = find_bags(colr1, rules)
        if len(found_bags) == 0:
            running = False
        else:
            bag_coll.append(found_bags)
            colr2 = find_1st2(found_bags)
            found_bags2 = find_bags(colr2, rules)
            if len(found_bags2) == 0:
                running = False
            else:
                bagsC = fcolor_bag(colr2, rules)

# for lines in rules:
#     a = re.search(r'\d shiny gold', lines)
#     if a:
#         shiny1.append(a.string)
# # print(shiny1)

# shiny2 = []
# for lines in shiny1:
#     b = re.search(r'^((?:\S+\s){2})', lines)
#     shiny2.append(b.group())
    
# shiny3 = []
# for i in range(len(shiny2)):
#     for lines in rules:
#         c = re.search(str(shiny2[i]), lines)
#         if c:
#             shiny3.append(c.string)
            

            
# final_shiny = list(dict.fromkeys(shiny3))

# print(len(final_shiny))