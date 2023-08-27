import sys
sys.setrecursionlimit(3333)

class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None
    def setValue(self, value):
        self.__value = value
    def setNext(self, next):
        self.__next = next
    def setPrev(self, prev):
        self.__prev = prev
    def getValue(self):
        return self.__value
    def getNext(self):
        return self.__next
    def getPrev(self):
        return self.__prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    
    
    # Untuk menambahkan node dibagian akhir linked list
    def add_end(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            n = self.head
            while n.getNext() != None:
                n = n.getNext()
            n.setNext(new_node)
            new_node.setPrev(n)
            self.tail = new_node

    # Untuk menampilkan nilai dari node yang ada di linked list
    def printLL(self):
        n = self.head
        while n != None:
            if n.getNext() == None:
                print(n.getValue())
            else:
                print(n.getValue(),end=",")
            n = n.getNext()
    # Untuk menampilkan nilai dari node yang ada di linked list dimulai dari tempHead yang dimasukkan pada parameter
    def printTempHead(self,tempHead):
        n = tempHead
        while n != None:
            if n.getNext() == None:
                print(n.getValue())
            else:
                print(n.getValue(),end=",")
            n = n.getNext()

    # Untuk menggabungkan dua linked list, sekaligus mengurutkan nilai-nilainya dari yang terkecil sampai terbesar
    def merge(self, first, second):
            if second is None:
                return first
            if first is None:
                return second 
            if first.getValue() < second.getValue():
                first.setNext(self.merge(first.getNext(), second))
                first.getNext().setPrev(first)
                first.setPrev(None)
                self.printTempHead(first)
                print()
                return first
            else:
                second.setNext(self.merge(first, second.getNext()))
                second.getNext().setPrev(second)
                second.setPrev(None)
                self.printTempHead(second)
                print()
                return second

    # Untuk membagi linked list 
    def split(self, tempHead):
            fast = slow =  tempHead
            while(True):
                if fast.getNext() is None:
                    break
                if fast.getNext().getNext() is None:
                    break
                fast = fast.getNext().getNext()
                slow = slow.getNext()  
            temp = slow.getNext()
            slow.setNext(None)
            return temp
    
    # untuk mengurutkan nilai-nilai dari node yang ada di linked list dari yang terkecil sampai yang terbesar
    def mergeSort(self, tempHead):
            if tempHead is None: 
                return tempHead
            if tempHead.getNext() is None:
                return tempHead
    
            print("Split")
            second = self.split(tempHead)
            print("First:", end="")
            self.printTempHead(tempHead)
            print("Second:", end="")
            self.printTempHead(second)
            print()
            
            tempHead = self.mergeSort(tempHead)
            second = self.mergeSort(second)

            print("Merge")
            print("First Linked List:", end="")
            self.printTempHead(tempHead)
            print("First:", end="")
            print(tempHead.getValue())
            print("Second Linked List:", end="")
            self.printTempHead(second)
            print("Second:", end="")
            print(second.getValue())
            return self.merge(tempHead, second)
            

    
            

print("Program Pengurutan")
value = str(input("Masukkan angka-angka acak(pisahkan dengan koma):"))
try:
    number = value.split(",")
    myLL = LinkedList()
    if len(number)>= 3 and len(number) <= 3333:
        for x in number:
            myLL.add_end(int(x))
        myLL.printLL()
        myLL.head = myLL.mergeSort(myLL.head)
        print("Output:")
        myLL.printLL()
    elif len(number) < 3:
        print("input minimal sebanyak 3 angka")
    else:
        print("input maksimal sebanyak 3333 angka")
except:
    print("input harus berupa angka-angka yang dipisahkan dengan koma")