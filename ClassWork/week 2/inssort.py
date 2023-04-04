import time

a = list(map(int, input().split()))
n = len(a)

st = time.process_time()

for i in range(1,n):
    currentValue = a[i]

    valueInfront = i-1

    while valueInfront >= 0 and a[valueInfront] > currentValue:
        a[valueInfront+1] = a[valueInfront]
        valueInfront -= 1
    
    a[valueInfront+1] = currentValue

et = time.process_time()
print(a)
print(et-st)
 
 
# a = [4,3,12,1,5,6]
# n = len(a)

# st = time.process_time()

# for i in range(1,n):
#     print(a)
#     currentValue = a[i]
#     print(currentValue)#3

#     valueInfront = i-1#4
#     print(i,valueInfront)

#     while valueInfront >= 0 and a[valueInfront] > currentValue:
#         print(a[valueInfront])
#         a[valueInfront+1] = a[valueInfront]
#         print(a[valueInfront+1])
#         valueInfront -= 1
    
#     print(valueInfront)
#     a[valueInfront+1] = currentValue


    
# et = time.process_time()
# #[4,3,12,1,5,6]
# print(a)
# print(et-st)
 