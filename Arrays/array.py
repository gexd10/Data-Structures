
class Array:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._size = 0
    
    def getSize(self):
        return self._size

    def getCapacity(self):
        return len(self._data)
    
    def isEmpty(self):
        return self._size == 0

    def addLast(self, e):
        self.add(self._size, e)

    def add(self, index, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        if index < 0 or index > self._size:
            raise ValueError("index require >=0 and <= size")
        for i in range(self._size -1, index -1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = e
        self._size += 1

    def addFirst(self, e):
        self.add(0, e)
    
    def get(self, index):
        if index < 0 or index >= self._size:
            raise ValueError("Index is illegal")
        return self._data[index]

    def set(self, index, e):
        if index < 0 or index >= self._size:
            raise ValueError("Index is illegal")
        self._data[index] = e
    
    def contains(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return True
        return False

    def find(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise ValueError("Remove failed Index is illegal")
        ret = self._data[index]
        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]
        self._size -= 1

        if self._size == len(self._data) // 4 and len(self._data) // 2 != 0:
            self._resize(len(self._data) // 2)
        return ret
    
    def removeFirst(self):
        return self.remove(0)
    
    def removeLast(self):
        return self.remove(self._size - 1)

    def removeElement(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)
    
    def _resize(self, newCapacity):
        newData = [None] * newCapacity
        for i in range(self._size):
            newData[i] = self._data[i]
        self._data = newData

    def __str__(self):
        return str('<Array> : {}, capacity: {}, size: {}'.format(self._data[0:self._size], self.getCapacity(), self.getSize()))

arr = Array()

for i in range(10):
    arr.addLast(i)
    
print(arr.__str__())
print(arr.add(1, 100))
print(arr.__str__())
print(arr.addFirst(-1))
print(arr.__str__())
print(arr.remove(2))
print(arr.__str__())
print(arr.removeElement(4))
print(arr.__str__())
print(arr.removeFirst())
print(arr.__str__())
print(arr.removeFirst())
print(arr.removeFirst())
print(arr.removeFirst())
print(arr.removeFirst())
print(arr.__str__())