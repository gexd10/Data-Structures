class LinkedList:

    class Node:
        
        def __init__(self, e = None, next = None) -> None:
            self.e = e
            self.next = next
        def __str__(self):
            return str(self.e)

    def __init__(self) -> None:
        self.dummyHead = self.Node()
        self._size = 0
    
    def getSize(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def add(self, index, e):
        if index < 0 or index > self._size:
            raise ValueError("index illegal")

        pre = self.dummyHead
        for _ in range(index):
            pre = pre.next
        node = self.Node(e)
        node.next = pre.next
        pre.next = node
        self._size += 1
    
    def addFirst(self, e):
        self.add(0, e)

    def addLast(self, e):
        self.add(self._size, e)
    
    def get(self, index):
        if index < 0 or index >= self._size:
            raise ValueError("get failed, index illegal")
        cur = self.dummyHead.next
        for _ in range(index):
            cur = cur.next
        return cur.e

    def getFirst(self):
        self.get(0)
    
    def getLast(self):
        self.get(self._size - 1)

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise ValueError("remove failed, index illegal")
        pre = self.dummyHead
        for _ in range(index):
            pre = pre.next
        delNode = pre.next
        pre.next = delNode.next
        delNode.next = None
        self._size -= 1
        return delNode

    def removeFirst(self):
        self.remove(0)
    
    def removeLast(self):
        self.remove(self._size - 1)


    def set(self, index, e):
        if index < 0 or index >= self._size:
            raise ValueError("set failed, index illegal")
        cur = self.dummyHead.next
        for _ in range(index):
            cur = cur.next
        cur.e = e
    
    def contains(self, e):
        cur = self.dummyHead.next
        while cur is not None:
            if cur.e == e:
                return True
            cur = cur.next
        return False
    
    def __str__(self):
        res = []
        cur = self.dummyHead.next
        while cur:
            res.append(str(cur.e))
            cur = cur.next
        res.append("None")
        return '<LinkedList>: (Head) ' + ' -> '.join(res) + ' (Tail)'
        
linkedList = LinkedList()

for i in range(5):
    linkedList.addFirst(i)
    print(linkedList)
linkedList.add(2, 666)
print(linkedList)
linkedList.remove(2)
print(linkedList)
linkedList.removeFirst()
print(linkedList)
linkedList.removeLast()
print(linkedList)
