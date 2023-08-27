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
        self.root = None

    def add( self,key,value ):
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

    def minValueNode(self, node):
        current = node

        # Perulangan untuk mencari node dengan nilai terkecil
        while(current.getLeft() is not None):
            current = current.getLeft()

        return current
    
    def transplant(self, deletedNode, replacer):
        if deletedNode.getParent() == None:
            self.root = replacer
        elif deletedNode == deletedNode.getParent().getLeft():
            deletedNode.getParent().setLeft(replacer)
        else:
            deletedNode.getParent().setRight(replacer)
        if replacer != None:
            replacer.setParent(deletedNode.getParent()) 


    def delete_fixup(self, node):
        if node == None:
            return
        while node != self.root and node.getRed() == False:
            if node == node.getParent().getLeft():
                siblings = node.getParent().getRight()
                if siblings.getRed() == True:
                    siblings.setRed(False)
                    node.getParent().setRed(True)
                    self.left_rotate(node.getParent())
                    siblings = node.getParent().getRight()

                if siblings.getLeft().getRed() == False and siblings.getRight().getRed() == False:
                    siblings.setRed(True)
                    node = node.getParent()

                else:
                    if siblings.getRight().getRed() == False:
                        siblings.getLeft().setRed(False)
                        siblings.setRed(True) 
                        self.right_rotate(siblings)
                        siblings = node.getParent().getRight()

                    siblings.setRed(node.getParent().getRed())
                    node.getParent().setRed(False)
                    siblings.getRight().setRed(False)
                    self.left_rotate(node.getParent())
                    node = self.root

            else:
                siblings = node.getParent().getLeft()
                if siblings.getRed() == True:
                    siblings.setRed(False)
                    node.getParent().setRed(True)
                    self.right_rotate(node.getParent())
                    siblings = node.getParent().getLeft()

                if siblings.getRight().getRed() == False and siblings.getLeft().getRed() == False:
                    siblings.setRed(True)
                    node = node.getParent()

                else:
                    if siblings.getLeft().getRed() == False:
                        siblings.getRight().setRed(False)
                        siblings.setRed(True)
                        self.left_rotate(siblings)
                        siblings = node.getParent().getLeft()

                    siblings.setRed(node.getParent().getRed())
                    node.getParent().setRed(False)
                    siblings.getLeft().setRed(False)
                    self.right_rotate(node.getParent())
                    node = self.root

        node.setRed(False)

    def delete(self, key):
        deletedNode = search(self.root,key)
        child = None
        replacer_orignal_color = deletedNode.getRed()
        if deletedNode.getLeft() == None:
            child = deletedNode.getRight()
            self.transplant(deletedNode, deletedNode.getRight())

        elif deletedNode.getRight() == None:
            child = deletedNode.getLeft()
            self.transplant(deletedNode, deletedNode.getLeft())

        else:
            replacer = self.minValueNode(deletedNode.getRight())
            replacer_orignal_color = replacer.getRed()
            child = replacer.getRight()
            if replacer.getParent()== deletedNode and child != None:
                child.setParent(deletedNode)

            else:
                self.transplant(replacer, replacer.getRight())
                replacer.setRight(deletedNode.getRight())
                if replacer.getRight() != None:
                    replacer.getRight().setParent(replacer)

            self.transplant(deletedNode, replacer)
            replacer.setLeft(deletedNode.getLeft())
            replacer.getLeft().setParent(replacer)
            replacer.setRed(deletedNode.getRed())

        if replacer_orignal_color == False:
            self.delete_fixup(child)


    def exist(self, key):
        if self.root == None:
            print(f"Tree Kosong, key:{key} Tidak Ada")
        elif search(self.root,key):
            print(f"key:{key} Ada")
            return True
        else:
            print(f"key:{key} Tidak Ada")
            return False

    def edit(self, key, value):
        if self.exist(key):
            temp = search(self.root,key).getValue()
            search(self.root,key).setValue(value)
            print(f"Red Black Tree dengan key:{key}, valuenya telah diubah dari {temp} menjadi {search(self.root,key).getValue()}")
        else:
            print("Key tidak ditemukan, tidak bisa mengupdate value")

def search(node, key):
        if key < node.getKey():
            if node.getLeft() is None:
                return False 
            return search(node.getLeft(),key)
        elif key > node.getKey():
            if node.getRight() is None:
                return False
            return search(node.getRight(),key)
        else:
            return node

def PrintTree(root):
    def height(root):
        return 1 + max(height(root.getLeft()), height(root.getRight())) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
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
            keystr= str(n[0].getKey())
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            keystrC = "\033[0;31m"+ keystr +"\033[0m" if n[0].getRed() == True else keystr
            pstr+=' '*(n[2]-pre-len(keystr))+ keystrC
            pre = n[2]
        print(linestr)
        print(pstr)    

r = RBTree() 
r.add(1, "Satu")
print("\033[0;31m"+"add(1):"+"\033[0m")
PrintTree(r.root)  
r.add(2, "Dua")
print("\033[0;31m"+"add(2):"+"\033[0m")
PrintTree(r.root)  
r.add(3, "Tiga")
print("\033[0;31m"+"add(3):"+"\033[0m")
PrintTree(r.root)
r.add(4, "Empat")
print("\033[0;31m"+"add(4):"+"\033[0m")
PrintTree(r.root)
r.add(5, "Lima")
print("\033[0;31m"+"add(5):"+"\033[0m")
PrintTree(r.root)
r.add(6, "Enam")
print("\033[0;31m"+"add(6):"+"\033[0m")
PrintTree(r.root)
r.add(7, "Tujuh")
print("\033[0;31m"+"add(7):"+"\033[0m")
PrintTree(r.root)
r.add(8, "Delapan")
print("\033[0;31m"+"add(8):"+"\033[0m")
PrintTree(r.root)
print("\033[0;31m"+f"delete(5):"+"\033[0m")
print("Before:")
PrintTree(r.root)
print()
print("After:")
r.delete(5)
PrintTree(r.root)
print()
print("\033[0;31m"+"exist(10):"+"\033[0m")
r.exist(10)
print()
print("\033[0;31m"+"edit(3,'Three'):"+"\033[0m")
r.edit(3,'Three') 
print()
    