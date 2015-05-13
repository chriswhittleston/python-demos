#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edge('a', 'b', duration=0.1)
g.add_edge('b', 'c', duration=1.5)
g.add_edge('a', 'c', duration=1.0)
g.add_edge('c', 'd', duration=2.2)

print nx.shortest_path(g, 'b', 'd')
print nx.shortest_path(g, 'b', 'd', 'duration')

nx.draw(G)
plt.draw()
