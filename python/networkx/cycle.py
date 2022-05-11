import networkx as nx

g = nx.DiGraph()
g.add_edge(1, 2)
g.add_edge(2, 3)

try:
    nx.find_cycle(g)
except nx.exception.NetworkXNoCycle:
    pass

g.add_edge(3, 1)
ret = nx.find_cycle(g)
print(ret)
