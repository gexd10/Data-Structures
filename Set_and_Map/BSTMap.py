import os, sys
sys.path.append(os.getcwd())

from Set_and_Map.map_int import Map

class BSTMap(Map):

    class Node:

        def __init__(self, key = None, value = None) -> None:
            self.key = key
            self.value = value
            self.left = None
            self.right = None
        def __str__(self):
            return "Key: {}, Value: {}".format(str(self.key), str(self.value))
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, key, value):
        self.root = self._add(self.root, key, value)

    def _add(self, node, key, value):
        if node == None:
            self.size += 1
            return self.Node(key, value)

        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:
            node.value = value
        return node

    def _getNode(self, node, key):
        if node is None: return None
        if node.key > key:
            return self._getNode(node.left, key)
        elif node.key < key:
            return self._getNode(node.right, key)
        elif node.key == key:
            return node

    def contains(self, key):
        if self._getNode(self.root, key):
            return True
        else:
            return False
    
    def get(self, key):
        node = self._getNode(self.root, key)
        return node.value if node is not None else None
    
    def set(self, key, newvalue):
        node = self._getNode(self.root, key)
        if node is None:
            raise ValueError("key not exist")
        node.value = newvalue
    
    def _minimum(self, node):
        if node.left is None:
            return node
        return self._minimum(node.left)

    def _removeMin(self, node):
        if node.left is None:
            rightNode = node.right
            node.right = None
            self.size -= 1
            return rightNode
        node.left = self._removeMin(node.left)
        return node

    def remove(self, key):
        node = self._getNode(self.root, key)
        if node is not None:
            self.root = self._remove(self.root, key)
            return node.value
        return None

    def _remove(self, node, key):
        if node is None: return None
        if key < node.key:
            self._remove(node.left, key)
            return node
        elif key > node.key:
            self._remove(node.right, key)
            return node
        else:
            if node.left is None:
                rightNode = node.right
                node.right = None
                self.size -= 1
                return rightNode
            if node.right is None:
                leftNode = node.left
                node.left = None
                self.size -= 1
                return leftNode
            successor = self._minimum(node.right)
            successor.left = node.left
            successor.right = self._removeMin(node.right)
            node.left = node.right = None
            return successor 

words = ''
with open('./Set_and_Map/pride-and-prejudice.txt', 'r') as f:
    words = f.read()
words = words.split()

from time import time
start_time = time()
bst_map = BSTMap()
for word in words:
    if bst_map.contains(word):
        bst_map.set(word, bst_map.get(word) + 1)
    else:
        bst_map.add(word, 1)

print('Total words: ', len(words))
print('Unique words: ', bst_map.getSize())
print('Contains word "prejudice": ', bst_map.contains('prejudice'))
print("Frequency of PRIDE: ",  bst_map.get("pride"))
print('Total time: {} seconds'.format(time() - start_time))