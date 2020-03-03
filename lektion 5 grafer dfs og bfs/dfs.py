from edge_list_graph import Edge
from edge_list_graph import Graph
from edge_list_graph import Vertex

class dfs_iterator:

    def __init__(self):
        self._graph = None
        self._visited = []  
        self._unexploredV = []
        self._unexploredE = []

    #Exercise 1
    def _dfs_visit(self, v):
        self._visited.append(v)
        for i in self._graph.adjacent_vertices(v):
            if i not in self._visited:
                return self._dfs_visit(i)
        
        
    def iterator_dfs(self, g, v):
        self._graph = g
        self._visited = []
        self._dfs_visit(v)
        return iter(self._visited)

    #Exercise 2:

    def is_connected(self, g: Graph):
        counter = 0
        for i in self.iterator_dfs(g,15):
            counter += 1

        if counter == g.num_vertices():
            return True
        return False
    
    def is_path(self, g: Graph, v1, v2):
        for i in self.iterator_dfs(g,v1):
            if i == v2:
                return True
        return False
    
    def _DFS(self, g : Graph, v):

        self._unexploredV.remove(v)

        for e in g.incident_edges(v):
            if self._unexploredE.__contains__(e):
                self._unexploredE.remove(e)
                for w in e.endpoints():  
                    if w != v and self._unexploredV.__contains__(w):
                        self._DFS(g, w)


    def DFS(self, g: Graph):
        
        for u in g.vertices():
            self._unexploredV.append(u._element)
        
        for u in g.edges():
            self._unexploredE.append(u)
        
        print("Unexplored edge:")
        for i in self._unexploredE:
            print(i)
        print("Unexplored vertex")
        for i in self._unexploredV:
            print(i)
        
        for u in self._unexploredV:
            self._DFS(g, u)

g = Graph()

g.insert_vertex(15)
g.insert_vertex(6)
g.insert_vertex(38)
g.insert_vertex(123)
g.insert_vertex(66)

g.insert_edge(10,15,38)
g.insert_edge(23, 15,6)
g.insert_edge(90, 15,66)
g.insert_edge(8, 66,6)
g.insert_edge(2, 66,38)
g.insert_edge(76, 66,123)
g.insert_edge(7, 123,6)
g.insert_edge(55, 123,38)

g2 = Graph()

g2.insert_vertex(15)
g2.insert_vertex(6)

d = dfs_iterator()
for i in d.iterator_dfs(g,15):
    print(i)

print(d.is_connected(g2))

print(d.is_path(g2, 15,6))

for i in g.incident_edges(15):
    print(i)

d.DFS(g)



print("Unexplored Edge")
for i in d._unexploredE:
    print(i)

print("Unexplored Vertex")
for i in d._unexploredV:
    print(i)
