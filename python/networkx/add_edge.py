import networkx as nx

g = nx.DiGraph()
g.add_edge(1, 2)
print(g)
# => DiGraph with 2 nodes and 1 edges
# いきなり知らないノードを追加して大丈夫

g.add_edge(1, 2)
print(g)
# => DiGraph with 2 nodes and 1 edges
# デフォルトでは辺の重複は許されない
