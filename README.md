# AI Lab

AI course labs in Python: BFS, DFS, IDS, number of generated nodes, Minimax, A* search and Greedy Best First Search.

Each lab uses a different graph, so the answers are not the same.

## Labs

| Lab | File | Start → Goal | Result |
| --- | --- | --- | --- |
| 1. BFS (initial to goal) | `lab1_bfs.py` | Pabna → Dhaka | Path: Pabna → Sirajganj → Tangail → Gazipur → Dhaka (4 edges) |
| 2. DFS (initial to goal) | `lab2_dfs.py` | Barisal → Patuakhali | Path: Barisal → Jhalokati → Barguna → Patuakhali (3 edges) |
| 3. IDS (initial to goal) | `lab3_ids.py` | Sylhet → Sreemangal | Found at depth limit 3 |
| 4. Number of generated nodes (BFS) | `lab4_bfs_generated_nodes.py` | Dinajpur → Thakurgaon | Generated: 9, Expanded: 8 |
| 5. Number of generated nodes (IDS) | `lab5_ids_generated_nodes.py` | Cumilla → Brahmanbaria | Per depth: 1, 4, 7, 10 — Total: 22 |
| 6. Minimax Algorithm | `lab6_minimax.py` | — | Leaf values: 4, 17, -3, 9, 12, -8, 6, 15 — Optimal value: 12 |
| 7. A* search | `lab7_a_star.py` | Jessore → Dhaka | Path: Jessore → Magura → Rajbari → Manikganj → Dhaka — Cost: 170 |
| 8. Greedy Best First Search | `lab8_greedy_best_first.py` | Rangamati → CoxBazar | Path: Rangamati → Bandarban → Chattogram → CoxBazar (3 edges; shortest is 2) |

## How to run

```bash
python3 lab1_bfs.py
python3 lab2_dfs.py
python3 lab3_ids.py
python3 lab4_bfs_generated_nodes.py
python3 lab5_ids_generated_nodes.py
python3 lab6_minimax.py
python3 lab7_a_star.py
python3 lab8_greedy_best_first.py
```
