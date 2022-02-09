import os, sys
sys.path.append(os.getcwd())

from Arrays.array import Array
from Stacks_and_Queues.queue_int import Queue

class ArrayQueue(Queue):

    def __init__(self, capacity=10):
        self.array = Array(capacity)

    def getSize(self):
        return self.array.getSize()

    def isEmpty(self):
        return self.array.isEmpty()
    
    def getCapacity(self):
        return self.array.getCapacity()

    def enqueue(self, e):
        return self.array.addLast(e)
    
    def dequeue(self):
        return self.array.removeFirst()
    
    def getFront(self):
        return self.array.getFirst()

    def __str__(self):
        return str('<array_queue> :{} '.format(self.array))
    

queue = ArrayQueue()
for i in range(10):
    queue.enqueue(i)
    print(queue.__str__())

    if i % 3 == 2:
        queue.dequeue()
        print(queue.__str__())

