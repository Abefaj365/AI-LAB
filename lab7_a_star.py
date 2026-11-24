# Lab 7: A* Search
# Start: Jessore, Goal: Dhaka
# Weighted graph + heuristic h(n) = estimated cost to Dhaka.
# Unique weights and heuristic - different from the usual Romania map.

import heapq

graph = {
    'Jessore': {'Jhenaidah': 45, 'Magura': 38},
    'Jhenaidah': {'Jessore': 45, 'Kushtia': 52},
    'Magura': {'Jessore': 38, 'Faridpur': 61, 'Rajbari': 55},
    'Kushtia': {'Jhenaidah': 52, 'Faridpur': 70},
    'Faridpur': {'Magura': 61, 'Kushtia': 70, 'Rajbari': 28, 'Manikganj': 48},
    'Rajbari': {'Magura': 55, 'Faridpur': 28, 'Manikganj': 35},
    'Manikganj': {'Faridpur': 48, 'Rajbari': 35, 'Dhaka': 42, 'Gazipur': 58},
    'Gazipur': {'Manikganj': 58, 'Dhaka': 32},
    'Dhaka': {'Manikganj': 42, 'Gazipur': 32}
}

heuristic = {
    'Jessore': 170, 'Jhenaidah': 155, 'Magura': 125, 'Kushtia': 140,
    'Faridpur': 85, 'Rajbari': 75, 'Manikganj': 38, 'Gazipur': 28, 'Dhaka': 0
}

def a_star(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start)]  # (f, g, node)
    parent = {start: None}
    g_score = {start: 0}
    visited_order = []

    while open_list:
        f, g, node = heapq.heappop(open_list)
        if node in visited_order:
            continue
        visited_order.append(node)
        if node == goal:
            break
        for neighbour, cost in graph[node].items():
            new_g = g + cost
            if neighbour not in g_score or new_g < g_score[neighbour]:
                g_score[neighbour] = new_g
                parent[neighbour] = node
                heapq.heappush(open_list, (new_g + heuristic[neighbour], new_g, neighbour))

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path, g_score[goal], visited_order

start, goal = 'Jessore', 'Dhaka'
path, cost, order = a_star(graph, heuristic, start, goal)

print("A* Visited Order:", order)
print("Path from", start, "to", goal, ":", " -> ".join(path))
print("Total Path Cost (g):", cost)
print("Heuristic values:", heuristic)
