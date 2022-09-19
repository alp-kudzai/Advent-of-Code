#%%
with open('input.txt') as f:
    data = f.read().split('\n')

#print(data)

def lower_point(curr, other):
    '''
    Determines if the current point is lower than other point
    '''
    if curr < other: return True
    return False

width = len(data[0])
width_range = [i for i in range(0, width)]
height = len(data)
height_range = [i for i in range(0,height)]
low_list = []
for h in range(0,height):
    current_line = data[h]
    for w in range(0, width):
        
        current_depth = int(current_line[w])
        if h == 0: #top
            if w == 0: #top left
                # check left & down
                right = int(current_line[w+1])
                down = int(data[h+1][w])
                if lower_point(current_depth, right) and lower_point(current_depth,down):
                    low_list.append(current_depth)
                    
            if w == width-1: #top right
                left = int(current_line[w-1])
                down = int(data[h+1][w])
                if lower_point(current_depth, left) and lower_point(current_depth,down):
                    low_list.append(current_depth)
    
            else: # edge
                left = int(current_line[w-1])
                right = int(current_line[w+1])
                down = int(data[h+1][w])
                if lower_point(current_depth, left) and lower_point(current_depth, right) and lower_point(current_depth,down):
                    low_list.append(current_depth)
        elif h == height-1: #bottom
            if w == 0: #bottom left
                right = int(current_line[w+1])
                up = int(data[h-1][w])
                if lower_point(current_depth, right) and lower_point(current_depth,up):
                    low_list.append(current_depth)
                
            if w == width-1: # bottom right
                left = int(current_line[w-1])
                up = int(data[h-1][w])
                if lower_point(current_depth, left) and lower_point(current_depth,up):
                    low_list.append(current_depth)

            else: # edge
                left = int(current_line[w-1])
                right = int(current_line[w+1])
                up = int(data[h-1][w])
                if lower_point(current_depth, left) and lower_point(current_depth, right) and lower_point(current_depth,up):
                    low_list.append(current_depth)
                
        elif w == 0: # left edge
            up = int(data[h-1][w])
            right = int(current_line[w+1])
            down = int(data[h+1][w])
            if lower_point(current_depth,up) and lower_point(current_depth,right) and lower_point(current_depth,down):
                low_list.append(current_depth)
            
        elif w == width-1: # right edge
            up = int(data[h-1][w])
            left = int(current_line[w-1])
            down = int(data[h+1][w])
            if lower_point(current_depth,up) and lower_point(current_depth,left) and lower_point(current_depth,down):
                low_list.append(current_depth)
        
        else:
            # everything else
            up = int(data[h-1][w])
            left = int(current_line[w-1])
            right = int(current_line[w+1])
            down = int(data[h+1][w])
            if lower_point(current_depth,up) and lower_point(current_depth,left) and lower_point(current_depth,right) and lower_point(current_depth,down):
                low_list.append(current_depth)

#print(low_list)

risk_level = list(map(lambda x: x+1, low_list))
print('The risk level is:')
print(sum(risk_level))
#%%