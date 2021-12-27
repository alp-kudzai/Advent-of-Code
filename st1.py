# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:59:45 2020

@author: User
"""
from functools import lru_cache

file_in = open('mass.txt', 'r')
mod_mass = file_in.read().splitlines()
num_mod = len(mod_mass)

print(f'The number of modules is: {num_mod}')

freq_c = []

for n in range(num_mod):
    freq_c += [(int((int(mod_mass[n]))/3)-2)]
    
#print(f'individual fuel requirements of modules: {freq_c}')

total_fuel = 0
for n in freq_c:
    total_fuel += n

print(f'The total fuel required: {total_fuel}')
@lru_cache(maxsize=5000000)

def total_Rfuel(weight):
    fuel_req = max((weight // 3) - 2, 0)
    if fuel_req == 0: return 0
    return fuel_req + total_Rfuel(fuel_req)

# def total_Rfuel(tl_fuel):
#     '''
#     Input: total fuel computed for the modules
#     Output: The total fuel including the fuel for
#             the fuel.
#     '''
    
#     fuel = 0
#     while int(tl_fuel/3-2) > 0:
#         tl_fuel = int(tl_fuel/3-2)
#         fuel += tl_fuel
#     return fuel
    # tc = 3452245
    # if tl_fuel <= 8:
    #     pass
    # else:
    #     tl_fuel = (int(tl_fuel/3) - 2)
    #     tc += tl_fuel
    #     if tl_fuel <= 8:
    #         pass
    #     else:
    #         tc += tl_fuel
    #         tl_fuel = total_Rfuel(tl_fuel)
        
    #     return tc
    
    # n2_store = 0
    # total_store = 0
    # running = True
    # n1 = (int(tl_fuel/3) - 2)
    
    # while running:
    #     if (n2_store > 0) and (n2_store <= 8):
    #         running = False
    #     if (n1 < 6):
    #         running = False
    #     n2_store = (int(n1/3) - 2)
    #     total_store += (n1+n2_store)
    #     n1 = (int(n2_store/3) - 2)
        
        
    # return total_store
    

print(f'Total fuels fuel is {total_Rfuel(total_fuel)+total_fuel}')
print('Done.')
