import os, sys
sys.path.append(os.getcwd())

from Set_and_Map.map_int import Map

class LinkedListMap(Map):

    class Node:

        def __init__(self, key = None, value = None, next = None):

            self.key = key
            self.value = value
            self.next = next

        def __str__(self):
            return "Key: {}, Value: {}".format(str(self.key), str(self.value))
    def __init__(self) -> None:
        self.dummyHead = self.Node()
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def _getNode(self, key):
        cur = self.dummyHead.next
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def contains(self, key):
        if self._getNode(key):
            return True
        else:
            return False
        
    
    def get(self, key):
        node = self._getNode(key)
        return node.value if node is not None else None

    def add(self, key, value):
        node = self._getNode(key)
        if node is None:
            self.dummyHead.next = self.Node(key, value, self.dummyHead.next)
            self.size += 1
        else:
            node.value = value

    def set(self, key, newvalue):
        node = self._getNode(key)
        if node is None:
            raise ValueError("key not exist")
            
        node.value = newvalue

    def remove(self, key):
        prev = self.dummyHead
        while prev.next is not None:
            if prev.next.key == key:
                break
            prev = prev.next

        if prev.next is not None:
            delNode = prev.next
            prev.next = delNode.next
            delNode.next = None
            self.size -= 1
            return delNode.value
        return None




words = ''
with open('./Set_and_Map/pride-and-prejudice.txt', 'r') as f:
    words = f.read()
words = words.split()

from time import time
start_time = time()
linkedlist_map = LinkedListMap()
for word in words:
    if linkedlist_map.contains(word):
        linkedlist_map.set(word, linkedlist_map.get(word) + 1)
    else:
        linkedlist_map.add(word, 1)

print('Total words: ', len(words))
print('Unique words: ', linkedlist_map.getSize())
print('Contains word "prejudice": ', linkedlist_map.contains('prejudice'))
print("Frequency of PRIDE: ",  linkedlist_map.get("pride"))
print('Total time: {} seconds'.format(time() - start_time))