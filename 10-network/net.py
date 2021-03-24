import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

g.add_node(1)
g.add_nodes_from([2,3])
g.add_node('ET')

print(g.nodes())

g.remove_node(1)

print(g.nodes())

g.add_edge(1,2)
g.add_edge(3,'ET')
g.add_edges_from([(2,3), (1,3)])
print(g.edges())
print(g.nodes())

g.remove_edge(1,2)
print(g.edges())
print(list(g.neighbors(1)))
print(g.degree(1))

G = nx.DiGraph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(range(100,110))

H = nx.Graph()
nx.add_path(H, [0,1,2,3,4,5,6,7,8,9])

G.add_nodes_from(H)
print(G.nodes())

nx.draw_networkx(G)
plt.show()

G.add_edge(1, 2)
G.add_edges_from([(1,2),(1,3)])
G.add_edges_from(H.edges())
print(G.edges())

nx.draw_networkx(G)
plt.show()

G = nx.lollipop_graph(4, 6)
nx.draw_networkx(G)
plt.show()

print("diameter: %d" % nx.diameter(G))
print()
print("degree centrality of nodes in G: ", nx.degree_centrality(G))

# for more, see networkx docs https://networkx.github.io/documentation/stable/reference/algorithms/index.html
