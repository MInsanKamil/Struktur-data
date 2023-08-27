class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
    # Untuk mengupdate nilai variabel private "value"
    def setValue(self, value):
        self.__value = value
    # Untuk mengupdate nilai variabel private "next"
    def setNext(self, next):
        self.__next = next
    # Untuk mendapatkan nilai variabel private "value"
    def getValue(self):
        return self.__value
    # Untuk mendapatkan nilai variabel private "next"
    def getNext(self):
        return self.__next

class Queue:
    def __init__(self):
        self.first =  None
    # memastikan apakah  masih ada Node yang bisa di pop
    def hasPop(self):
        return self.first != None

    # Method untuk menambahkan Node dibagian akhir
    def push(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
        else:
            n = self.first
            while n.getNext() != None:
                n = n.getNext()
            n.setNext(new_node)
    # method mengambil node dari depan
    def pop(self):
        if self.hasPop():
            self.first = self.first.getNext()
    # Method untuk menampilkan nilai dari Node yang ada di queue
    def printQ(self):
        n = self.first
        while n != None:
            print(n.getValue(), "-->", end=" ")
            n = n.getNext()
        print("None")

print()
print("Queue")
myQueue = Queue()
print("Output Method push('A'):")
myQueue.push('A')
myQueue.printQ()
print("Output Method push('P'):")
myQueue.push('P')
myQueue.printQ()
print("Output Method push('E'):")
myQueue.push('E')
myQueue.printQ()
print("Output Method push('L'):")
myQueue.push('L')
myQueue.printQ()
print()
print("Pop Queue")
myQueue.printQ()
while myQueue.hasPop():
    print("Output Method pop():")
    myQueue.pop() 
    myQueue.printQ()
print()

