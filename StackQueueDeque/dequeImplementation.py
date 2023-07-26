'''

Deque()

addRight()
addLeft()

removeRight()
removeLeft()

isEmpty()
size()

'''

class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addRight(self, item):
        return self.items.append(item)
    
    def addLeft(self, item):
        return self.items.insert(0, item)
    
    def removeRight(self):
        return self.items.pop()
    
    def removeLeft(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    

myDeque = Deque()
myDeque.addRight(1)
myDeque.addRight(2)
myDeque.addRight(3)
myDeque.addLeft(4)
myDeque.addLeft(5)

print(myDeque.size())
print(myDeque.isEmpty())
print(myDeque.removeLeft())
print(myDeque.removeLeft())
print(myDeque.removeLeft())
print(myDeque.removeRight())
print(myDeque.removeRight())
print(myDeque.isEmpty())