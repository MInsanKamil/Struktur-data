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
    def __init__(self,sensitive):
        self.nil = Node(0,"nil")
        self.nil.setRed(False)
        self.nil.setLeft(None) 
        self.nil.setRight(None)
        self.root = self.nil
        self.sensitive = sensitive

    def add(self, key, value):
        key = key if self.sensitive == True else key.lower()
        if self.sensitive == False and type(value) == str:
            value = value.lower()
        # Ordinary Binary Search addion
        new_node = Node(key, value)
        new_node.setParent(None)
        new_node.setLeft(self.nil)
        new_node.setRight(self.nil)
        new_node.setRed(True)

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.getKey() < current.getKey():
                current = current.getLeft()
            elif new_node.getKey() > current.getKey():
                current = current.getRight()
            else:
                return

        # Set the parent and add the new node
        new_node.setParent(parent)
        if parent == None:
            self.root = new_node
        elif new_node.getKey() < parent.getKey():
            parent.setLeft(new_node)
        else:
            parent.setRight(new_node)

        # Fix the tree
        self.fix_add(new_node)

    # rotate left at node x
    def rotate_left(self, node):
        y = node.getRight()
        node.setRight(y.getLeft())
        if y.getLeft() != self.nil:
            y.getLeft().setParent(node)

        y.setParent(node.getParent())
        if node.getParent() == None:
            self.root = y
        elif node == node.getParent().getLeft():
            node.getParent().setLeft(y)
        else:
            node.getParent().setRight(y)
        y.setLeft(node)
        node.setParent(y)


    # rotate right at node x
    def rotate_right(self, node):
        y = node.getLeft()
        node.setLeft(y.getRight()) 
        if y.getRight() != self.nil:
            y.getRight().setParent(node)

        y.setParent(node.getParent())
        if node.getParent() == None:
            self.root = y
        elif node == node.getParent().getRight():
            node.getParent().setRight(y)
        else:
            node.getParent().setLeft(y)
        y.setRight(node)
        node.setParent(y)

    def fix_add(self, new_node):
        while self.root != new_node and True == new_node.getParent().getRed():
            if new_node.getParent() == new_node.getParent().getParent().getLeft():
                if new_node.getParent().getParent().getRight().getRed():
                    new_node.getParent().getParent().getRight().setRed(False)
                    new_node.getParent().getParent().setRed(True)
                    new_node.getParent().setRed(False)
                    new_node = new_node.getParent().getParent()
                else:
                    if new_node == new_node.getParent().getRight():
                        self.rotate_left( new_node.getParent() )
                    new_node.getParent().setRed(False)
                    new_node.getParent().getParent().setRed(True)
                    self.rotate_right( new_node.getParent().getParent() )
            else:
                if new_node.getParent().getParent().getLeft().getRed():
                    new_node.getParent().getParent().getLeft().setRed(False)
                    new_node.getParent().getParent().setRed(True)
                    new_node.getParent().setRed(False)
                    new_node = new_node.getParent().getParent()
                else:
                    if new_node == new_node.getParent().getLeft():
                        self.rotate_right( new_node.getParent() )
                    new_node.getParent().setRed(False)
                    new_node.getParent().getParent().setRed(True)
                    self.rotate_left( new_node.getParent().getParent() )
        self.root.setRed(False)

    def maxKeyNode_printHelper(self):
        current = self.root

        # Perulangan untuk mencari node dengan nilai terkecil
        while(current.getRight() is not self.nil):
            current = current.getRight()

        return current


    def minKeyNode_printHelper(self):
        current = self.root

        # Perulangan untuk mencari node dengan nilai terkecil
        while(current.getLeft() is not self.nil):
            current = current.getLeft()

        return current

    def minKeyNode(self, node):
        current = node

        # Perulangan untuk mencari node dengan nilai terkecil
        while(current.getLeft() is not self.nil):
            current = current.getLeft()

        return current
    
    def transplant(self, deletedNode, replacer):
        if deletedNode.getParent() == self.nil:
            self.root = replacer
        elif deletedNode == deletedNode.getParent().getLeft():
            deletedNode.getParent().setLeft(replacer)
        else:
            deletedNode.getParent().setRight(replacer)
        replacer.setParent(deletedNode.getParent()) 


    def delete_fixup(self, node):
        while node != self.root and node.getRed() == False:
            if node == node.getParent().getLeft():
                siblings = node.getParent().getRight()
                if siblings.getRed() == True:
                    siblings.setRed(False)
                    node.getParent().setRed(True)
                    self.rotate_left(node.getParent())
                    siblings = node.getParent().getRight()

                if siblings.getLeft().getRed() == False and siblings.getRight().getRed() == False:
                    siblings.setRed(True)
                    node = node.getParent()

                else:
                    if siblings.getRight().getRed() == False:
                        siblings.getLeft().setRed(False)
                        siblings.setRed(True) 
                        self.rotate_right(siblings)
                        siblings = node.getParent().getRight()

                    siblings.setRed(node.getParent().getRed())
                    node.getParent().setRed(False)
                    siblings.getRight().setRed(False)
                    self.rotate_left(node.getParent())
                    node = self.root

            else:
                siblings = node.getParent().getLeft()
                if siblings.getRed() == True:
                    siblings.setRed(False)
                    node.getParent().setRed(True)
                    self.rotate_right(node.getParent())
                    siblings = node.getParent().getLeft()

                if siblings.getRight().getRed() == False and siblings.getLeft().getRed() == False:
                    siblings.setRed(True)
                    node = node.getParent()

                else:
                    if siblings.getLeft().getRed() == False:
                        siblings.getRight().setRed(False)
                        siblings.setRed(True)
                        self.rotate_left(siblings)
                        siblings = node.getParent().getLeft()

                    siblings.setRed(node.getParent().getRed())
                    node.getParent().setRed(False)
                    siblings.getLeft().setRed(False)
                    self.rotate_right(node.getParent())
                    node = self.root

        node.setRed(False)

    def delete(self, key):
        key = key if self.sensitive == True else key.lower()
        if self.search(self.root,key):
            deletedNode = self.search(self.root,key)
        else:
            print(f"Tidak bisa menghapus, key:'{key}' tidak ada")
            return
        x = None
        replacer_orignal_color = deletedNode.getRed()
        if deletedNode.getLeft() == self.nil:
            x = deletedNode.getRight()
            self.transplant(deletedNode, deletedNode.getRight())

        elif deletedNode.getRight() == self.nil:
            x = deletedNode.getLeft()
            self.transplant(deletedNode, deletedNode.getLeft())

        else:
            replacer = self.minKeyNode(deletedNode.getRight())
            replacer_orignal_color = replacer.getRed()
            x = replacer.getRight()
            if replacer.getParent()== deletedNode:
                x.setParent(deletedNode)

            else:
                self.transplant(replacer, replacer.getRight())
                replacer.setRight(deletedNode.getRight())
                replacer.getRight().setParent(replacer)

            self.transplant(deletedNode, replacer)
            replacer.setLeft(deletedNode.getLeft())
            replacer.getLeft().setParent(replacer)
            replacer.setRed(deletedNode.getRed())

        if replacer_orignal_color == False:
            self.delete_fixup(x)

    def edit(self, key, value):
        key = key if self.sensitive == True else key.lower()
        if self.sensitive == False and type(value) == str:
            value = value.lower()
        self.search(self.root,key).setValue(value)


    def get(self, key):
        key = key if self.sensitive == True else key.lower()
        if self.search(self.root,key):
            return self.search(self.root,key).getValue()
        else:
            return f"Key:'{key}' tidak ada"

    def search(self,node, key):
            key = key if self.sensitive == True else key.lower()
            if key < node.getKey():
                if node.getLeft() is self.nil:
                    return False 
                return self.search(node.getLeft(),key)
            elif key > node.getKey():
                if node.getRight() is self.nil:
                    return False
                return self.search(node.getRight(),key)
            else:
                return node

    def printHashMap(self):
        return self.printHelper(self.root)
    
    def printHelper(self,node):
        if node:
            self.printHelper(node.getLeft())
            if type(node.getKey()) == str and type(node.getValue()) == str:
                if node == self.minKeyNode_printHelper() and node.getRight() == self.nil and node.getLeft() == self.nil and node == self.root:
                    txt3 = "{}'{}': '{}'".format("{",node.getKey(),node.getValue())
                    print(txt3, end="}\n")
                elif node == self.minKeyNode_printHelper():
                    txt3 = "{}'{}': '{}'".format("{",node.getKey(),node.getValue())
                    print(txt3, end=", ")
                elif node == self.maxKeyNode_printHelper():
                    print(f"'{node.getKey()}': '{node.getValue()}'", end="}\n")
                else:
                    print(f"'{node.getKey()}': '{node.getValue()}'", end=", ")
            elif type(node.getKey()) == str and type(node.getValue()) != str:
                if node == self.minKeyNode_printHelper():
                    txt3 = "{}'{}': {}".format("{",node.getKey(),node.getValue())
                    print(txt3, end=", ")
                elif node == self.maxKeyNode_printHelper():
                    print(f"'{node.getKey()}': {node.getValue()}", end="}\n")
                else:
                    print(f"'{node.getKey()}': {node.getValue()}", end=", ")
            self.printHelper(node.getRight())

Device = HashMap(True)
print("add('Nama Perangkat', 'Redmi Note 8'):")
Device.add("Nama Perangkat", "Redmi Note 8")
Device.printHashMap()
print()
print("add('ROM(GB)',64):")
Device.add("ROM(GB)",64)
Device.printHashMap()
print()
print("add('Versi MIUI', 12):")
Device.add("Versi MIUI", 12)
Device.printHashMap()
print()
print("add('Versi Android', 11):")
Device.add("Versi Android", 11)
Device.printHashMap()
print()
print("add('RAM(GB)', 4):")
Device.add("RAM(GB)", 4)
Device.printHashMap()
print()
print("delete('CPU'):")
Device.delete("CPU")
print()
print("delete('Versi Android'):")
Device.delete("Versi Android")
Device.printHashMap()
print()
print("Device.get('RAM(GB)'):")
print(Device.get("RAM(GB)"))
print()
print("Device.get('Versi Android'):")
print(Device.get("Versi Android"))