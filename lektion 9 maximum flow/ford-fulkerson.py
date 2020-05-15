from edge_list_graph import Edge
from edge_list_graph import Vertex
from edge_list_graph import Graph


class ford_fulkerson:

    def __init__(self, graph):
        self._graph = graph
        self._visited = []  
        self._unexploredV = []
        self._unexploredE = []
        self._augmentingPath = [] #indeholder kanterne stil stien fra source til sink

    # Return a graph that is a residual network
    def _findResidualNetwork(self):
        graph = self._graph
        residualGraph = Graph()
        residualGraph._source = graph.source
        residualGraph._sink = graph.sink

        # laver en residual edge re med en eksra attribut cf, som indeholder
        # hvor meget mere flow denne edge kan tage
        for v in graph.vertices():
            residualGraph.insert_vertex(v)

        print("***Residualnetwork edges before***")
        for e in graph.edges():
            #re == residual edge
            re = Vertex(e.element())
            re.cf = e.capacity() - e.element()
            residualGraph.insert_edge(e.element(), e.capacity(), e.vertexFrom(), e.vertexTo())

            print("e.element: ", e.element(), "e.capacity: ", e.capacity())
            print("re.cf ", re.cf)


        return residualGraph

    def _findAugmentingPath(self):
        self.DFS(self._graph)

#tager en risudal graf som parameter
    def DFS(self, residualGraph):

        for u in residualGraph.vertices():
            self._unexploredV.append(u._element)

        for u in residualGraph.edges():
            self._unexploredE.append(u)

        for u in residualGraph.adjacent_vertices(residualGraph.source()):
            if(self._unexploredV.__contains__(u)):
                self._augmentingPath = []
                self._DFS(u)

                #Laver selve operationerne her

                #Finder edgen med lavest cf og sætte alle kanternes flow til at være dette

                minCf = self._augmentingPath[0].cf
                for e in self._augmentingPath:
                    minCf = min(e.cf, minCf)
                
                for e in self._augmentingPath:
                #_element == flow
                    e._element = minCf
        
        return residualGraph
    
    def _DFS(self, v: Vertex):
        graph = self._graph
        if v == graph.source:
            return

        self._unexploredV.remove(v)

        for e in graph.incident_edges(v):
            if self._unexploredE.__contains__(e):
                self._unexploredE.remove(e)

                if e.cf >0:
                    self._augmentingPath.append(e)
                    w = e.vertexTo() 
                    if w == graph.sink:
                        return
                    if self._unexploredV.__contains__(w):
                        self._DFS(w)
g = Graph()

v15 = g.insert_vertex(15)
v6 = g.insert_vertex(6)
v38 = g.insert_vertex(38)
v123 = g.insert_vertex(123)
v66 = g.insert_vertex(66)

g.source = v15
g.sink = v123

g.insert_edge(10,20,v15,v38)
g.insert_edge(23, 30, v15,v6)
g.insert_edge(90,100, v15,v66)
g.insert_edge(8, 16,v66,v6)
g.insert_edge(2, 16, v66,v38)
g.insert_edge(76, 100,v66,v123)
g.insert_edge(7, 24,v123,v6)
g.insert_edge(55,70, v123,v38)

ff = ford_fulkerson(g)





for e in ff.DFS(ff._findResidualNetwork()).edges():
    print("e.element: ", e.element(), "e.capacity: ", e.capacity())
    
