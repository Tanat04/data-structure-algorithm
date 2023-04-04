from os import dup
import random

def findDuplicate(nums):
 
    actual_sum = sum(nums)
    expected_sum = len(nums) * (len(nums) - 1) // 2
 
    return actual_sum - expected_sum
 
 
if __name__ == '__main__':
 
    nums = [1, 2, 3, 4, 4]
    print('The duplicate element is', findDuplicate(nums))

print("---------------------------------------------")

# wrote myself
def duplicateElement(lt):
    for i in lt:
        check = i
        for j in range(i,len(lt)):
            if j == check:
                return j
    return "No duplicate elemant."

randomList = []
for i in range(10):
    n = random.randint(1,10)
    randomList.append(n)

print(randomList)
print(duplicateElement(randomList))