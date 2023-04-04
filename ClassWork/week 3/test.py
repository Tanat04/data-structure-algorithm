from Heap import heap
import time

item = list(map(int, input().split()))

test = heap(items= item)
lt = []

st = time.process_time()
while not test.empty():
    lt.append(test.extract())

total = 0
st = time.process_time()
for i in range(2,len(lt)+1):
    total += sum(lt[0:i])

et = time.process_time()
print(lt)
print(total)
print(et-st)
