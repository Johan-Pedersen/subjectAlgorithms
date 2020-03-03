class Node:

    def __init__(self, key, value):
        self._key = key
        self._value = value
    
    def __repr__(self):
        return '({0},{1})'.format(self._key, self._value)
    
    def __lt__(self, node):
        return self._key < node._key


class heap_priotity_queue:

    def __init__(self):
        self._queue = []

    def _left(self, j):
        return j*2+1

    def _right(self, j):
        return j*2+2

    def AddNode(self, node):
        self._queue.append(node)

        _upHeap(len(self._queue)-1)

    def _parent(self, j):
        return j-1 //2

    def _swap(self, i, j):
        self._queue[i], self._queue[j] = self._queue[j], self._queue[i]
        
    def _upHeap(self,j):
        parent = _parent(j)
        if self._queue[j] < self._queue[parent]:
            self._swap(j, parent)

            return _upHeap(parent)
    
    def removeMin(self, node):
        self._queue[0] = self._queue[len(self._queue)-1]
        self._queue.pop(len(self._queue)-1)
        self._downheap(0)

    
    def _downheap(self, j):
        if self._queue[self._left(j)] != None:
            smallChild = self._left
            #find den mindste af børnene og swap med denne. Kald rekursivt
            if self._queue[self._right(j)] != None:
                if self._queue[self._right(j)]< self._queue[self._left(j)]:
                    smallChild = self._right
            if(self._queue[smallChild] > self._queue[j]):
                self.swap(smallChild, j)
                return _downheap(smallChild)





