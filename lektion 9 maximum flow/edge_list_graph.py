class Vertex:    
    def __init__(self, e):
        self._element = e
        self._inflow = 0
        self._outflow = 0
    
    def __str__(self):
        return str(self._element)
    
    def element(self):
        return self._element
    
    def inflow(self):
        return self._inflow
    
    def addInflow(self, inflow):
        self._inflow += inflow

    def removeInflow(self, inflow):
        self._inflow -= inflow

    def outflot(self):
        return self._outflow
    
    def addOutflow(self, outflow):
        self._outflow += outflow
    
    def removeOutflow(self, outflow):
        self._outflow -= outflow

    
        
class Edge:
    def __init__(self, e, capacity, v1, v2):
        if e < capacity:
            self._element = e
            self._capacity = capacity
            self._endpoints = [v1, v2]
        else:
            raise Exception('Flow can\'t be bigger than capacity')

    def __str__(self):
        return str(self._element)
    
    #element fungerer som flow
    def element(self):
        return self._element
    
    def capacity(self):
        return self._capacity
    
    def vertexFrom(self):
        return self._endpoints[0]
    
    def vertexTo(self):
        return self._endpoints[1]
    
    def endpoints(self):
        return self._endpoints

class Graph:

    def __init__(self, source, sink):
        self._vertices = []
        self._edges = []
        self._source = source
        self._sink = sink
        
    #Inserts and returns a new vertex containing the element e.
    #Input: V; Output: Vertex    
    def insert_vertex(self, e):
        v = Vertex(e)
        self._vertices.append(v)
        return v
    
    #Removes the vertex v and all its incident edges
    #Input: Vertex; Output: nothing
    def remove_vertex(self, v):
        self._edges = [e for e in self._edges if v not in e._vertices]
        self._vertices.remove(v)
    
    #Inserts and returns a new edge between the vertices v and w. 
    #The element of the edge is o. 
    def insert_edge(self, o, v, w):
        e = Edge(o, v, w)

        if not self.are_adjacent(v, w):
            self._edges.append(e)
        return e

    #Removes the edge e.
    #Input: Edge; Output: nothing
    def remove_edge(self, e):
        self._edges.remove(e)
    
    #Returns the count of vertices in the graph.
    #Input: nothing; Output: int
    def num_vertices(self):
        return len(self._vertices)
    
    #Returns the count of edges in the graph.
    #Input: nothing; Output: int
    def num_edges(self):
        return len(self._edges)
    
    #Returns an iterator on the vertices in the graph.
    #Input: nothing; Output: Iterator
    def vertices(self):
        return iter(self._vertices)
    
    #Returns an iterator on the edges in the graph.
    #Input: nothing; Output: Iterator
    def edges(self):
        return iter(self._edges)
    
    #Returns the degree of the vertex v.
    #Input: Vertex; Output: int
    def degree(self, v):
        d = 0
        for e in self._edges:
            if v in e._endpoints:
                d += 1
        return d
    
    #Returns an iterator on the vertices that are adjacent to v.
    #Input: Vertex; Output: Iterator
    def adjacent_vertices(self, v):
        a = []
        for e in self._edges:
            if v == e._endpoints[0]:
                a.append(e._endpoints[1])
            elif v == e._endpoints[1]:
                a.append(e._endpoints[0])
        return iter(a)
    
    #Returns an iterator on the edges that are incident to v. 
    #Input: Vertex; Output: Iterator
    def incident_edges(self, v):
        i = []
        for e in self._edges:
            if v in e._endpoints:
                i.append(e)
        return iter(i)
    
    #Returns a list with the two vertices at the ends of the edge e. 
    #Input: Edge; Output: list with 2 vertices
    def end_vertices(self, e):
        return e._endpoints[:]
    
    #Returns the vertex opposite v along the edge e.
    #Input: Vertex, Edge; Output: Vertex
    def opposite(self, v, e):
        if e._endpoints[0] == v:
            return e._endpoints[1]
        else:
            return e._endpoints[0]
    
    #Returns whether the vertices v and w are adjacent.
    #Input: Vertex, Vertex; Output: boolean    
    def are_adjacent(self, v, w):
        for e in self._edges:
            if v in e._endpoints and w in e._endpoints:
                return True
        return False

    #Return the capcity of edge e
    #input: Edge e; Output: int
    def getCapcity(self, e):
        return e.getCapcity()
            
    
    #Return whether flow conservation is respected.
    #is only called on a residual graph 
    #output: bool
    def flowConservation(self):
        pass

    def sink(self):
        return self._sink
    
    def source(self):
        return self._source