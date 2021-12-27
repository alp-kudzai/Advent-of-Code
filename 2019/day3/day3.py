#%%
# import numpy as np
# import matplotlib.pyplot as plt

# with open('input.txt', 'r') as f:
#     lines = f.readlines()
#     data = [x[:-1] for x in lines]
    
    
# def process_data(data):
#     d = [x.split(',') for x in data]
#     return d

# wire1, wire2 = process_data(data)
# # print(wire1)
# # print(wire2)

# def convert_to_xy(wire):
#     final_x, final_y = [], []
#     x, y = 0, 0,
#     for dir in wire:
#         direction = dir[0]
#         distance = int(dir[1:])
#         if dir == wire[0]:
#             if direction == 'R' or direction == 'L':
#                 if direction == 'L':
#                     x = -distance
#                 else:
#                     x = distance
#                 final_x.append(x)
#                 final_y.append(0)
#             elif direction == 'D':
#                 y = -distance
#                 final_x.append(0)
#                 final_y.append(y)
#             else:
#                 y = distance
#                 final_x.append(0)
#                 final_y.append(y)
#         else:
#             if direction == 'R' or direction == 'L':
#                 if direction == 'L':
#                     x = final_x[-1] - distance
#                 else:
#                     x = final_x[-1] + distance
#                 final_x.append(x)
#                 final_y.append(final_y[-1])
#             else:
#                 if direction == 'D':
#                     y = final_y[-1] - distance
#                 else:
#                     y = final_y[-1] + distance
#                 final_x.append(final_x[-1])
#                 final_y.append(y)
#     return final_x, final_y

# w2x, w2y = convert_to_xy(wire2)
# w1x, w1y = convert_to_xy(wire1)

# wire1_set = list(zip(w1x, w1y))
# wire2_set = list(zip(w2x, w2y))
# # print(wire1_set)

# # plt.plot(w2x, w2y, color='r', label='wire2')
# # plt.plot(w1x, w1y, color='b', label='wire1')
# # plt.grid()
# # plt.show()
                
            
# def find_intersections(wire1_set, wire2_set):
#     intersections = []
#     for i in wire1_set:
#         for j in wire2_set:
#             if i[0] == j[0] or i[1] == j[1]:
#                 print('match', i, j)
#                 intersections.append(i)
#     return intersections

# res = set([tuple(sorted(ele)) for ele in wire1_set]) & set([tuple(sorted(ele)) for ele in wire2_set])
# print(res)
# %%
#%%
with open(r'input.txt', 'r') as f:
    raw_input = f.read()

def traverse_wire(wire):
    wire_info = {}
    x, y, count = 0, 0, 0
    directions =  {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    for part in wire:
        for _ in range(int(part[1:])):
            offset = directions[part[0]]
            x += offset[0]
            y += offset[1]
            count += 1
            wire_info[(x, y)] = count
    return wire_info

def solutions(raw_input):
    wires = [x.split(',') for x in raw_input.strip().split('\n')]

    wire_one = traverse_wire(wires[0])
    wire_two = traverse_wire(wires[1])

    crossings = wire_one.keys() & wire_two.keys()

    fewest_steps = min(crossings, key=lambda x: wire_one[x] + wire_two[x])
    steps = wire_one[fewest_steps] + wire_two[fewest_steps]

    closest = min([intersection for intersection in crossings], key=lambda x: abs(x[0]) + abs(x[1]))
    distance = abs(closest[0]) + abs(closest[1])

    return ('day one', distance, 'day two', steps)

print(solutions(raw_input))

# %%
