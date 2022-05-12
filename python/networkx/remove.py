import networkx as nx

g = nx.DiGraph()
g.add_edge(1, 2)
g.remove_edge(1, 2)
print(g)
# => DiGraph with 2 nodes and 0 edges
# 孤立したノードも残る
