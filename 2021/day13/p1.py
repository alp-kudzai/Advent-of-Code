#%%
from collections import defaultdict
import re

with open('input.txt') as f:
    data = f.read().split('\n')
coord = defaultdict(list)
y_coord = defaultdict(list)
other = False
patt = r'[x|y]=[\d]*'
fold = []
max_x, max_y = 0,0
for d in data:
    if d != '' and other == False:
        x, y = d.split(',')
        x,y = int(x), int(y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        coord[x].append(y)
        y_coord[y].append(x)
        y_coord[y].sort()
        coord[x].sort()
    elif d == '':
        other = True
    elif other:
        res = re.findall(patt,d)
        fold.append(res[0])

#print(coord)
print(fold)
# x_coord = dict(sorted(coord.items()))
# y_coord = dict(sorted(y_coord.items()))
def sort_dict(dic:defaultdict):
    sorted_keys = sorted(dic)
    new_dic = defaultdict(list)
    for k in sorted_keys:
        new_dic[k] = dic[k]
    return new_dic

x_coord = sort_dict(coord)
y_coord = sort_dict(y_coord)


# print(x_coord)
# print(f'\n{y_coord}\n')
#print(f'max x: {max_x}\nmax y: {max_y}')
def get_max():
    global y_coord
    global x_coord
    #print(f'{x_coord}\n{y_coord}\n')
    x_list = sorted(x_coord)
    y_list = sorted(y_coord)
    #print(f'{x_list}\n{y_list}')
    max_x,max_y = x_list[-1], y_list[-1]
    return max_x,max_y

def get_range(n,axis):
    global y_coord
    global x_coord
    mx,my = get_max()
    if axis == 'y':
        to_fold = [i for i in range(n+1,my+1)]
    else:
        to_fold = [i for i in range(n+1, mx+1)]
    return to_fold

def make_opposite(dic:defaultdict):
    new_dic = defaultdict(list)
    for k,v in dic.items():
        for coord in v:
            new_dic[coord].append(k)
    new_dic = sort_dict(new_dic)
    return new_dic

def fold_y(y):
    global y_coord
    global x_coord
    # range to fold along the y axis
    to_fold = get_range(y,'y')
    to_fold = to_fold[::-1]
    # delete the line we will fold on if it as dots
    if y in y_coord: del y_coord[y]
    for i in range(len(to_fold)):
        #get x coord from y_coord
        if to_fold[i] in y_coord:
            x_list_y = y_coord[to_fold[i]]
            #print(i)
            for x in x_list_y:
                y_coord[i].append(x)
                y_coord[i].sort()
                # remove overlaps
                y_coord[i] = [*set(y_coord[i])]
            #delete the old y key from dict
            del y_coord[to_fold[i]]
    y_coord = sort_dict(y_coord)
    x_coord = make_opposite(y_coord)
    
            
def fold_x(x):
    global y_coord
    global x_coord
    to_fold = get_range(x,'')
    to_fold = to_fold[::-1]
    # delete the line we will fold if it exists
    if x in x_coord: del x_coord[x]
    for i in range(len(to_fold)):
        if to_fold[i] in x_coord:
            y_list_x = x_coord[to_fold[i]]
            for y in y_list_x:
                x_coord[i].append(y)
                x_coord[i].sort()
                x_coord[i] = [*set(x_coord[i])]
            del x_coord[to_fold[i]]
    x_coord = sort_dict(x_coord)
    y_coord = make_opposite(x_coord)


def count_dots(dic:defaultdict):
    total = 0
    for k,v in dic.items():
        total += len(v)
    return total

def do_folds():
    global y_coord
    global x_coord
    #counter = 0
    for f in fold:
        axis, n = f.split('=')
        n = int(n)
        #print(n)
        if axis == 'x':
            fold_x(n)
            #counter += 1
        elif axis == 'y':
            fold_y(n)
            #counter += 1
        #if counter == num:
    dots_x = count_dots(x_coord)
    dots_y = count_dots(y_coord)
    if dots_x != dots_y:
        print('Something is very wrong. The dots do not match!!!!')
        print(f'X: {dots_x}\nY: {dots_y}')
        raise ValueError
    print(f'Total Dots: {dots_x}\n')
            #print(f'X\n{x_coord}')
            #print(f'\nY\n{y_coord}')
            






def draw(file):
    global y_coord
    global x_coord
    do_folds()
    dot = '#'
    ntg = ' '
    #print(fold)
    with open(file,'a') as f:
        mx,my = get_max()
        #print(my)
        #print(mx)
        for y in range(my+1):
            for x in range(mx+1):
                if (y in y_coord) and (x in y_coord[y]):
                    mark = dot
                else:
                    mark = ntg
                f.write(mark)
            f.write('\n')
    
draw('results.txt')



#print(data)
#%%