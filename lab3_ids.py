# Lab 3: IDS (Iterative Deepening Search - Initial to Goal)
# Start: Sylhet, Goal: Sreemangal (goal at depth 3)
# Unique graph - different from Lab 1 and Lab 2.

graph = {
    'Sylhet': ['Habiganj', 'Moulvibazar', 'Sunamganj'],
    'Habiganj': ['Sylhet', 'Baniachong'],
    'Moulvibazar': ['Sylhet', 'Kamalganj', 'Rajnagar'],
    'Sunamganj': ['Sylhet', 'Jagannathpur'],
    'Baniachong': ['Habiganj', 'Nabiganj'],
    'Kamalganj': ['Moulvibazar', 'Sreemangal'],
    'Rajnagar': ['Moulvibazar'],
    'Jagannathpur': ['Sunamganj'],
    'Nabiganj': ['Baniachong'],
    'Sreemangal': ['Kamalganj']
}

def dls(node, goal, limit, path):
    if node == goal:
        return path
    if limit == 0:
        return None
    for neighbour in graph[node]:
        if neighbour not in path:
            result = dls(neighbour, goal, limit - 1, path + [neighbour])
            if result is not None:
                return result
    return None

def ids(graph, start, goal, max_depth=5):
    for limit in range(max_depth + 1):
        print(f"Depth Limit = {limit} : searching...")
        result = dls(start, goal, limit, [start])
        if result is not None:
            print(f"Goal found at depth limit {limit}")
            return result
    return None

start, goal = 'Sylhet', 'Sreemangal'
path = ids(graph, start, goal)

print("Path from", start, "to", goal, ":", " -> ".join(path))
print("Path Length (edges):", len(path) - 1)
