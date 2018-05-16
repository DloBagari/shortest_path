class Heap:

    def __init__(self,pos):
        self.__heap = []
        self.__positions = pos

    def push(self, element):
        self.__heap.append(element)
        self.__parents_down(0,len(self.__heap) -1)

    def heappop(self):
        heap = self.__heap
        if heap:
            element = heap[0]
            last = heap.pop()
            if heap:
                heap[0] = last
                self.__parents_up(0, len(heap))
            return element
        return None

    def __parents_up(self, start, end):
        heap = self.__heap
        pos = self.__positions
        element = heap[start]
        childIndex = start * 2 + 1
        while childIndex < end:
            rightChild = childIndex + 1
            if rightChild < end and heap[rightChild] < heap[childIndex]:
                childIndex = rightChild
            heap[start] = heap[childIndex]
            heap[start].setIndex(start)
            pos[heap[start].getValue()] = start
            start = childIndex
            childIndex = 2 * start + 1
        heap[start] = element
        heap[start].setIndex(start)
        pos[heap[start].getValue()] = start
        self.__parents_down( 0,start)

    def __parents_down(self,start, end):
        heap = self.__heap
        pos = self.__positions
        new_element = heap[end]
        while end > start:
            parent_index = (end - 1) >> 1
            parent = heap[parent_index]
            if parent > new_element:
                heap[end] = parent
                heap[end].setIndex(end)
                pos[heap[end].getValue()] = end
                end = parent_index
                continue
            break
        heap[end] = new_element
        heap[end].setIndex(end)
        pos[heap[end].getValue()] = end

        
                
    def __len__(self):
        return len(self.__heap)
     
    def __str__(self):
        return ", ".join(str(i) for i in self.__heap)

    def update(self, item, key):
        position = self.__positions[item]
        self.__heap[position].setKey(key)
        self.__parents_down(0, position)
        
