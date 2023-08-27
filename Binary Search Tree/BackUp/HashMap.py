class Node:
    def __init__(self, key, value):
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__key = key
        self.__isRed = False
        self.__value = value
    def setRed(self, boolean):
        self.__isRed = boolean
    def setParent(self, parent):
        self.__parent = parent
    def setLeft(self,left):
        self.__left = left
    def setRight(self,right):
        self.__right = right
    def setKey(self, key):
        self.__key = key
    def setValue(self, value):
        self.__value = value
    def getRed(self):
        return self.__isRed
    def getParent(self):
        return self.__parent
    def getLeft(self):
        return self.__left
    def getRight(self):
        return self.__right
    def getKey(self):
        return self.__key
    def getValue(self):
        return self.__value

class HashMap:
    def __init__(self, sensitive):
        self.root = None
        self.sensitive = sensitive

    def add( self,key,value ):
        key = key if self.sensitive == True else key.lower()
        if ( self.root == None ):
            self.root = Node( key , value )
            return True
        else:
            return self.add_root_not_None( self.root, key, value )
    
    def add_root_not_None(self, node, key, value ):
        if ( node.getKey() < key ):
            if ( None == node.getRight() ):
                node.setRight(  Node( key, value ) )
                node.getRight().setParent( node )
                node.getRight().setRed(True)
                self.balancing( node.getRight() )
                return True
            else:
                return self.add_root_not_None( node.getRight(), key, value )
        elif key < node.getKey():
            if ( None == node.getLeft() ):
                node.setLeft(  Node( key, value ) )
                node.getLeft().setParent( node )
                node.getLeft().setRed(True)
                self.balancing( node.getLeft() )
                return True
            else:
                return self.add_root_not_None( node.getLeft(), key, value )
        return False
    
    def balancing(self, node ):
        if ( None != node.getParent() and None != node.getParent().getParent() ):
            if ( node.getParent() == node.getParent().getParent().getRight() ):
                if ( None != node.getParent().getParent().getLeft() and node.getParent().getParent().getLeft().getRed() ):
                    node.getParent().getParent().getLeft().setRed( False )
                    node.getParent().getParent().setRed( True )
                    node.getParent().setRed( False )
                    self.balancing( node.getParent().getParent() )
                else:
                    if ( node == node.getParent().getLeft() ):
                        node = node.getParent()
                        self.rotateToRight( node )
                    
                    node.getParent().setRed( False )
                    node.getParent().getParent().setRed( True )
                    self.rotateToLeft( node.getParent().getParent() )
                
            else:
                if ( None != node.getParent().getParent().getRight() and node.getParent().getParent().getRight().getRed() ):
                    node.getParent().getParent().getRight().setRed( False )
                    node.getParent().getParent().setRed( True )
                    node.getParent().setRed( False )
                    self.balancing( node.getParent().getParent() )
                else:
                    if ( node == node.getParent().getRight() ):
                        node = node.getParent()
                        self.rotateToLeft( node )
                    
                    node.getParent().setRed( False )
                    node.getParent().getParent().setRed( True )
                    self.rotateToRight( node.getParent().getParent() )
        self.root.setRed( False )
    
    def rotateToRight( self, node ):
        if ( self.root == node ):
            self.root = node.getLeft()
        elif ( node == node.getParent().getRight() ):
            node.getParent().setRight( node.getLeft() )
        else:
            node.getParent().setLeft( node.getLeft() )
        node.getLeft().setParent( node.getParent() )
        node.setParent( node.getLeft() )
        node.setLeft( node.getLeft().getRight() )
        node.getParent().setRight( node )
        if ( None != node.getLeft() ):
            node.getLeft().setParent( node )
    
    def rotateToLeft( self, node ):
        if ( self.root == node ):
            self.root = node.getRight()
        elif ( node == node.getParent().getRight() ):
            node.getParent().setRight( node.getRight() )
        else:
            node.getParent().setLeft( node.getRight() )
        node.getRight().setParent( node.getParent() )
        node.setParent( node.getRight() )
        node.setRight( node.getRight().getLeft() )
        node.getParent().setLeft( node )
        if ( None != node.getRight() ):
            node.getRight().setParent( node )

    def edit(self, key, value):
        key = key if self.sensitive == True else key.lower()
        self.search(self.root,key).setValue(value)

    def get(self, key):
        key = key if self.sensitive == True else key.lower()
        return self.search(self.root,key).getValue()

    def search(self,node, key):
            key = key if self.sensitive == True else key.lower()
            if key < node.getKey():
                if node.getLeft() is None:
                    return False 
                return self.search(node.getLeft(),key)
            elif key > node.getKey():
                if node.getRight() is None:
                    return False
                return self.search(node.getRight(),key)
            else:
                return node
                
    def maxValueNode(self):
        current = self.root

        # Perulangan untuk mencari node dengan nilai terkecil
        while(current.getRight() is not None):
            current = current.getRight()

        return current

    def minValueNode(self):
        current = self.root

        # Perulangan untuk mencari node dengan nilai terkecil
        while(current.getLeft() is not None):
            current = current.getLeft()

        return current

    def printHashMap(self):
        return self.printHelper(self.root)
    
    def printHelper(self,node):
        if node:
            self.printHelper(node.getLeft())
            if type(node.getKey()) == str and type(node.getValue()) == str:
                if node == self.minValueNode():
                    txt3 = "{}'{}': '{}'".format("{",node.getKey(),node.getValue())
                    print(txt3, end=", ")
                elif node == self.maxValueNode():
                    print(f"'{node.getKey()}': '{node.getValue()}'", end="}")
                else:
                    print(f"'{node.getKey()}': '{node.getValue()}'", end=", ")
            elif type(node.getKey()) == str and type(node.getValue()) != str:
                if node == self.minValueNode():
                    txt3 = "{}'{}': {}".format("{",node.getKey(),node.getValue())
                    print(txt3, end=", ")
                elif node == self.maxValueNode():
                    print(f"'{node.getKey()}': {node.getValue()}", end="}")
                else:
                    print(f"'{node.getKey()}': {node.getValue()}", end=", ")
            self.printHelper(node.getRight())


Hm = HashMap(True) 
Hm.add("Orange", "Jeruk")  
Hm.add("Red",True)
Hm.add("Black", False)
Hm.add("Purple", "Anggur")
Hm.add("Yellow", "Kuning")
Hm.printHashMap()
# r.add("gokss", "Empat")
# print("\033[0;31m"+"add(4):"+"\033[0m")
# PrintTree(r.root)  
# r.add("", "Lima")
# print("\033[0;31m"+"add(5):"+"\033[0m")
# PrintTree(r.root) 
# r.add("hoho", "Enam")
# print("\033[0;31m"+"add(6):"+"\033[0m")
# PrintTree(r.root)  
# r.add("fufu", "Tujuh")
# print("\033[0;31m"+"add(7):"+"\033[0m")
# PrintTree(r.root) 
# r.add("haha", "Delapan")
# print("\033[0;31m"+"add(8):"+"\033[0m")
# PrintTree(r.root)
# print()
# print("\033[0;31m"+"exist(10):"+"\033[0m")
# r.exist(10)
# print()
# print("\033[0;31m"+"edit(7,'TUJUHHHH'):"+"\033[0m")
# r.edit(7,"TUJUHHHH") 
# print()