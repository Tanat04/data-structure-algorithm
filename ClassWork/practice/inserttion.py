lt = [10,9,8,7,6,5,4,3,2,1]
n = len(lt)

for i in range(1, n):
    currentValue = lt[i]
    previousIndex = i-1

    while previousIndex >= 0 and lt[previousIndex] > currentValue:
        lt[previousIndex+ 1] = lt[previousIndex]
        previousIndex -= 1

    lt[previousIndex + 1] = currentValue

print(lt)

# aight so we loop throught the list, starting from the element at the first index
# then we check if the previous index's value is greater than the current value
# if it is greater than we assign the previous index's value to the current value
# and the current value to the privious index, its kind of like swapping them.