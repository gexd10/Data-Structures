import os, sys
sys.path.append(os.getcwd())

from Stacks_and_Queues.queue_int import Queue
from Stacks_and_Queues.array_queue import ArrayQueue
from LinkedList.linkedlistqueue import LinkedListQueue

class LoopQueue(Queue):

    def __init__(self, capacity=10):
        self.data = [None] * (capacity + 1)
        self.front = 0
        self.tail = 0
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.front == self.tail
    
    def getCapacity(self):
        return len(self.data) - 1

    def enqueue(self, e):
        if (self.tail + 1) % len(self.data) == self.front:
            self._resize(self.getCapacity() * 2)
        self.data[self.tail] = e
        self.tail = (self.tail + 1) % len(self.data)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Queue is empty, cannot dequeue")
        ret = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        if self.size == self.getCapacity() // 4:
            self._resize(self.getCapacity() // 2)
        return ret

    def getFront(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")
        return self.data[self.front]

    def _resize(self, newCapacity):
        newData = [None] * (newCapacity + 1)
        for i in range(self.size):
            newData[i] = self.data[(i + self.front) % len(self.data)]
        self.data = newData
        self.front = 0
        self.tail = self.size
    

    def __str__(self):
        if self.tail > self.front:
            return str('<loop_queue> : front {} tail, capacity: {}, size: {}'.format(self.data[self.front : self.tail], self.getCapacity(), self.getSize()))
        else:
            return str('<loop_queue> 2 : front {} tail, capacity: {}, size: {}'.format(str(self.data[self.front:] + self.data[:self.tail]), self.getCapacity(), self.getSize()))
    
queue = LoopQueue()
for i in range(10):
    queue.enqueue(i)
    print(queue.__str__())

    if i % 3 == 2:
        queue.dequeue()
        print(queue.__str__())

from time import time
from random import randint

def test_Queue(q, opCount):
    start_time = time()
    for i in range(opCount):
        q.enqueue(randint(1, 2000))
    for i in range(opCount):
        q.dequeue()
    end_time = time()
    return (end_time) - (start_time)


opCount = 20000
array_queue = ArrayQueue()
loop_queue = LoopQueue()
linkedlist_queue = LinkedListQueue()


print('LoopQueue time: ', test_Queue(loop_queue, opCount))
print('ArrayQueue time: ', test_Queue(array_queue, opCount))
print('linkedlist_queue time: ', test_Queue(linkedlist_queue, opCount))