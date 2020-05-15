# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:39:05 2019

@author: jhaj
"""

class Vertex:
    
    def __init__(self, element):
        self._element = element
        self._outgoing = []
        self._incoming = []

    def element(self):
        return self._element
    
    def outgoing(self):
        return self._outgoing
    
    def incoming(self):
        return self._incoming
    
class Edge:
    
    def __init__(self, capacity, start, end):
        self._capacity = capacity
        self._start = start
        self._end = end
        self._flow = 0
        
    def start(self):
        return self._start
    
    def end(self):
        return self._end

    def capacity(self):
        return self._capacity

    def flow(self):
        return self._flow
    
    def inc_flow(self, inc):
        self._flow += inc
    
    def residual_capacity(self):
        return self._capacity - self._flow
    
class Residual_Edge(Edge):
    def __init__(self, parent):
        super().__init__(parent.flow(), parent.end(), parent.start())
        self._parent = parent
    
    def residual_capacity(self):
        return self._capacity

    def parent_edge(self):
        return self._parent
        
class FlowNetwork:
    
    def __init__(self):
        self._source = None
        self._sink = None
        self._vertices = []
        self._edges = []
        self._residual_edges = []
    
    def insert_vertex(self, label, source=False, sink=False):
        v = Vertex(label)
        self._vertices.append(v)
        if source:
            self._source = v
        elif sink:
            self._sink = v
        return v
    
    def insert_edge(self, capacity, start, end):
        e = Edge(capacity, start, end)
        start._outgoing.append(e)
        end._incoming.append(e)
        self._edges.append(e)
        
    def insert_residual_edge(self, parent):
        e = Residual_Edge(parent)
        parent.end()._outgoing.append(e)
        parent.start()._incoming.append(e)
        self._residual_edges.append(e)

    def find_max_flow(self): 
        while True:
            p = self.augmenting_path()
            if p == None:
                break
            else:
                self.augment_flow(p)
        result = 0
        for e in self._source.outgoing():
            result += e.flow()
        return result
    
    def augment_flow(self, path):
        low = float("inf")
        for e in path:
            low = min(low, e.residual_capacity()) 
        for e in path:
            if type(e) == Residual_Edge:
                e.parent().inc_flow(-low)
            else:
                e.inc_flow(low)
        self.delete_residual_edges()
        for e in self._edges:
            if e.flow() > 0:
                self.insert_residual_edge(e)

    def delete_residual_edges(self):
        for e in self._residual_edges:
            e.start().outgoing().remove(e)
            e.end().incoming().remove(e)
        self._residual_edges = []    

    def augmenting_path(self):
        l = [[self._source]]
        path = [[]]
        visited = []
        i = 0
        found = False
        while len(l[i]) > 0 and not found:
            l.append([])
            path.append([])
            for v in l[i]:
                for e in v._outgoing:
                    if e.residual_capacity() > 0 and not e in visited:
                        visited.append(e)
                        l[i+1].append(e.end())
                        path[i+1].append(e)
                        if e.end() == self._sink:
                            found = True
                            break
                if found:
                    break
            if found:
                break
            i += 1
        if found:    
            return(self.lists_to_path(l, path))
        else:
            print("no path")
            return None
#        return (l, path)
#        for p in path:
#            for e in p:
#                print(e.capacity())
#            print()
#        print(path)
#        print(l)
#        for i in range(len(path)):
#            for j in range(len(path[i])):
#                print(l[i][j].element(), path[i][j].capacity())

    def lists_to_path(self, vertices, edges):
        path = []
        current = self._sink
        i = len(edges) - 1
        while current != self._source:
            pos = vertices[i].index(current)
            path.insert(0, edges[i][pos])
            current = edges[i][pos]._start
            i -= 1
        return path
#        print(path)
#        for e in path:
#            print(e.capacity())
        
        
        
f = FlowNetwork()
vs = f.insert_vertex("s", source=True)
vt = f.insert_vertex("t", sink=True)
v1 = f.insert_vertex("1")
v2 = f.insert_vertex("2")
v3 = f.insert_vertex("3")
v4 = f.insert_vertex("4")

f.insert_edge(16, vs, v1)
f.insert_edge(13, vs, v2)
f.insert_edge(4, v2, v1)
f.insert_edge(12, v1, v3)
f.insert_edge(9, v3, v2)
f.insert_edge(14, v2, v4)
f.insert_edge(7, v4, v3)
f.insert_edge(20, v3, vt)
f.insert_edge(4, v4, vt)


#f.augmenting_path()
print(f.find_max_flow())