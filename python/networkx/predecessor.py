import networkx as nx

g = nx.DiGraph()
g.add_edge(1, 2)
g.add_edge(3, 2)
ret = g.predecessors(2)
print(ret)
# => <dict_keyiterator object at 0x7fabe8137a60>

print(list(ret))
# => [1, 3]
