import os, sys
sys.path.append(os.getcwd())

from Arrays.array import Array
from Stacks_and_Queues.stack_int import Stack

class ArrayStack(Stack):

    def __init__(self, capacity=10):
        self.array = Array(capacity)

    def getSize(self):
        return self.array.getSize()

    def isEmpty(self):
        return self.array.isEmpty()
    
    def getCapacity(self):
        return self.array.getCapacity()

    def push(self, e):
        return self.array.addLast(e)
    
    def pop(self):
        return self.array.removeLast()
    
    def peek(self):
        return self.array.getLast()

    def __str__(self):
        return str('<array_stack> :{} '.format(self.array))


stack = ArrayStack()
for i in range(5):
    stack.push(i)
    print(stack.__str__())

stack.pop()
print(stack.__str__())
