from edge_list_graph import Graph
from edge_list_graph import Edge
from edge_list_graph import Vertex


def opgD(f,s,g,u,d):
    g = Graph()


    #opretter alle hjørner 
    for i in range(1, f):
        g.insert_vertex(i)
    
    #indsætter kanter
    myVertices = list(g.vertices())
    for i in range(1,f, u):
        g.insert_edge(i, myVertices)
