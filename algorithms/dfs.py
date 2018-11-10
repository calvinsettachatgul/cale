graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set('B'),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
'''
   A
  /  \
 C    B
        / \
       D   E
            /   
           F
 '''
         
'''
   A
  /  \
 C    B
 |   / \
 |  D   E
 |     /   
 |-----F
 visited=set(A,B,E,F,C,D)
walkthrough:
visited=set(A,)
stack=[B,C]
cycle1: vertex=A
------------------
visited=set(A,B)
stack=[C,D,E]
cycle2: vertex=B
------------------
visited=set(A,B,E)
stack=[C,D,F]
cycle3: vertex=E
------------------
visited=set(A,B,E,F)
stack=[C,D,C]
cycle4: vertex=F
------------------
visited=set(A,B,E,F,C)
stack=[C,D]
cycle5: vertex=C
------------------
visited=set(A,B,E,F,C,D)
stack=[C]
cycle6: vertex=D
------------------
visited=set(A,B,E,F,C,D)
stack=[]
cycle7: vertex=C

'''
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set('B'),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
         
'''



# depth first search

def dfs(graph,start):
    visited,stack=set(),[start]
    visited_ls=[]
    while stack:
        vertex=stack.pop() #A
        if vertex not in visited: # A is not in visited
            visited.add(vertex) # visted.add(A)
            visited_ls.append(vertex)
            stack.extend(graph[vertex]-visited) # stack.extend([B, C] - set(A))
    print(visited_ls)
    return visited

print(dfs(graph,'A'))
'''