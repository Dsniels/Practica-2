import time 
from tqdm import tqdm
from pyvis.network import Network
import pandas as pd 

net  = Network(height="750px",font_color=True, width="100%", bgcolor="#222222", cdn_resources="remote")
data = pd.read_csv('Libro1.csv')

n = len(set(data['nodo 1']).union(set(data['nodo 2'])))
m = len(data)

grados = data['nodo 1']._append(data['nodo 2']).value_counts()


total = len(data)
source = data['nodo 1']
target = data['nodo 2']

edge_data = zip(source, target)
progress = tqdm(total=total, desc="Creando nodos")
for e in edge_data:
    src = e[0]
    trg = e[1]

    net.add_node(src, src, title = src)
    net.add_node(trg,label=trg, title = src)
    net.add_edge(src, trg)
    progress.update(1)

vecino = net.get_adj_list()

for e in net.nodes:
    e['title'] += " vecinos: " + ',' .join(vecino[e['id']])

progress.close()
time.sleep(1)
print(f'Numero de vertices: {n}')
print(f'Numero de Aristas: {m}')
print(f'Grados de cada vertice:')
print(grados)
time.sleep(1)
net.show("Red de amigos.html", notebook=False)



