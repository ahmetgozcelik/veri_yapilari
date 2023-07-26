#Singly Linked List
class Node():

    def __init__(self, value):
        self.value = value
        self.nextNode = None

firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

print(firstNode.nextNode.value)
print(firstNode.nextNode.nextNode.value)

#Doubly Linked List

class DoublyNode():

    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

x = DoublyNode(10)
y = DoublyNode(20)
z = DoublyNode(30)

x.nextNode = y
y.prevNode = x
y.nextNode = z
z.prevNode = y

print(x.nextNode.nextNode.value)
print(z.prevNode.prevNode.value)