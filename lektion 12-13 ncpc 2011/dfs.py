from edge_list_graph import Edge
from edge_list_graph import Graph
from edge_list_graph import Vertex


class dfs_iterator:

    def __init__(self):
        self._graph = None
        self._visited = []
        self._unexploredV = []
        self._unexploredE = []
        self._counter = 0

    # Exercise 1
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

    # Exercise 2:

    def is_connected(self, g: Graph):
        counter = 0
        for i in self.iterator_dfs(g, 15):
            counter += 1

        if counter == g.num_vertices():
            return True
        return False

    def is_path(self, g: Graph, v1, v2):
        for i in self.iterator_dfs(g, v1):
            if i == v2:
                return True
        return False

    def _DFS(self, g: Graph, v):

        self._unexploredV.remove(v)

        for e in g.incident_edges(v):
            if self._unexploredE.__contains__(e):
                self._unexploredE.remove(e)
                if self._unexploredV.__contains__(e.toVertex()):
                    if e.toVertex == g.end():
                        self._counter = self._counter + 1
                    else:
                        self._DFS(g, e.toVertex())


    def DFS(self, g: Graph):

        for u in g.vertices():
            self._unexploredV.append(u)

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

        return self._counter


'''
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
'''
