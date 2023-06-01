
graph = {"5" : ["3","7"], "3" : ["2","4","5"],  "7" : ["5","8"], "2" : ["3"] , "4" : ["3","8"], "8": ["7" , "4"] }

visited =[]
queue = []

def bfs(start, find):
    visited.append(start)
    queue.append(start)
    while queue:
        node = queue.pop(0)
        print(node)
        for current in graph[node]:
            if(current not in visited):
                if(current == find) :
                    return current
                visited.append(current)
                queue.append(current)
              

result = bfs("8","2")
print("--------------------------BFS------------------------")
print(result)
print("--------------------------BFS------------------------")

visited = []
def dfs(start, find):
    node = start
    if node not in visited:
        if(node == find) : 
                return node
        visited.append(node)
        # print(node)
        for neighbor in graph[node]:          # To visit all neighbors
            print(neighbor)
            dfs(neighbor,find)

print(dfs("8","2"))



    
