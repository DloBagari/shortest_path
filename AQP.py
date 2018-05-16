from heapAPQ import Heap
from element import Element
class APQ:
    "Adaptable Priority Queues, heap"
    def __init__(self):
        self.__size = 0
        self.__positions = {}
        self.__heap = Heap(self.__positions)

    def add(self, key, item):
        if item not in self.__positions :
            self.__heap.push(Element(key, item, self.__size))
            self.__size += 1
    def getMin(self):
        return self.__heap.heappop()

    def __str__(self):
        return str(self.__heap)

    def update(self, element, key):
        self.__heap.update(element, key)
        
    def __len__(self):
        return len(self.__heap)
