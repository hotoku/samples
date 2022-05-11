import networkx as nx

g = nx.DiGraph()
g.add_node(1)
g.add_node(1)
g.add_node("a")

print(g)
# => DiGraph with 2 nodes and 0 edges
# 同じオブジェクトは複数回登録しても区別されない
