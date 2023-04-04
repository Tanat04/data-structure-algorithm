import time

class heap:
    def __init__(self, array = [], compareFunction = lambda x, y: x < y):
        self.array = array
        self.compareFunction = compareFunction
        self.heapsize = len(self.array)
        if self.heapsize > 0:
            self.buildHeap()

    def isEmpty(self):
        return self.heapsize == 0

    def buildHeap(self):
        for i in range((self.heapsize-1)//2, -1, -1):
            self.heapify(i)

    def heapify(self, parentIndex):
        mainIndex = parentIndex
        leftIndex = (parentIndex * 2) + 1
        rightIndex = (parentIndex * 2) + 2

        if leftIndex < self.heapsize and self.compareFunction(self.array[leftIndex], self.array[mainIndex]):
            mainIndex = leftIndex

        if rightIndex < self.heapsize and self.compareFunction(self.array[rightIndex], self.array[mainIndex]):
            mainIndex = leftIndex

        if mainIndex != parentIndex:
            self.array[parentIndex], self.array[mainIndex] = self.array[mainIndex], self.array[parentIndex]

            self.heapify(mainIndex)

    def extract(self):
        firstNode = self.array[0]
        lastIndex = self.heapsize - 1

        self.array[0], self.array[lastIndex] = self.array[lastIndex], self.array[0]
        self.heapsize -= 1
        self.heapify(0)

        return firstNode

    def insert(self, element):
        self.heapsize += 1
        if len(self.array) < self.heapsize:
            self.array.append(element)
        else:
            self.array[self.heapsize - 1] = element
        
        elementIndex = (self.heapsize - 1)
        parentIndex = (elementIndex - 1) // 2

        while elementIndex > 0 and self.compareFunction(elementIndex, parentIndex):
            self.array[elementIndex], self.array[parentIndex] = self.array[parentIndex], self.array[elementIndex]
        
            elementIndex = parentIndex
            parentIndex = (elementIndex - 1) // 2

arr = [9,8,7,6,5,4,3,2,1]
resultList = []

st = time.process_time()

heapTest = heap(array= arr)
while not heapTest.isEmpty():
    resultList.append(heapTest.extract())

et = time.process_time()

print(resultList)
print(et - st)