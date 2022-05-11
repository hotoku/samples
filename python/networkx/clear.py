import networkx as nx

g = nx.DiGraph()
g.add_edge(1, 2)
g.add_edge(2, 3)

g2 = nx.DiGraph(g)
g2.clear()

print(g)
print(g2)
