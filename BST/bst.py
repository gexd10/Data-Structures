from calendar import weekday
import collections


class BST:
    class Node:
        def __init__(self,e = 0, left = None, right = None) -> None:
            self.e = e
            self.left = left
            self.right = right
    def __init__(self) -> None:
        self.root = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
    
    def add(self, e):
        self.root = self._add(self.root, e)
        # if self.root == None:
        #     self.root = self.Node(e)
        #     self.size += 1
        # else:
        #     self._add(self.root, e)

    def _add(self, node, e):
        # if node.e == e:
        #     return
        # elif node.e < e and node.right is None:
        #     node.right = self.Node(e)
        #     self._size += 1
        #     return 
        # elif node.e > e and node.left is None:
        #     node.left = self.Node(e)
        #     self._size += 1
        #     return
        # if node.e < e:
        #     self._add(self, node.right, e)
        # elif node.val > e:
        #     self._add(self, node.left, e)
        # clear way
        if node is None:
            node = self.Node(e)
            self._size += 1
            return node
        if node.e > e:
            node.left = self._add(node.left, e)
            
        elif node.e < e:
            node.right = self._add(node.right, e)
        return node
    
    def contains(self, e):
        return self._contains(self.root, e)

    def _contains(self, node, e):
        if node is None: return False
        if e == node.e: return True
        elif e > node.e: return self._contains(node.right, e)
        else:
            return self._contains(node.left, e)

    def preOrder(self):
        self._preOrder(self.root)

    def preOrderNR(self):
        stack = []
        stack.append(self.root)
        while stack:
            cur = stack.pop()
            print(cur.e)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    def levelOrder(self):
        q = collections.deque()
        q.append(self.root)
        while q:
            cur = q.popleft()
            print(cur.e)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    def _preOrder(self, node):
        if node is None: return
        print(node.e)
        self._preOrder(node.left)
        self._preOrder(node.right)

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, node):
        if node is None: return
        
        self._inOrder(node.left)
        print(node.e)
        self._inOrder(node.right) 
    
    def postOrder(self):
        self._postOrder(self.root)

    def _postOrder(self, node):
        if node is None: return
        
        self._postOrder(node.left)
        self._postOrder(node.right)
        print(node.e)

    def minimum(self):
        if self._size == 0: raise ValueError("BST empty")
        minNode = self._minimum(self.root)
        return minNode.e

    def _minimum(self, node):
        if node.left is None:
            return node
        return self._minimum(node.left)

    def maximum(self):
        if self._size == 0: raise ValueError("BST empty")
        maxNode = self._maximum(self.root)
        return maxNode.e

    def _maximum(self, node):
        if node.right is None:
            return node
        return self._maximum(node.right)

    def removeMin(self):
        ret = self.minimum()
        self.root = self._removeMin(self.root)
        return ret

    def _removeMin(self, node):
        if node.left is None:
            rightNode = node.right
            node.right = None
            self._size -= 1
            return rightNode
        node.left = self._removeMin(node.left)
        return node
    
    def removeMax(self):
        ret = self.maximum()
        self.root = self._removeMax(self.root)
        return ret
    
    def _removeMax(self, node):
        if node.right is None:
            leftNode = node.left
            node.left = None
            self._size -= 1
            return leftNode
        node.right = self._removeMax(node.right)
        return node
    
    def remove(self, e):
        root = self._remove(self.root, e)
    
    def _remove(self, node, e):
        if node is None: return None
        if node.e < e:
            self._remove(node.right, e)
            return node
        elif node.e > e:
            self._remove(node.left, e)
            return node
        else: 
            # e == node.e
            if node.left is None:
                rightNode = node.right
                node.right = None
                self._size -= 1
                return rightNode
            if node.right is None:
                leftNode = node.left
                node.left = None
                self._size -= 1
                return leftNode
            
            successor = self._minimum(node.right)
            successor.right = self._removeMin(successor.right)
            successor.left = node.left

            node.left = node.right = None
            return node



    def __str__(self):
        res = []
        self._generate_BST_string(self.root, 0, res)
        return '<BST>:\n' + ''.join(res)

    def _generate_BST_string(self, node, depth, res):
        if not node:
            res.append(self._generate_depth_string(depth) + 'None\n')
            return
        res.append(self._generate_depth_string(depth) + str(node.e) + '\n')
        self._generate_BST_string(node.left, depth + 1, res)
        self._generate_BST_string(node.right, depth + 1, res)

    def _generate_depth_string(self, depth):
        res = ''
        for _ in range(depth):
            res += '--'
        return res


nums = [5, 3, 6, 8, 4, 2, 2]
bst = BST()   
# for num in nums:
#     bst.add(num)

# bst.preOrder()
# print("pre", bst)

# bst.preOrderNR()
# print("NR", bst)

# bst.inOrder()
# print("in", bst)

# bst.postOrder()
# print("post", bst)


from random import randint
for i in range(20):
    bst.add(randint(0, 10))
print(bst)
bst.inOrder()
print('*' * 20)
bst.removeMin()
bst.removeMax()
bst.inOrder()
print('*' * 20)
print(bst.size())
print(bst.remove(2))
print(bst.size())



