arrLen = int(input())
A = list(map(int,input().split()))

dictI = {}
dictJ = {}

for each in range(len(A)):
    keyI = A[each] + (each+1) * (each+1)
    dictI[keyI] = dictI.get(keyI, 0) + 1

    keyJ = A[each] - (each+1) * (each+1)
    dictJ[keyJ] = dictJ.get(keyJ, 0) + 1


#print(dictI)
#print(dictJ)

count = 0
for each in dictI:
    count += dictJ.get(each,0) * dictI.get(each)

print(count)
