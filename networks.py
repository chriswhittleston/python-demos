#!/usr/bin/python

# import useful modules
import networkx as nx
import matplotlib.pyplot as plt

# create a graph object
g = nx.Graph()
# add some edges
g.add_edge('a', 'b', duration=0.1)
g.add_edge('b', 'c', duration=1.5)
g.add_edge('a', 'c', duration=1.0)
g.add_edge('c', 'd', duration=2.2)

# determine positions for labels 
pos=nx.spring_layout(g)

# find the shortest path with edges weighted using duration
path = nx.shortest_path(g, 'b', 'd', 'duration')
# create list of edges on shortest path
path_edges = zip(path,path[1:])

# DEBUGGING
print path
print path[1:]
print path_edges

# plot the network using matplotlib
nx.draw_networkx(g, pos, alpha=0.5)
# plot edge labels
nx.draw_networkx_edge_labels(g, pos)

# re-plot nodes and edges on the shortest path
nx.draw_networkx_nodes(g,pos,nodelist=path,node_color='b')
nx.draw_networkx_edges(g,pos,edgelist=path_edges,edge_color='b',width=10)

# show plot
plt.show()
