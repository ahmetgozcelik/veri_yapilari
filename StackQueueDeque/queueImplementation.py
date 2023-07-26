'''
FIFO mantığıyla çalışır. İlk giren ilk çıkar.
Queue()
enqueue(element)
dequeue()
size()
isEmpty()

'''

class Queue():

    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []
    
    def enqueue(self, element):
        return self.elements.insert(0, element)

    def dequeue(self):
        return self.elements.pop()
    
    def size(self):
        return len(self.elements)

myQueue = Queue()

print(myQueue.isEmpty())

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.size())
print(myQueue.isEmpty())