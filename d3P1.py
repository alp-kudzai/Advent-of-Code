# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:08:06 2020

@author: User
"""
output_file = 't.txt'
file_in = open('day3.txt', 'r')
out = open(output_file, 'w')
slope = file_in
    
for line in slope:
    full_slope = ''
    n_line = (line.strip('\n'))
    full_slope += n_line*100
    full_slope += '\n'
    str_slope = str(full_slope)
    out.write(str_slope)
    
out.close()
    
new_land = open(output_file, 'r')
def tree_no(file_in, right, down):
    '''
    Inputs: takes; the file with land, the rightward move and the
    downward move.
    Outputs: the number of trees
    '''
    new_land = file_in
    move_down = down
    last_move = right
    move_right = right
    tree_tracker = 0
    tree = '#'
    if move_down == 1:
        next(new_land)
        for line in new_land:
            if line[last_move] == tree:
                tree_tracker += 1
                last_move += move_right
            else:
                last_move += move_right
    else:
        line_co = 0
        #line_tr = 0
        next(new_land)
        for line in new_land:
            line_co += 1
            if line_co%2 == 0:
                if line[last_move] == tree:
                    tree_tracker += 1
                    last_move += move_right
                else:
                    last_move += move_right
    return tree_tracker

#tree1 = tree_no(new_land, 3, 1)
#print(tree1)
# tree2 = tree_no(new_land, 1, 1)
# print(tree2)
# tree3 = tree_no(new_land, 5, 1)
# print(tree3)
# tree4 = tree_no(new_land, 7, 1)
# print(tree4)
# tree5 = tree_no(new_land, 1, 2)
# print(tree5)

# new_land.close()
        
