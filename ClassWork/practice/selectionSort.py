lt = [10,9,8,7,6,5,4,3,2,1]
n = len(lt)

for i in range(n):
    minIndex = i

    for j in range(i+1, n):
        if  lt[j] < lt[minIndex] :
            minIndex = j

    lt[i], lt[minIndex] = lt[minIndex], lt[i]
    print(lt)

print(lt)

# Aight for this is pretty simple. We loop through the whole list then we keep the first index as min
# then we loop again through the whole list while starting to count the first index. then when it find 
# the number that are lower than the first element then assign as min to it
# at the end of the loop it swap the min value with the first index's value.

lt = [5,4,3,2,1,8,4,2,1,6,9]
n = len(lt)

def findFuckingMax(lt, lastIndex):

    maxIndex = 0
    for i in range(1, lastIndex + 1):
        if lt[i] > lt[maxIndex]:
            maxIndex = i

    MaxValue = lt[maxIndex]
    lt[maxIndex] = lt[lastIndex]
    #print(lt)
    return MaxValue

for i in range(n-1,-1,-1):
    lt[i] = findFuckingMax(lt, i)

print(lt)

# Aight for this shit, its just rying to do the more complicated way which is
# it loop the list backward find the largest element in the list and then swab
# it with the last index.