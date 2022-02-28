from collections import deque
graph={
    'a':['c','d'],
    'b':['d'],
    'c':['e'],
    'd':[],
    'e':['b'],
    'f':[]
}
def dfs(graph,start,visited=[],queue=deque()):
    if start not in visited:
        visited.append(start)
        for nodes in graph[start]:
            queue.append(nodes)
        while len(queue)>0:
            dfs(graph,queue.popleft(),visited,queue)
    return visited

print(dfs(graph,'a'))