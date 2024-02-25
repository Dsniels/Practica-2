import networkx as nx
import matplotlib.pyplot as plt
from unratedwriting import typewrite

g = nx.DiGraph()

g.add_edge("LA ROCA", "PAUL WALKER", length = 1)
g.add_edge("LA ROCA", "RYAN REINOLDS", length = 1)
g.add_edge("RYAN REINOLDS", "HUGH JACKMAN", length = 1)
g.add_edge("HUGH JACKMAN", "ZACK EFRON", length = 1)
g.add_edge("ZACK EFRON", "ZENDAYA", length = 1)
g.add_edge("ZENDAYA", "TOM HOLLAND", length = 1)
g.add_edge("TOM HOLLAND","JAMIE FOX", length = 1)
g.add_edge("JAMIE FOX", "LA ROCA", length = 1)

result = str(nx.dijkstra_path(g, source="LA ROCA", target="TOM HOLLAND"))
typewrite(result, delay=0.02)

nx.draw(g, with_labels = True, font_weight='bold')

plt.show()


