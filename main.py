import networkx as nx
import matplotlib.pyplot as plt
import pyvis
from pyvis.network import Network


net = Network(height="750px",font_color=True, width="100%", bgcolor="#222222", cdn_resources="remote")




net.add_nodes([1,2,3,4,5,6,7,8,9,10], label = ['David','Daniel', 'Liz','Mike','Daniel de la Fuente','Blanca','Barbara','DaniLentes','Hugo','Norma'])
net.add_edges([(1,3,5), (2,4,10), (3,6,11), (5,4,3), (2,5,4), (2,6,6), (4,3,1), (7,2,3), (8,3,5), (1,9,10), (9,10,10),(2,3,20)])




net.show_buttons(filter_=['physics'])
net.show("red.html", notebook=False)

