#%%
from collections import defaultdict
  
# This class represents a directed graph
# using adjacency list representation
class Graph:
  
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
         
        # default dictionary to store graph
        self.graph = defaultdict(list)
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for k,v in self.graph.items():
            print(f'Edge : {k} --> {v}')
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, path, all_p):
 
        # Mark the current node as visited and store in path
        #visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            #print(path)
            all_p.append(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                #if visited[i]== False:
                if i.islower() and (i not in path):
                    self.printAllPathsUtil(i, d, path, all_p)
                elif i.isupper():
                    self.printAllPathsUtil(i, d, path, all_p)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        #visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d, all_p=[]):
 
        # Mark all the vertices as not visited
        #nodes = [n for n in self.graph.keys()]
        #falses = [False]*len(nodes)
        #visited = {n:f for (n,f) in zip(nodes,falses)}
 
        # Create an array to store paths
        path = []
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, path,all_p)
        return all_p
  
  
  
# Create a graph given in the above diagram
with open('input.txt') as f:
    data = f.read().split('\n')

Nodes = []
for d in data:
    n1, n2 = d.split('-')
    if n1 not in Nodes:
        Nodes.append(n1)
    if n2 not in Nodes:
        Nodes.append(n2)
# print(f'{Nodes}\n')
# print(f'{data}\n')
g = Graph(len(Nodes))
for d in data:
    n1,n2 = d.split('-')
    g.addEdge(n1, n2)
#g.print_graph()
#print('\n')
all_paths = g.printAllPaths('start', 'end')
print(f'\nNumber of Possible Paths: {len(all_paths)}')


#%%