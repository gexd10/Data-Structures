import os, sys
sys.path.append(os.getcwd())

from Set_and_Map.set_int import Set
from BST.bst import BST

class BSTset(Set):

    def __init__(self) -> None:
        self.bst = BST()

    def getSize(self):
        return self.bst.size()
    
    def isEmpty(self):
        return self.bst.isEmpty()

    def remove(self, e):
        return self.bst.remove(e)
    
    def contains(self, e):
        return self.bst.contains(e)
    
    def add(self, e):
        return self.bst.add(e)

from time import time
start_time = time()
words1 = ''
with open('./Set_and_Map/pride-and-prejudice.txt', 'r') as f:
    words1 = f.read()
words1 = words1.split()


set1 = BSTset()
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
# set2 = BSTset()
# for word in words2:
#     set2.add(word)
# print("Total different words: ", set2.getSize())