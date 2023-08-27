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

class RBTree:
    def __init__(self):
        self.nil = Node(0,"nil")
        self.nil.setRed(False)
        self.nil.setLeft(None) 
        self.nil.setRight(None)
        self.root = self.nil

    def insert(self, key, value):
        # Ordinary Binary Search Insertion
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

        # Set the parent and insert the new node
        new_node.setParent(parent)
        if parent == None:
            self.root = new_node
        elif new_node.getKey() < parent.getKey():
            parent.setLeft(new_node)
        else:
            parent.setRight(new_node)

        # Fix the tree
        self.fix_insert(new_node)

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

    def fix_insert(self, new_node):
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
        if self.search(key):
            deletedNode = self.search(key)
        else:
            print(f"Tidak bisa menghapus, key:{key} tidak ada")
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
    
    def exist(self, key):
        if self.root == None:
            print(f"Tree Kosong, key:{key} Tidak Ada")
        elif self.search(key):
            print(f"key:{key} Ada")
            return True
        else:
            print(f"key:{key} Tidak Ada")
            return False

    def edit(self, key, value):
        if self.exist(key):
            temp = self.search(key).getValue()
            self.search(key).setValue(value)
            print(f"Red Black Tree dengan key:{key}, valuenya telah diubah dari {temp} menjadi {self.search(key).getValue()}")
        else:
            print("Key tidak ditemukan, tidak bisa mengupdate value")


    def search_helper(self,node, key):
        if key < node.getKey():
            if node.getLeft() is None:
                return False 
            return self.search_helper(node.getLeft(),key)
        elif key > node.getKey():
            if node.getRight() is None:
                return False
            return self.search_helper(node.getRight(),key)
        else:
            return node

    def search(self, key):
        return self.search_helper(self.root,key)

    def height(self,node):
        return 1 + max(self.height(node.getLeft()), self.height(node.getRight())) if node else -1

    def PrintTree(self):  
        nlevels = self.height(self.root)
        width =  pow(2,nlevels+1)

        q=[(self.root,0,width,'c')]
        levels=[]

        while(q):
            node,level,x,align= q.pop(0)
            if node:            
                if len(levels)<=level:
                    levels.append([])
            
                levels[level].append([node,level,x,align])
                seg= width//(pow(2,level+1))
                q.append((node.getLeft(),level+1,x-seg,'l'))
                q.append((node.getRight(),level+1,x+seg,'r'))

        for i,l in enumerate(levels):
            pre=0
            preline=0
            linestr=''
            pstr=''
            seg= width//(pow(2,i+1))
            for n in l:
                valstr= str(n[0].getKey())
                if n[3]=='r':
                    linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                    preline = n[2] 
                if n[3]=='l':
                    linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
                    preline = n[2] + seg + seg//2
                valstrC = "\033[0;31m"+ valstr +"\033[0m" if n[0].getRed() == True else valstr 
                pstr+=' '*(n[2]-pre-len(valstr))+ valstrC
                pre = n[2]
            print(linestr)
            print(pstr)

r = RBTree() 
r.insert(1, "Satu")
print("insert(1):")
r.PrintTree()  
r.insert(2, "Dua")
print("insert(2):")
r.PrintTree()    
r.insert(3, "Tiga")
print("insert(3):")
r.PrintTree()    
r.insert(4, "Empat")
print("insert(4):")
r.PrintTree()    
r.insert(5, "Lima")
print("insert(5):")
r.PrintTree()    
r.insert(6, "Enam")
print("insert(6):")
r.PrintTree()    
r.insert(7, "Tujuh")
print("insert(7):")
r.PrintTree()    
r.insert(8, "Delapan")
print("insert(8):")
r.PrintTree()
print("\033[0;31m"+f"delete(5):"+"\033[0m")
print("Before:")
r.PrintTree()
print()
print("After:")
r.delete(5)
r.PrintTree()
print() 
print("\033[0;31m"+"exist(10):"+"\033[0m")
r.exist(10)
print()
print("\033[0;31m"+"edit(3,'Three'):"+"\033[0m")
r.edit(3,'Three') 
print()


