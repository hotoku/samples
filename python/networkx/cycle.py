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

g2 = nx.DiGraph()
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(2, 3)
try:
    # デフォルトでは、エッジの向きを気にする
    nx.find_cycle(g2)
except nx.exception.NetworkXNoCycle:
    pass


# orientationに"ignore"を指定すると、向きを無視する
ret = nx.find_cycle(g2, None, "ignore")
print(ret)
