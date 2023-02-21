"""
1. Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
2. Repeat until all the nodes are visited, or the node to be searched is found.

"""

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


visited = set()

def dfs(visited, graph,node):
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph,neighbor)
        
dfs(visited, graph,'B')