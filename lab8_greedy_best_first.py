# Lab 8: Greedy Best First Search
# Start: Rangamati, Goal: CoxBazar
# Greedy uses ONLY the heuristic h(n), it ignores the path cost g(n).
# So it can pick a longer path - here it goes via Bandarban (h=47)
# instead of the shorter Rangamati -> Chattogram -> CoxBazar route.
# Unique graph and heuristic - different from Lab 7 (A*).

import heapq

graph = {
    'Rangamati': ['Khagrachari', 'Chattogram', 'Bandarban'],
    'Khagrachari': ['Rangamati', 'Chattogram'],
    'Chattogram': ['Rangamati', 'Khagrachari', 'Bandarban', 'CoxBazar'],
    'Bandarban': ['Rangamati', 'Chattogram'],
    'CoxBazar': ['Chattogram']
}

# h(n) = estimated distance to CoxBazar
heuristic = {
    'Rangamati': 118,
    'Khagrachari': 139,
    'Chattogram': 71,
    'Bandarban': 47,
    'CoxBazar': 0
}

def greedy_best_first(graph, heuristic, start, goal):
    # heap entry: (h, node, parent_node) - parent is set when the node
    # is actually expanded, not when it is first discovered. That way
    # the path follows the order greedy really visited the nodes.
    open_list = [(heuristic[start], start, None)]  # (h, node, parent) - no g(n)
    parent = {}
    visited = set()
    order = []

    while open_list:
        h, node, from_node = heapq.heappop(open_list)
        if node in visited:
            continue
        visited.add(node)
        parent[node] = from_node
        order.append(node)
        if node == goal:
            break
        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(open_list, (heuristic[neighbour], neighbour, node))

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path, order

start, goal = 'Rangamati', 'CoxBazar'
path, order = greedy_best_first(graph, heuristic, start, goal)

print("Greedy Visited Order:", order)
print("Path from", start, "to", goal, ":", " -> ".join(path))
print("Path Length (edges):", len(path) - 1)
print("Note: Greedy is NOT optimal here. Shortest path would be")
print("Rangamati -> Chattogram -> CoxBazar (2 edges), but greedy")
print("first picks Bandarban because its h (47) is lowest.")
