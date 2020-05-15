class AVL:

    def __init__(self):
        super().__init__()

    def getRoot(self):
        return self._root

    def setRoot(self, root):
        self._root = root
        root.setParent(-1)

    def createNode(self, key, val):
        return self.Node(key, val)

    class Node:
        def __init__(self, key, val):
            self._parent = -1
            self._right = -1
            self._left = -1
            self._height = 1
            self._key = key
            self._val = val

        def getKey(self):
            return self._key

        def getVal(self):
            return self._val

        def getParent(self):
            return self._parent

        def setParent(self, parent):
            self._parent = parent

        def getRight(self):
            return self._right

        def setRight(self, node):
            self._right = node
            if node != -1:
                node.setParent(self)

        def getLeft(self):
            return self._left

        def setLeft(self, node):
            self._left = node
            if node != -1:
                node.setParent(self)

        def getHeight(self):
            return self._height
        
        def setHeight(self, height):
            self._height = height

        def heightLeft(self):
            if(self._left != -1):
                return self._left.getHeight()
            return 0
        
        def setHeightLeft(self, height):
            self.getLeft().setHeight(height)

        def heightRight(self):
            if(self._right != -1):
                return self._right.getHeight()
            return 0
        
        def setHeightRight(self, height):
            self.getRight().setHeight(height)
        
        def calcHeight(self):
            return max(self.heightRight(), self.heightLeft())+1

        #Kaldes ved indsættelse
        def incrementHeight(self):
            self._height = self._height + 1

            parent = self.getParent()
            if parent != -1:
                parent.incrementHeight()

        #Kaldes ved fjernelse
        def decrementHeight(self):
            self._height = self._height - 1

            parent = self.getParent()
            if parent != -1:
                parent.decrementHeight()

    #Kaldes for at genudregne højden af noderne i træet.
    def reCalcHeight(self, node):
        
        if node == -1:
            return 0
        if  self.isLeaf(node):
            node.setHeight(1)
            return 1
        else:
            node.setHeight(max(self.reCalcHeight(node.getLeft()), self.reCalcHeight(node.getRight()))+1)
            return node.getHeight()
        

    # insert
    def insert(self, node):
        self._insert(self.getRoot(), node)

        unbalancedNode = self.isBalanced(node)
        self.balance(unbalancedNode)

    # insert hjælpe metode
    def _insert(self, node, newNode):

        if self.isLeaf(node):
            node.incrementHeight()

        if node.getKey() <= newNode.getKey():
            if node.getRight() == -1:
                node.setRight(newNode)
            else:
                return self._insert(node.getRight(), newNode)
        else:
            if node.getLeft() == -1:
                node.setLeft(newNode)
            else:
                return self._insert(node.getLeft(), newNode)

    #Kaldes for at sikre træet's height balanace property.
    #Metoden kaldes på den første node fra bunden som er i ubalance.
    def balance(self, unbalancedNode):
        #unbalancedNode != -1 betyder at der  er nogle ubalanceret noder i træet
        while (unbalancedNode != -1):
                # De 4 senarier for ubalance

                # unbalancedNode er 2 niveauer dybere i højre side end venstre
            if unbalancedNode.heightLeft()-unbalancedNode.heightRight() == -2:

                # unbalancedNode.right hvilken side der er dybere end den anden
                if unbalancedNode.getRight().heightLeft()-unbalancedNode.getRight().heightRight() == -1:
                    self.leftRotate(unbalancedNode)
                else:
                    self.rightLeftRotate(unbalancedNode)

            # unbalancedNode er 2 niveauer dybere i venstre side end højre
            elif unbalancedNode.heightLeft()-unbalancedNode.heightRight() == 2:
                # unbalancedNode.left hvilken side der er dybere end den anden
                if unbalancedNode.getLeft().heightLeft()-unbalancedNode.getLeft().heightRight() == -1:
                    self.leftRightRotate(unbalancedNode)
                else:
                    self.rightRotate(unbalancedNode)
            
            self.reCalcHeight(self.getRoot())

            #Tjekker om resten af subtræet er balanceret
            unbalancedNode = unbalancedNode.getParent()

    # Delete hjælpe metoder
    def setRightLeftTreeRoot(self, node):
        node.setRight(self.getRoot().getRight())
        node.setLeft(self.getRoot().getLeft())
        self.setRoot(node)
        node.decrementHeight()
        self.balance(node)

    def setRightLeftTree(self,deletedNode, node):
        node.setRight(deletedNode.getRight())
        node.setLeft(deletedNode.getLeft())
        node.setParent(deletedNode.getParent()) 
        deletedNode.getParent().setRight(node)
        node.decrementHeight()
        self.balance(node)

    def setLeftRightTree(self, deletedNode, node):
        node.getParent().setRight(-1)
        node.setLeft(deletedNode.getLeft())
        node.setRight(deletedNode.getRight())
        node.setParent(deletedNode.getParent())
        deletedNode.getParent().setLeft(node)
        node.decrementHeight()
        self.balance(node)

    #Delete
    def delete(self, node):

        #Hvis man vil slette roden
        if node.getKey() == self.getRoot().getKey():
            tempNode = node.getRight()

            #så længe man kan gå til venstre, så gør man det
            while tempNode.getLeft() != -1:
                tempNode = tempNode.getLeft()

            #Hvis den node man har fundet ikke er den yderste
            if not self.isLeaf(tempNode):

                #Hvis ikke nodens højre barn er det yderste man har fundet
                if not self.isLeaf(tempNode.getRight()):
                    
                    #Hvis der er zigzag kæde tilsidst
                    if tempNode.getRight().getLeft() != -1:
                        leafnode = tempNode.getRight().getLeft()
                        leafnode.getParent().setLeft(-1)
                        self.setRightLeftTreeRoot(leafnode)
                    else:
                        leafnode = tempNode.getRight().getRight()
                        leafnode.getParent().setRight(-1)
                        self.setRightLeftTreeRoot(leafnode)
                #Hvis noden er den yderste node
                else:
                    leafnode = tempNode.getRight()
                    leafnode.getParent().setRight(-1)
                    self.setRightLeftTreeRoot(leafnode)

            #Hvis den første node man har fundet er den yderste
            else:
                    tempNode.getParent().setLeft(-1)
                    self.setRightLeftTreeRoot(tempNode)
        #Hvis man vil slette en node som er større end rodden
        elif node.getKey() > self.getRoot().getKey():
        #så længe man kan gå til venstre gør man det
            tempNode = node
            while tempNode.getLeft() != -1:
                tempNode = tempNode.getLeft()
            
            #Hvis den node man har fundet ikke er den yderste
            if not self.isLeaf(tempNode):   

                #Hvis ikke nodens højre barn er det yderste man har fundet
                if not self.isLeaf(tempNode.getRight()):

                    #Hvis der er zigzag kæde tilsidst
                    if tempNode.getRight().getLeft() != -1:
                        leafnode = tempNode.getRight().getLeft()
                        leafnode.getParent().setLeft(-1)
                        self.setRightLeftTree(node, leafnode)
                    else:
                        leafnode = tempNode.getRight().getRight()
                        leafnode.getParent().setRight(-1)
                        self.setRightLeftTree(node, leafnode)

                #Hvis noden er den yderste node
                else:
                    leafnode = tempNode.getRight()
                    leafnode.getParent().setRight(-1)
                    leafnode.setLeft(node.getLeft())
                    leafnode.setParent(node.getParent())  
                    node.getParent().setRight(leafnode)

            #Hvis noden man vil fjerne er den ydereste 
            else:
                    tempNode.getParent().setLeft(-1)
                    self.setRightLeftTree(node, tempNode)
        #Hvis noden man vil fjerne er mindre end rodden
        else:

            #så længe man kan gå til højre, så gør man det
            tempNode = node
            while tempNode.getRight() != -1:
                tempNode = tempNode.getRight()
            
            #Hvis den node man har fundet ikke er den yderste
            if not self.isLeaf(tempNode):   

                #Hvis ikke nodens venstre barn er det yderste man har fundet
                if not self.isLeaf(tempNode.getLeft()):

                    #Hvis der er zigzag kæde tilsidst
                    if tempNode.getLeft().getRight() != -1:
                        leafnode = tempNode.getLeft().getRight()
                        leafnode.getParent().setRight(-1)
                        self.setLeftRightTree(node, leafnode)

                    else:
                        leafnode = tempNode.getLeft().getLeft()
                        leafnode.getParent().setLeft(-1)
                        self.setLeftRightTree(node, leafnode)
                
                #Hvis noden er den yderste node
                else:
                    leafnode = tempNode.getLeft()

                    leafnode.getParent().setLeft(-1)
                    leafnode.setRight(node.getRight())
                    leafnode.setParent(node.getParent())  
                    node.getParent().setLeft(leafnode)
                    leafnode.decrementHeight()
                    self.balance(leafnode)
            
            #Hvis noden man vil fjerne er den ydereste 
            else:
                    tempNode.getParent().setRight(-1)
                    self.setLeftRightTree(node, tempNode)
    
    #Tjekker om denne node har nogle børn
    def isLeaf(self, node):
        return  node.getLeft() == -1 and  node.getRight() == -1

    # Rebalance

    # Metoder til at ændre barn-forældre relation
    def _setParentChildRight(self, node, parent):
        parent.setRight(node)

        if node != -1:
            if node.getKey() == self.getRoot().getKey():
                self.setRoot(parent)
                parent.setParent(-1)

                print("ny root", self.getRoot().getKey())

    def _setParentChildLeft(self, node, parent):
        parent.setLeft(node)

        #Hvis top noden er roden
        if node != -1:
            if node.getKey() == self.getRoot().getKey():
                self.setRoot(parent)
                parent.setParent(-1)
                
                print("ny root", self.getRoot().getKey())

    # Right rotate
    def rightRotate(self, node):

        #Node er noden i ubalance
        z = node.getParent()
        x = node.getLeft()

        # Hvis grandGrandParent eksisterer
        if z != -1:
            self._setParentChildLeft(x, z)
        
        node.setLeft(x.getRight())
        self._setParentChildRight(node,x)
        
    # Left Rotate
    def leftRotate(self, node):
        z = node.getParent()
        x = node.getRight()

        # Hvis grandgrandParent eksisterer
        if z != -1:
            self._setParentChildRight(x, z)

        node.setRight(x.getLeft())
        self._setParentChildLeft(node, x)

    # Left + Right Rotate
    def leftRightRotate(self, node):
        x = node.getLeft()
        y = x.getRight()

        x.setRight(y.getLeft())
        # Left rotate
        self._setParentChildLeft(y, node)
        self._setParentChildLeft(x, y)

        # Right rotate
        self.rightRotate(node)

    # Right + left Rotate
    def rightLeftRotate(self, node):
        x = node.getRight()
        y = x.getLeft()

        x.setLeft(y.getRight())
        # Left rotate
        self._setParentChildRight(y, node)
        self._setParentChildRight(x, y)

        # left rotate
        self.leftRotate(node)


    # isBalanced
    def isBalanced(self, node):
        return self._isBalanced(node)

    #isBalanced hjælpe metode
    def _isBalanced(self, node):
        # Hvis toppen af træet er nået så er træet er balanceret.
        if node == -1:
            return -1
        if abs(node.heightLeft()-node.heightRight()) <= 1:
            return self._isBalanced(node.getParent())
        else:
            return node

    # find
    def find(self, node):
        return self._find(self.getRoot(), node)
    
    #Find hjælpe metode
    def _find(self, node, nodeToFind):
        if node == -1:
            return -1
        if node.getKey() == nodeToFind.getKey():
            return node
        elif nodeToFind.getKey() > node.getKey():
            return self._find(node.getRight(), nodeToFind)
        else:
            return self._find(node.getLeft(), nodeToFind)

    # print tree
    def inOrderPrint(self):
        self._inOrderPrint(self.getRoot())
    
    #hjælpe metode til print
    def _inOrderPrint(self, node):

        if node.getLeft() != -1:
            self._inOrderPrint(node.getLeft())

        if node.getKey() == self.getRoot().getKey():

            print("root", "n.key: ", node.getKey())
        else:
            print("n.key: ", node.getKey(), " p.key: ", node.getParent().getKey())

        if node.getRight() != -1:
            self._inOrderPrint(node.getRight())


avl = AVL()
n16 = avl.createNode(16, 42)
n15 = avl.createNode(15, 1337)

n44 = avl.createNode(44, 1)
n17 = avl.createNode(17, 2)
n32 = avl.createNode(32, 3)
n78 = avl.createNode(78, 4)
n50 = avl.createNode(50, 5)
n88 = avl.createNode(88, 6)
n48 = avl.createNode(48, 7)
n62 = avl.createNode(62, 8)
n89 = avl.createNode(89, 9)
n63 = avl.createNode(63, 10)
n64 = avl.createNode(64, 10)

avl.setRoot(n44)
avl.insert(n17)
avl.insert(n32)
avl.insert(n48)
avl.insert(n50)
avl.insert(n78)
avl.insert(n88)
avl.insert(n62)
avl.insert(n89)
avl.insert(n63)

avl.inOrderPrint()

print(avl.find(n89).getKey())

#Find en node som ikke er i træet
print(avl.find(n64))

avl.delete(n32)

avl.inOrderPrint()
