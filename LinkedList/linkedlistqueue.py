import os, sys
sys.path.append(os.getcwd())

from Stacks_and_Queues.queue_int import Queue

class LinkedListQueue(Queue):

    class Node():
        def __init__(self, e = None, next = None) -> None:
            self.e = e
            self.next = next

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def getFront(self):
        if self.isEmpty():
            raise ValueError("failed, it is empty")
        return self.head.e
    
    def dequeue(self):
        if self.isEmpty():
            raise ValueError("failed, it is empty")
        delNode = self.head
        self.head = self.head.next
        delNode.next = None
        if self.head == None: self.tail = None
        self.size -= 1
        return delNode.e
    
    def enqueue(self, e):
        if self.tail == None:
            self.tail = self.Node(e)
            self.head = self.tail
        else:
            self.tail.next = self.Node(e)
            self.tail = self.tail.next
        self.size += 1

    def __str__(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.e))
            cur = cur.next
        res.append("None Tail")
        return '<LinkedListQueue>: (Head) ' + ' -> '.join(res)
            
queue = LinkedListQueue()
for i in range(10):
    queue.enqueue(i)
    print(queue.__str__())

    if i % 3 == 2:
        queue.dequeue()
        print(queue.__str__())
        