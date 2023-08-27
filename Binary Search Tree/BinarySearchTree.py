# Kelompok 4:
# Guntur Wisnu Saputra_11211042
# Muhammad Insan Kamil_11211058
# Muhammad Ricky Zakaria_11211062	
# Ramadhan Djibran Sanjaya_11211070	
# Rangga Hermawan_11211071	
# Rendy Pernanda_11211074	

class Node:
    # Method yang akan dieksekusi ketika membuat objek Node
    def __init__(self, key, value):
        self.__left = None 
        self.__right = None
        self.__key = key
        self.__value = value
    # Method untuk mengupdate nilai dari variabel private "left"
    def setLeft(self,left):
        self.__left = left
    # Method untuk mengupdate nilai dari variabel private "right"
    def setRight(self,right):
        self.__right = right
    # Method untuk mengupdate nilai dari variabel private "key"
    def setkey(self, key):
        self.__key = key
    def setValue(self, value):
        self.__value = value
    # Method untuk mendapatkan nilai dari variabel private "left"
    def getLeft(self):
        return self.__left
    # Method untuk mendapatkan nilai dari variabel private "right"
    def getRight(self):
        return self.__right
    # Method untuk mendapatkan nilai dari variabel private "key"
    def getkey(self):
        return self.__key
    def getValue(self):
        return self.__value


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root == None:
            self.root = Node(key, value)
        else:
            self.insert_helper(self.root, key, value)

    # Fungsi untuk membantu menyelipkan node dibagian tertentu sesuai dengan konsep Binary Search Tree(BST)
    def insert_helper(self,node, key, value):
        # Untuk mengecek apakah node-nya kosong atau tidak, sekaligus sebagai batas dari perulangan yang dilakukan oleh fungsi rekursif
        if node is None:
            return Node(key, value)
        # Jika node tidak kosong
        else:
            # Jika nilai node yang ingin diinsert sama dengan nilai dari node, maka return node, karena dalam Binary Search Tree tidak bolah ada nilai yang duplikat
            if node.getkey() == key:
                return node
            # Jika nilai node yang ingin diinsert lebih besar dari nilai node, insert node tersebut ke bagian kanan node
            elif node.getkey() < key:
                node.setRight(self.insert_helper(node.getRight(), key, value))
            # Jika nilai node yang ingin diinsert lebih kecil dari nilai node, insert node tersebut ke bagian kiri node
            else:
                node.setLeft(self.insert_helper(node.getLeft(), key, value))
        return node

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
                valstr= str(n[0].getkey())
                if n[3]=='r':
                    linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                    preline = n[2] 
                if n[3]=='l':
                    linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
                    preline = n[2] + seg + seg//2
                pstr+=' '*(n[2]-pre-len(valstr))+ valstr
                pre = n[2]
            print(linestr)
            print(pstr)

    # Fungsi untuk menampilkan nilai-nilai dari Node pada Binary Search Tree dari yang terkecil sampai yang terbesar
    def inorder_helper(self,node):
        if node:
            self.inorder_helper(node.getLeft())
            print(node.getkey(), end=" ")
            self.inorder_helper(node.getRight())

    def inorder(self):
        return self.inorder_helper(self.root)

    # Fungsi untuk mencari node dengan nilai terkecil
    def minkeyNode(self,node):
        current = node

        # Perulangan untuk mencari node dengan nilai terkecil
        while(current.getLeft() is not None):
            current = current.getLeft()

        return current

    # Fungsi untuk menghapus Node berdasarkan key
    def deleteNode_helper(self,node, key):
    
        # Untuk mengecek apakah node-nya kosong atau tidak, sekaligus sebagai batas dari perulangan yang dilakukan oleh fungsi rekursif
        if node is None:
            return node
    
        # Jika nilai node yang ingin dihapus kurang dari nilai node, maka bagian kiri node akan diatur untuk menghapus node tersebut
        if key < node.getkey():
            node.setLeft(self.deleteNode_helper(node.getLeft(), key))
    
        # Jika nilai node yang ingin dihapus lebih dari nilai node, maka bagian kanan node akan diatur untuk menghapus node tersebut
        elif(key > node.getkey()):
            node.setRight(self.deleteNode_helper(node.getRight(), key))
        
        # Jika nilai node yang ingin dihapus sama dengan nilai node, maka node akan dihapus, lalu bagian kanan node atau bagian kiri node akan diatur untuk menggantikan node
        else:
            # Kondisi jika node hanya memiliki satu daun(leaf) atau tidak memiliki daun(leaf)
            # Jika node tidak memiliki daun, maka akan di return nilai None
            # Jika bagian kiri node kosong(tidak memiliki daun dibagian kiri), maka bagian kanan node yang akan menggantikan node yang telah dihapus
            if node.getLeft() is None:
                temp = node.getRight()
                node = None
                return temp
            # Jika bagian kanan node kosong(tidak memiliki daun dibagian kanan), maka bagian kiri node yang akan menggantikan node yang telah dihapus
            elif node.getRight() is None:
                temp = node.getLeft()
                node = None
                return temp


            # Kondisi jika node memiliki dua daun(leaf)
            # maka dicari node dengan nilai terkecil dibagian kanan node, kemudian node tersebutlah yang akan menggantikan node yang telah dihapus
            temp = self.minkeyNode(node.getRight())
            node.setkey(temp.getkey())
            node.setRight(self.deleteNode_helper(node.getRight(), temp.getkey())) 
    
        return node

    def deleteNode(self,key):
        return self.deleteNode_helper(self.root,key)




r = BSTree()
print()
print("\033[0;31m"+"Binary Search Tree"+"\033[0m")
print("insert(5, 'Lima'): ")
r.insert(5, "Lima")
r.PrintTree()
print("insert(3, 'Tiga'): ")
r.insert(3, "Tiga")
r.PrintTree()
print("insert(2, 'Dua'): ")
r.insert(2, "Dua")
r.PrintTree()
print("insert(4, 'Empat'): ")
r.insert(4, "Empat")
r.PrintTree()
print("insert(7, 'Tujuh'): ")
r.insert(7, "Tujuh")
r.PrintTree()
print("insert(6, 'Enam'): ")
r.insert(6, "Enam")
r.PrintTree()
print("insert(8, 'Delapan'): ")
r.insert(8, "Delapan")
r.PrintTree()
print("Inorder")
r.inorder()
print("\n")
print("\033[0;31m"+"deleteNode(5):"+"\033[0m")
print("Before:")
r.PrintTree()
print("After:")
r.deleteNode(5)
r.PrintTree()