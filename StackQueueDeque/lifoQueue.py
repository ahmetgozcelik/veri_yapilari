# #LIFO
# from queue import LifoQueue
# lifoQueue = LifoQueue()
# lifoQueue.put(1)
# lifoQueue.put(2)
# lifoQueue.put(3)

# print("sa")
# print(lifoQueue.get())
# # output: 3


# FIFO
# from queue import Queue
# myQueue = Queue()
# myQueue.put(1)
# myQueue.put(50)
# myQueue.put(100)
# print(myQueue.get())
# #output: 1


from collections import deque
myDeque = deque()
myDeque.append(1)
myDeque.append(2)
myDeque.append(3)

print(myDeque)
# output: deque([1, 2, 3])
myDeque.appendleft(4)
print(myDeque)
# output: deque([4, 1, 2, 3])