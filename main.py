from theorygraph import Graf

# =================================================
# IMPLEMENTASI DASAR (SESUSAI SOAL ALP)
# =================================================
print("===== IMPLEMENTASI DASAR GRAF =====")

graph = Graf()

# Menambah node
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

# Menambah edge
graph.add_edge(1, 2, weight=4.5)
graph.add_edge(1, 3, weight=3.2)
graph.add_edge(2, 4, weight=2.7)
graph.add_edge(3, 4, weight=1.8)
graph.add_edge(1, 4, weight=6.7)
graph.add_edge(3, 5, weight=2.7)

# Visualisasi graf
graph.visualize_graph()

# Jalur terpendek
print("Jalur terpendek dari 1 ke 5:", graph.shortest_path(1, 5))

# Visualisasi jalur terpendek
graph.visual_shortest_path(1, 5)


# =================================================
# AFL-3 SOAL 1 — GRAF TAK BERARAH
# =================================================
print("\n===== AFL-3 SOAL 1 =====")

g1 = Graf()
edges1 = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'),
    ('C', 'E'), ('D', 'E'), ('E', 'F'), ('C', 'F')
]

for u, v in edges1:
    g1.add_edge(u, v)

g1.visualize_graph()
print("Derajat simpul:", g1.node_degree())
print("Cycle:", g1.find_cycles())
print("Graf connected:", g1.is_connected())


# =================================================
# AFL-3 SOAL 2 — GRAF TERARAH BERBOBOT
# =================================================
print("\n===== AFL-3 SOAL 2 =====")

g2 = Graf(directed=True)
g2.add_edge(1, 3, 4)
g2.add_edge(3, 2, 6)
g2.add_edge(2, 4, 3)
g2.add_edge(4, 5, 2)
g2.add_edge(5, 3, 5)

g2.visualize_graph()
print("Path 1 ke 5:", g2.shortest_path(1, 5))
print("Cycle:", g2.find_cycles())
print("Strongly connected:", g2.is_connected())
print("Jarak terpendek dari 1:", g2.dijkstra(1))


# =================================================
# AFL-3 SOAL 3 — BFS, DFS, DIJKSTRA
# =================================================
print("\n===== AFL-3 SOAL 3 =====")

g3 = Graf()
edges3 = [
    ('A', 'B', 2), ('A', 'C', 5), ('B', 'D', 4),
    ('B', 'E', 6), ('C', 'F', 3), ('D', 'G', 2),
    ('E', 'F', 4), ('F', 'G', 1)
]

for u, v, w in edges3:
    g3.add_edge(u, v, w)

g3.visualize_graph()
print("BFS dari A:", g3.bfs('A'))
print("DFS dari A:", g3.dfs('A'))
print("Dijkstra dari A:", g3.dijkstra('A'))
print("Path A ke G:", g3.shortest_path('A', 'G'))
