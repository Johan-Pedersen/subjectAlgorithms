from edge_list_graph import Graph
from edge_list_graph import Vertex
from edge_list_graph import Edge
from heap_priority_queue import HeapPriorityQueue
import math

def kruskal(g:Graph):
    q = HeapPriorityQueue()
    T = [] #Holder listen af edges med minimal vægt
    trees = {}
    union = unionFind()
    
    for v in g.vertices():
        trees[v] = union.makeset(v)

    for e in g.edges():
        q.add(e._element, e)
    
    while len(T) < g.num_vertices() -1:
        (u,e) = q.remove_min()
        v1 = g.end_vertices(e)[0]
        v2 = g.end_vertices(e)[1]

        leaderv1 = union.quickFind(trees[v1])
        leaderv2 =union.quickFind(trees[v2])

        if leaderv1._element != leaderv2._element:
            union.quickUnion(leaderv1, leaderv2)
            T.append(e)
    return T


class unionFind:

    class TreeNode:

        def __init__(self, element):
            self._parent = self
            self._element = element
            self._size = 1
        

        def setParent(self, node):
            
            if node._size > self._size:
                self._parent = node
                node._size += self._size  
            else:
                node._parent = self
                self._size += node._size
    '''
    Union-find algoritmer
    '''
#laver et træ med 1 element i
    def makeset(self,x):
        return self.TreeNode(x)

#finder nodens leader (Øverste node)
    def quickFind(self, x):
        if x._parent != x:
            self.quickFind(x._parent)
        return x

#tilføjer det mindste træ, som barn til leaderen på det største 
    def quickUnion(self, x,y):
        self.TreeNode.setParent(x, y)



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
