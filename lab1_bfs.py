# Lab 1: BFS (Initial to Goal)
# Start: Pabna, Goal: Dhaka
# Unique graph - Bangladesh districts, not the usual A-B-C graph

from collections import deque

graph = {
    'Pabna': ['Rajshahi', 'Kushtia', 'Sirajganj'],
    'Rajshahi': ['Pabna', 'Natore', 'Chapainawabganj'],
    'Kushtia': ['Pabna', 'Meherpur', 'Jhenaidah'],
    'Sirajganj': ['Pabna', 'Tangail'],
    'Natore': ['Rajshahi', 'Bogra'],
    'Chapainawabganj': ['Rajshahi'],
    'Meherpur': ['Kushtia'],
    'Jhenaidah': ['Kushtia', 'Jessore'],
    'Tangail': ['Sirajganj', 'Gazipur'],
    'Bogra': ['Natore', 'Joypurhat'],
    'Jessore': ['Jhenaidah', 'Khulna'],
    'Gazipur': ['Tangail', 'Dhaka'],
    'Joypurhat': ['Bogra'],
    'Khulna': ['Jessore'],
    'Dhaka': ['Gazipur']
}

def bfs(graph, start, goal):
    visited = {start}
    queue = deque([start])
    parent = {start: None}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        if node == goal:
            break
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)

    # Reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path, order

start, goal = 'Pabna', 'Dhaka'
path, order = bfs(graph, start, goal)

print("BFS Visited Order:", order)
print("Path from", start, "to", goal, ":", " -> ".join(path))
print("Path Length (edges):", len(path) - 1)
