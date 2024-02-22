import networkx as nx
import matplotlib.pyplot as plt


g = nx.DiGraph()
g.add_edge("O", "C", length=1)
g.add_edge("O", "A", length=4)
g.add_edge("A", "E", length=3)
g.add_edge("A", "O", length=4)
g.add_edge("A", "B", length=2)
g.add_edge("C", "B", length=2)
g.add_edge("C", "O", length=2)
g.add_edge("C", "D", length=3)
g.add_edge("B", "F", weigth=4)
g.add_edge("B", "A", weigth=4)
g.add_edge("B", "C", weigth=4)
g.add_edge("B", "G", weigth=4)
g.add_edge("D", "E", weigth=4)
g.add_edge("D", "C", weigth=4)
g.add_edge("E", "F", weigth=3)
g.add_edge("E", "A", weigth=3)
g.add_edge("E", "D", weigth=3)
g.add_edge("F", "G", weigth=2)
g.add_edge("F", "B", weigth=4)
g.add_edge("F", "E", weigth=3)
g.add_edge("G", "B", weigth=4)
g.add_edge("G", "F", weigth=2)

resultado = nx.dijkstra_path(g, source="G", target="O")
lg = nx.dijkstra_path_length(g, source="G", target="O")

print(resultado, lg)

nx.draw(g, with_labels=True, font_weight='bold')


plt.show()