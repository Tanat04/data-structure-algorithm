arrLen = int(input())      
A = list(map(int,input().split()))
 
dictI = {}

for each in range(len(A)):
    keyI = A[each] + (each+1) * (each+1)
    dictI[keyI] = dictI.get(keyI, 0) + 1

#print(dictI) 
count = 0

for each in range(len(A)):
    keyJ = A[each] - (each+1) * (each+1)
    if keyJ in dictI:
        #print(keyJ)
        count += dictI.get(keyJ)

print(count)