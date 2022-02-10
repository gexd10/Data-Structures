import os, sys
sys.path.append(os.getcwd())

from Stacks_and_Queues.stack_int import Stack
from LinkedList.linkedlist import LinkedList
from Stacks_and_Queues.array_stack import ArrayStack

class LinkedListStack(Stack):

    def __init__(self) -> None:
        self.list = LinkedList()

    def getSize(self):
        return self.list.getSize()

    def isEmpty(self):
        return self.list.isEmpty()

    def pop(self):
        return self.list.removeFirst()

    def peek(self):
        return self.list.getFirst()

    def push(self,e):
        return self.list.addFirst(e)
    
    def __str__(self):
        res = []
        cur = self.list.dummyHead.next
        while cur:
            res.append(str(cur))
            cur = cur.next
        res.append("None")
        return '<LinkedListStack>: (top) ' + ' -> '.join(res)

stack = LinkedListStack()
for i in range(5):
    stack.push(i)
    print(stack)

stack.pop()
print(stack)

from time import time
from random import randint

def test_Stack(q, opCount):
    start_time = time()
    for i in range(opCount):
        q.push(randint(1, 2000))
    for i in range(opCount):
        q.pop()
    end_time = time()
    return (end_time) - (start_time)


opCount = 10000000
array_stack = ArrayStack()
linkedlist_stack = LinkedListStack()


print('linkedliststack time: ', test_Stack(linkedlist_stack, opCount))
print('arraystack time: ', test_Stack(array_stack, opCount))