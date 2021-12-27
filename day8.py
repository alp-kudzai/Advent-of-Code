# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:42:56 2020

@author: User
"""

def break_up(strng):
    '''
    Input: takes in a string of instructions
            it then splits then into name - number
    OutPut: the instruction name , number
    '''
    cont = strng.split(' ')
    name, numb = cont[0], int(cont[1])
    return name, numb



def jump(jump_to, instrctns, tracker, acc_counter, counter):
    nop = 'nop'
    acc = 'acc'
    # jmp = 'jmp'

    for lines in instrctns[int(jump_to):]:
        print(lines)
        brok_inst = break_up(lines)
        if counter > 100:
            return acc_counter
        
        elif brok_inst[0] == nop:
            tracker[counter] = brok_inst
            counter += 1
        elif brok_inst[0] == acc:
            # print('acc add', brok_inst[1])
            acc_counter += int(brok_inst[1])
            tracker[counter] = brok_inst
            counter += 1
        else:
            if brok_inst[1] > 0:
                tracker[counter] = brok_inst
                counter += 1
                jt = counter + int(brok_inst[1] - 1)
                print('JT', jt)
                return jump(jt, instrctns, tracker, acc_counter, counter)
            else:
                tracker[counter] = brok_inst
                counter += 1
                jt = counter + (int(brok_inst[1]) - 1)
                print('JT', jt)
                return jump(jt, instructions, tracker, acc_counter, counter)
in_file = 'day8.txt'
file_in = open(in_file, 'r')
instructions = file_in.read().split('\n')
# print(instructions)

nop = 'nop'
acc = 'acc'
jmp = 'jmp'
tracker = {}

counter = 0
acc_counter = 0
running = True
ind = 0
            
while running:
    if ind in tracker or counter >= 10000:
        running = False
    else:
        brok_inst = break_up(instructions[ind])
        inst, inst_value = brok_inst[0], int(brok_inst[1])
        tracker[ind] = brok_inst
        if inst == nop:
            ind += 1
            counter += 1
        elif inst == acc:
            acc_counter += inst_value
            ind += 1
            counter += 1
            
        elif inst == jmp:
                ind = ind + inst_value
                counter += 1
                
print('Acc:', acc_counter)
    


