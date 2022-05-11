import networkx as nx

g = nx.DiGraph()
g.add_edge(1, 2)
g.add_edge(2, 3)

g2 = nx.DiGraph(g)
g2.clear()

print(g)
print(g2)

# =>
# DiGraph with 3 nodes and 2 edges
# DiGraph with 0 nodes and 0 edges
