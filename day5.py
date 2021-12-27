# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:06:26 2020

@author: User
"""
import math 

in_file = 'day5.txt'
file_in = open(in_file, 'r')

datalist = file_in.read().split('\n')
file_in.close()



data_len = len(datalist)

def seating_position(data_str):
    upper_row, lower_row = 128, 1
    upper_column, lower_column = 7, 1
    
    b = 'B'
    f = 'F'
    r = 'R'
    l = 'L'
    final_data = []
    for c in data_str:
        if c == b and (lower_row + 1) != upper_row:
            mid = math.floor(((upper_row + lower_row)/2))
            lower_row = mid
        elif c == f and (lower_row + 1) != upper_row:
            mid = math.floor(((upper_row + lower_row)/2))
            upper_row = mid
        else:
            if c == b:
                final_row = max(lower_row, upper_row)
                
            else:
                final_row = min(lower_row, upper_row)
                
                
    
        if c == r and (lower_column + 1) != upper_column:
            mid = math.floor(((upper_column + lower_column)/2))
            lower_column = mid
        elif c == l and (lower_column + 1) != upper_column:
            mid = math.floor(((upper_column + lower_column)/2))
            upper_column = mid
        else: 
            if c == l:
                final_column = min(upper_column, lower_column)
                
            else:
                final_column = max(upper_column, lower_column)
            

    final_data.append(final_row)
    final_data.append(final_column)
    return final_data
#create list of the seating positions of individuals
rc_data = []   
for ind in datalist:
    rc_data.append(seating_position(ind))


def seating_id(rc_dt):
    row, col = (rc_dt[0]), (rc_dt[1])
    st_id = ((row * 8) + col)
    return st_id

seat_ID = []
for ind in rc_data:
    seat_ID.append(seating_id(ind))

print(max(seat_ID))
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for c in data_str:
    #     if c == b and (lower_row + 1) != upper_row:
    #         mid = ((upper_row + lower_row)//2)
    #         lower_row = mid
    #     elif c == f and (lower_row + 1) != upper_row:
    #         mid = ((upper_row + lower_row)//2)
    #         upper_row = mid
    #     elif (c == b or c == f) and (lower_row+1) == upper_row:
    #         if c == b:
    #             final_row = max(lower_row, upper_row)
    #             print(final_row)
    #             final_data.extend(final_row)
    #         else:
    #             final_row = min(lower_row, upper_row)
    #             print(final_row)
    #             final_data.extend(final_row)
        
    #     elif c == r and (lower_column + 1) != upper_column:
    #         mid = (upper_column + lower_column)//2
    #         lower_column = mid
    #     elif c == l and (lower_column + 1) != upper_column:
    #         mid = (upper_column + lower_column)//2
    #         upper_column = mid
    #     elif (c == l or c == r) and lower_column + 1 == upper_column:
    #         if c == l:
    #             final_column = min(upper_column, lower_column)
    #             final_data.extend(final_column)
    #         else:
    #             final_column = max(upper_column, lower_column)
    #             final_data.extend(final_column)
    # print(c)
    # if len(final_data) == 2:
    #     return final_data        
      
            
            