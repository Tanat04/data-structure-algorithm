import sys
sys.setrecursionlimit(10000)

counter = 0

def partition(A, start, end):  # Lomuto's partition scheme
    pivot = A[end]
    i = start-1
    for j in range(start, end):
        global counter
        counter += 1
        if A[j] <= pivot:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[end],A[i+1] = A[i+1],A[end]
    return i+1

def quicksort(A, start, end):
    if start < end:
        pivot = partition(A, start, end)

        quicksort(A, start, pivot-1)
        quicksort(A, pivot+1, end)

def partitionTest(A):
    pivot = partition(A, 0, len(A)-1)
    print("Pivot", A[pivot])
    print("Left side", A[:pivot])
    print("RIght side", A[pivot+1:len(A)])
    print()

arr = list(map(int,input().split()))
n = len(arr)

quicksort(arr, 0, n-1)
print(counter)

firstCase = [10,9,8,7,6,5,4,3,2,1]
partitionTest(firstCase)
secondCase = [1,2,3,4,5,6,7,8,9,10]
partitionTest(secondCase)
thirdCase = [1,9,2,8,3,7,4,6,5]
partitionTest(thirdCase)