# Lab 5: Number of Generated Nodes (IDS)
# Start: Cumilla, Goal: Brahmanbaria (goal at depth 3)
# Generated node = every node visited in a depth-limited search.
# IDS repeats work, so we count per depth limit AND the total.
# Unique graph - different from Lab 4.

graph = {
    'Cumilla': ['Chandpur', 'Feni', 'Lakshmipur'],
    'Chandpur': ['Cumilla', 'Shahrasti'],
    'Feni': ['Cumilla', 'Daganbhuiyan'],
    'Lakshmipur': ['Cumilla', 'Ramganj'],
    'Shahrasti': ['Chandpur', 'Hajiganj'],
    'Daganbhuiyan': ['Feni', 'Sonagazi'],
    'Ramganj': ['Lakshmipur', 'Brahmanbaria'],
    'Hajiganj': ['Shahrasti'],
    'Sonagazi': ['Daganbhuiyan'],
    'Brahmanbaria': ['Ramganj']
}

def dls_count(node, goal, limit, path, counter):
    counter[0] += 1  # this node is generated
    if node == goal:
        return path
    if limit == 0:
        return None
    for neighbour in graph[node]:
        if neighbour not in path:
            result = dls_count(neighbour, goal, limit - 1, path + [neighbour], counter)
            if result is not None:
                return result
    return None

def ids_count(graph, start, goal, max_depth=5):
    total_generated = 0
    for limit in range(max_depth + 1):
        counter = [0]
        result = dls_count(start, goal, limit, [start], counter)
        total_generated += counter[0]
        print(f"Depth Limit = {limit} : Generated Nodes = {counter[0]}")
        if result is not None:
            print(f"Goal found at depth limit {limit}")
            return result, total_generated
    return None, total_generated

start, goal = 'Cumilla', 'Brahmanbaria'
path, total = ids_count(graph, start, goal)

print("Path from", start, "to", goal, ":", " -> ".join(path))
print("Total Number of Generated Nodes (all iterations):", total)
