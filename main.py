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
g.add_edge("KEVIN COSTNER", "lESLY MANVILLE", length = 1)
g.add_edge("lESLY MANVILLE", "ANGELINA JOLIE", length = 1)
g.add_edge("ANGELINA JOLIE", "JACK BLACK", length = 1)
g.add_edge("ANGELINA JOLIE", "BRAD PITT", length = 1)
g.add_edge("JACK BLACK", "LA ROCA", length = 1)
g.add_edge("JAMIE FOX", "WILL SMITH", length = 1)
g.add_edge("WILL SMITH", "MARGOT ROBBIE", length = 1)
g.add_edge("MARGOT ROBBIE", "LEONARDO DICAPRIO", length=1)
g.add_edge("MARGOT ROBBIE", "BRAD PITT", length=1)
g.add_edge("LEONARDO DICAPRIO", "BRAD PITT", length=1)
pos = nx.spring_layout(g, k=1.20)
result = str(nx.dijkstra_path(g, source="LA ROCA", target="BRAD PITT"))
typewrite('Los actores que conectan a La ROCA y a BRAD PITT son:', delay=0.1)
if (result):
       typewrite(result, delay=0.1)
else:
    result = str(nx.dijkstra_path(g, source="LA ROCA", target="MARGOT ROBBIE"))
    typewrite(result, delay=0.1)
    
nx.draw (g, pos, with_labels = True, font_weight='bold', node_size = 5000)
plt.show()


