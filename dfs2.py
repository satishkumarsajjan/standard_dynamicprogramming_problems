graph={
    'a':['c','b'],
    'b':['d'],
    'c':['e'],
    'd':[],
    'e':['b','f'],
    'f':[]
}

def dfs(graph,start,visited=[],stack=[]):
    if start not in visited:
        visited.append(start)
        for nodes in graph[start]:
            stack.append(nodes)
        while len(stack)>0:
            dfs(graph,stack.pop(),visited,stack)
    return visited

print(dfs(graph,'a'))