class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
    def setValue(self, value):
        self.__value = value
    def setNext(self, next):
        self.__next = next
    def getValue(self):
        return self.__value
    def getNext(self):
        return self.__next

class Stack:
    def __init__(self):
        self.first =  None
    def hasPop(self):
        # memastikan apakah list masih bisa di pop
        return self.first != None
    def push(self, value):
        # menyimpan Node
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
        else:
            new_node.setNext(self.first)
            self.first = new_node
    def pop(self):
        # mengambil node
        if self.hasPop():
            self.first = self.first.getNext()
    def printS(self):
        n = self.first
        while n != None:
            print(n.getValue(), "-->", end=" ")
            n = n.getNext()
        print("None")


myStack = Stack()
print()
print("Stack")
print("Output Method push('A'):")
myStack.push('A')
myStack.printS()
print("Output Method push('P'):")
myStack.push('P')
myStack.printS()
print("Output Method push('E'):")
myStack.push('E')
myStack.printS()
print("Output Method push('L'):")
myStack.push('L')
myStack.printS()
print()
print("Pop Stack")
myStack.printS()
while myStack.hasPop():
    print("Output Method pop():")
    myStack.pop() 
    myStack.printS()
print()