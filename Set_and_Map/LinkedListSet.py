import os, sys
sys.path.append(os.getcwd())

from Set_and_Map.set_int import Set
from LinkedList.linkedlist import LinkedList

class LinkedListSet(Set):

    def __init__(self) -> None:
        self.list = LinkedList()

    def getSize(self):
        return self.list.getSize()

    def isEmpty(self):
        return self.list.isEmpty()
    
    def remove(self, e):
        self.list.remove(e)
    
    def contains(self, e):
        return self.list.contains(e)
    
    def add(self, e):
        if not self.list.contains(e):
            self.list.addFirst(e)


from time import time
start_time = time()
words1 = ''
with open('./Set_and_Map/pride-and-prejudice.txt', 'r') as f:
    words1 = f.read()
words1 = words1.split()

set1 = LinkedListSet()
for word in words1:
    set1.add(word)
print("Total words: ", len(words1))
print("Total different words: ", set1.getSize())
print('Total time: {} seconds'.format(time() - start_time))

# words2 = ''
# with open('./Set_and_Map/a-tale-of-two-cities.txt', 'r') as f:
#     words2 = f.read()
# words2 = words2.split()
# print("Total words: ", len(words2))
# set2 = LinkedListSet()
# for word in words2:
#     set2.add(word)
# print("Total different words: ", set2.getSize())