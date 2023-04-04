def merge(A, leftside, middle, rightside):
    B = []
    i = leftside
    j = middle+1
    while i <= middle and j <= rightside:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    
    A[leftside:rightside+1] = B + A[i:middle+1] + A[j:rightside+1]

def mergesort(A, p, r):
    if p < r:
        middle = (p + r) // 2
        mergesort(A, p, middle)
        mergesort(A, middle+1, r)
        merge(A, p, middle, r)

a = list(map(int, input().split()))
import time

st = time.process_time()
mergesort(a, 0, len(a)-1)
et = time.process_time()

print(a)
print(et-st)



# def merge(A, leftside, middle, rightside):
#     B = []
#     i = leftside
#     j = middle+1
#     while i <= middle and j <= rightside:
#         if A[i] <= A[j]:
#             B.append(A[i])
#             i += 1
#         else:
#             B.append(A[j])
#             j += 1
    
#     print(A[leftside:rightside+1], B,A[i:middle+1],A[j:rightside+1])
#     print(A[leftside:rightside+1], B+A[i:middle+1]+ A[j:rightside+1])
#     A[leftside:rightside+1] = B + A[i:middle+1] + A[j:rightside+1]

# def mergesort(A, p, r):
#     print(p,r,"outside")
#     if p < r:
#         print(p,r,"Inside")
#         middle = (p + r) // 2
#         mergesort(A, p, middle)
#         mergesort(A, middle+1, r)
#         print("Reached")
#         merge(A, p, middle, r)

# #a = list(map(int, input().split()))
# a = [3,4,1,6,2,5,7,8,5,9,10]
# import time

# st = time.process_time()
# mergesort(a, 0, len(a)-1)
# et = time.process_time()

# print(a)
# print(et-st)