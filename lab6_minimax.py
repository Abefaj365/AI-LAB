# Lab 6: Minimax Algorithm
# Depth = 3, Branching factor = 2
# Leaf values are unique (not the usual 3, 5, 6, 9...):
#   A=4, B=17, C=-3, D=9, E=12, F=-8, G=6, H=15
# Root = MAX, Level 1 = MIN, Level 2 = MAX, Leaves = terminal values

leaves = [4, 17, -3, 9, 12, -8, 6, 15]
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
MAX_DEPTH = 3

def minimax(depth, node_index, is_max):
    if depth == MAX_DEPTH:
        return leaves[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False),
            minimax(depth + 1, node_index * 2 + 1, False)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True),
            minimax(depth + 1, node_index * 2 + 1, True)
        )

print("Leaf values:")
for label, value in zip(labels, leaves):
    print(f"  {label} = {value}")

# Value of left and right sub-tree of the root (for the report)
left_value = min(max(leaves[0], leaves[1]), max(leaves[2], leaves[3]))
right_value = min(max(leaves[4], leaves[5]), max(leaves[6], leaves[7]))
print(f"\nLeft sub-tree value (MIN of MAX(4,17), MAX(-3,9)) = {left_value}")
print(f"Right sub-tree value (MIN of MAX(12,-8), MAX(6,15)) = {right_value}")

optimal = minimax(0, 0, True)
print("\nOptimal Minimax Value at Root:", optimal)
print("Best move for MAXIMIZER: Right sub-tree" if optimal == right_value else "Best move for MAXIMIZER: Left sub-tree")
