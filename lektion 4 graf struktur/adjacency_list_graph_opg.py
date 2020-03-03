from adjacency_list_graph import Edge as Edge
from adjacency_list_graph import Graph as Graph
from adjacency_list_graph import Vertex as Vertex
g = Graph()



enfem = Vertex(15, {38: 10, 6:23, 66:90})
g.insert_vertex(enfem)
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


LastVisitet = 0
mx = -1
mySet = set()
def max_value(graf : Graph, vertex):
    global mx

    if(mySet.__len__() == graf.num_vertices()):
        return mx
    if(vertex > mx):
        mx = vertex
    if not mySet.__contains__(vertex):
        mySet.add(vertex)
        LastVisitet = vertex
        for i in graf.adjacent_vertices(vertex):
            if not mySet.__contains__(i):
                return max_value(graf, i)
    
    return max_value(graf, LastVisitet)

print(max_value(g, 15))