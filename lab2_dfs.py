# Lab 2: DFS (Initial to Goal)
# Start: Barisal, Goal: Patuakhali
# Unique graph - different start/goal and different shape from Lab 1.
# DFS goes deep first, so it explores dead-ends before finding the goal.

graph = {
    'Barisal': ['Bhola', 'Pirojpur', 'Jhalokati'],
    'Bhola': ['Barisal', 'Lakshmipur'],
    'Pirojpur': ['Barisal', 'Bagerhat'],
    'Jhalokati': ['Barisal', 'Barguna'],
    'Lakshmipur': ['Bhola', 'Noakhali'],
    'Bagerhat': ['Pirojpur', 'Khulna'],
    'Barguna': ['Jhalokati', 'Patuakhali'],
    'Noakhali': ['Lakshmipur', 'Feni'],
    'Khulna': ['Bagerhat', 'Satkhira'],
    'Patuakhali': ['Barguna'],
    'Feni': ['Noakhali'],
    'Satkhira': ['Khulna']
}

def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    parent = {start: None}
    order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        if node == goal:
            break
        # reversed() so the first neighbour is explored first
        for neighbour in reversed(graph[node]):
            if neighbour not in visited and neighbour not in parent:
                parent[neighbour] = node
                stack.append(neighbour)

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path, order

start, goal = 'Barisal', 'Patuakhali'
path, order = dfs(graph, start, goal)

print("DFS Visited Order:", order)
print("Path from", start, "to", goal, ":", " -> ".join(path))
print("Path Length (edges):", len(path) - 1)
