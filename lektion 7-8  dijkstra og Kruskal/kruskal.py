from edge_list_graph import Graph
from edge_list_graph import Vertex
from edge_list_graph import Edge
from heap_priority_queue import HeapPriorityQueue
import math

def kruskal(g:Graph):
    q = HeapPriorityQueue()
    clusters = []
    T = []
    for v in g.vertices():
        clusters.append([v])
        v.pos = len(clusters)-1
    
    for e in g.edges():
        q.add(e._element, e)
    
    while len(T) < g.num_vertices()-1:
        (w,e) = q.remove_min()
        v1 = g.end_vertices(e)[0]
        v2 = g.end_vertices(e)[1]
        
        A = clusters[v1.pos]
        B = clusters[v2.pos]

        if A != B:
            _merege(A,B)
            T.append(e)
    return T


def _merege(A,B):

    if len(A) > len(B):
        biggest = A
        smallest = B
    else:
        biggest = B
        smallest = A

    for i in range(len(smallest)):
        biggest.append(smallest[i])
        smallest.pop(i)


g = Graph()

v15 = g.insert_vertex(15)
v6 = g.insert_vertex(6)
v38 = g.insert_vertex(38)
v123 = g.insert_vertex(123)
v66 = g.insert_vertex(66)

g.insert_edge(10,v15,v38)
g.insert_edge(23, v15,v6)
g.insert_edge(90, v15,v66)
g.insert_edge(8, v66,v6)
g.insert_edge(2, v66,v38)
g.insert_edge(76, v66,v123)
g.insert_edge(7, v123,v6)
g.insert_edge(55, v123,v38)

for e in kruskal(g):
    print(str(e))
