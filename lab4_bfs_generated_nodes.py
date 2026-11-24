# Lab 4: Number of Generated Nodes (BFS)
# Start: Dinajpur, Goal: Thakurgaon
# Generated node = every node put into the queue (including the start node).
# Unique graph - different from Lab 1, 2 and 3.

from collections import deque

graph = {
    'Dinajpur': ['Rangpur', 'Nilphamari', 'Panchagarh'],
    'Rangpur': ['Dinajpur', 'Kurigram', 'Gaibandha'],
    'Nilphamari': ['Dinajpur', 'Lalmonirhat'],
    'Panchagarh': ['Dinajpur', 'Thakurgaon'],
    'Kurigram': ['Rangpur'],
    'Gaibandha': ['Rangpur', 'Bogra'],
    'Lalmonirhat': ['Nilphamari'],
    'Thakurgaon': ['Panchagarh'],
    'Bogra': ['Gaibandha']
}

def bfs_count(graph, start, goal):
    visited = {start}
    queue = deque([start])
    parent = {start: None}
    generated = [start]          # nodes generated, in order
    expanded = []                # nodes removed from queue

    while queue:
        node = queue.popleft()
        expanded.append(node)
        if node == goal:
            break
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)
                generated.append(neighbour)

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path, generated, expanded

start, goal = 'Dinajpur', 'Thakurgaon'
path, generated, expanded = bfs_count(graph, start, goal)

print("Path from", start, "to", goal, ":", " -> ".join(path))
print("Generated Nodes (in order):", generated)
print("Number of Generated Nodes:", len(generated))
print("Number of Expanded Nodes:", len(expanded))
print("Expanded Nodes:", expanded)
