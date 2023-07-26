'''
Stack()

push(item)
pop()
showLast()
size()
isEmpty()

'''

class Stack():

    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []
    
    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def showLast(self):
        return self.elements[-1]
    
myStack = Stack()
print(myStack.isEmpty())

myStack.push(10)
myStack.push(20)
myStack.push(30)
print(myStack.showLast())

myStack.push("a")
print(myStack.showLast())

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.isEmpty())