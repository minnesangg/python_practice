graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]  
    if start == end:
        return [path]  
    if start not in graph:
        return []  
    paths = []
    for node in graph[start]:
        if node not in path: 
            new_paths = find_all_paths(graph, node, end, path)  
            for p in new_paths:
                paths.append(p)  
    return paths

# example:
start_node = 'A'
end_node = 'F'
all_paths = find_all_paths(graph, start_node, end_node)

print(f"All paths from {start_node} to {end_node}:")
for path in all_paths:
    print(" -> ".join(path))
