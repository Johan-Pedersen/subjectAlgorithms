class Vertex:    
    def __init__(self, e, incidentEdges):
        self._element = e
        #Key er hjørnet og value er den kant som forbinder dem
        self._incidentEdges = incidentEdges
        self._degree = len(self._incidentEdges)
    
    def __str__(self):
        return str(self._element)

    def getIncidentEdges(self):
        return self._incidentEdges

    def getDegree(self):
        return self._degree
    
    def addDegree1(self):
        self._degree += 1

    def element(self):
        return self._element
    
        
class Edge:
    def __init__(self, e, v1: Vertex, v2 : Vertex):
        self._element = e
        v1.getIncidentEdges().append(e)
        v1.addDegree1()
        v2.getIncidentEdges().append(e)
        v2.addDegree1()
        self._endpoints = [v1, v2]
    
    def __str__(self):
        return str(self._element)
    
    def element(self):
        return self._element
    
    def endpoints(self):
        return self._endpoints

class Graph:

    #Man declare Vertex'er og Edge's på samme tid og bagefter tilføjer man dem til grafen
    def __init__(self):
        self._vertices = []
    
    #Inserts and returns a new vertex containing the element e.
    #Input: V; Output: Vertex    
    def insert_vertex(self, e):
        v = Vertex(e)
        self._vertices.append(v)
        return v
    
    #Removes the vertex v and all its incident edges
    #Input: Vertex; Output: nothing

    def remove_vertex(self, v: Vertex):
        for i in v.getIncidentEdges().Keys():
            i.getIncidentEdges().remove(v)
            v.getIncidentEdges().remove(i)
        self._vertices.remove(v)
    
    #Inserts and returns a new edge between the vertices v and w. 
    #The element of the edge is o.    

    '''
    Er det nødvendigt at have denne metode, da kanterne kun kendes af hjørnerne og 
    derfor indsættes ny kanter direkte mellem 2 hjørner frem for direkte i grafen.
    '''
    def insert_edge(self, o, v, w):
        e = Edge(o, v, w)
        return e

    #Removes the edge e.
    #Input: Edge; Output: nothing
    def remove_edge(self, e):
        pass
        #Hvordan kan man lave remove_edge med O(1) tid
    
    #Returns the count of vertices in the graph.
    #Input: nothing; Output: int
    def num_vertices(self):
        return len(self._vertices)
    
    #Returns the count of edges in the graph.
    #Input: nothing; Output: int
    def num_edges(self):
        count = 0
        for i in vertices:
            count += i.getDegree()
        return count
    
    #Returns an iterator on the vertices in the graph.
    #Input: nothing; Output: Iterator
    def vertices(self):
        return iter(self._vertices)
    
    #Returns an iterator on the edges in the graph.
    #Input: nothing; Output: Iterator
    '''
    def edges(self):
        return iter(self._edges)
    '''

    #Returns the degree of the vertex v.
    #Input: Vertex; Output: int
    def degree(self, v):
        return v.getDegree()
    
    #Returns an iterator on the vertices that are adjacent to v.
    #Input: Vertex; Output: Iterator
    def adjacent_vertices(self, v):
        a = []
        for e in v.getIncidentEdges():
            if v == e._endpoints[0]:
                a.append(e._endpoints[1])
            elif v == e._endpoints[1]:
                a.append(e._endpoints[0])
        return iter(a)
    
    #Returns an iterator on the edges that are incident to v. 
    #Input: Vertex; Output: Iterator
    def incident_edges(self, v: Vertex):
        return v.getIncidentEdges()
    
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
    def are_adjacent(self, v:Vertex, w: Vertex):
        for i in v.getIncidentEdges():
            if i.endpoints()[1] == w:
                return True
        return False


