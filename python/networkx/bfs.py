import networkx as nx

g = nx.DiGraph()
g.add_edge(1, 11)
g.add_edge(1, 12)
g.add_edge(11, 21)
g.add_edge(11, 22)
g.add_edge(12, 23)
g.add_edge(12, 24)

print(list(nx.bfs_successors(g, 1)))
# => [(1, [11, 12]), (11, [21, 22]), (12, [23, 24])]

for e in nx.edge_bfs(g, 1):
    print(e)
# =>
# (1, 11)
# (1, 12)
# (11, 21)
# (11, 22)
# (12, 23)
# (12, 24)
