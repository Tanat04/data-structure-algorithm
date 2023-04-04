import time

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = list(map(int,input().split()))
list4 = list(map(int,input().split()))
listOneTwoDict = {}

st = time.process_time()
for i in list1:
    for j in list2:
        key = i + j
        listOneTwoDict[key] = [i, j]

found = False
for i in list3:
    for j in list4:
        key = -1 * (i + j)
        if key in listOneTwoDict:
            break
    else:
        continue

    break
et = time.process_time()

print(f"{listOneTwoDict[key][0]}, {listOneTwoDict[key][1]}, {i}, {j}")
print(listOneTwoDict[key][0] + listOneTwoDict[key][1] + i + j)
print(et - st)
