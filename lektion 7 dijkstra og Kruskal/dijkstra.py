import edge_list_graph
from edge_list_graph import Graph
from edge_list_graph import Vertex
from edge_list_graph import Edge
import math
from adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

infinity = math.inf

def dijkstra(g, s):
    q = AdaptableHeapPriorityQueue()
    dist = {}
    locators = {}
    for v in g.vertices():
        if v == s:
            dist[v] = 0
        else:
            dist[v] = infinity
        l = q.add(dist[v], v)
        locators[v] = l
    
    while q.__len__()>0:
        (key, u) = q.remove_min()
        print("***", key, u)
        for e in g.incident_edges(u):
            w = g.opposite(u,e)

            if dist[w] > dist[u] + e.element():
                dist[w] = dist[u] + e.element()
                q.update(locators[w],dist[w], w)


g = edge_list_graph.Graph()

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



dijkstra(g,v15)

