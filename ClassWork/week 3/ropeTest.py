from Heap import heap
import time

def getMinCost(lt):

    ropes = heap(lt)
    cost = 0

    while ropes.heapsize > 1:
        x = ropes.extract()
        y = ropes.extract()
        print(x,y)

        total = x + y
        print(total)
        ropes.insert(total)

        cost += total
        print(cost)
        print()
    return cost

lt = list(map(int, input().split()))

st = time.process_time()
print(getMinCost(lt))
et = time.process_time()

print(et-st)