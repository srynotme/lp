


#dfs 

g={'1':['2','5'],'2':['3','4'],'5':['6'],'6':[],'4':[],'3':['7'],'7':[]}

visited=[]

def dfs(visited,g,node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in g [node]:
            dfs(visited,g,neighbour)

    
print("DFS Table")
dfs(visited,g,'1')

######BFS #######

graph={'1':['2','5'],'2':['3','4'],'5':['6'],'6':[],'4':[],'3':['7'],'7':[]}


visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end="")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("BFS\n")
bfs(visited,graph,"1")




    