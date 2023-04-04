def merge(a, start, middle, end):
    lt = []
    i = start
    j = middle + 1

    while i <= middle and j <= end:
        if a[i] <= a[j]:
            lt.append(a[i])
            i += 1
        else:
            lt.append(a[j])
            j += 1

    a[start:end+1] = lt + a[i:middle+1] + a[j:end+1]

def mergesort(a, start, end):
    if start < end:
        middle = (start + end) // 2
        mergesort(a, start, middle)
        mergesort(a, middle+1, end)

        merge(a, start, middle, end)

a = [5,4,1,3,6,8,7,9,1,5,2,6,6]

mergesort(a, 0, len(a)-1)
print(a)

# aight i like this one, so we just keep dividing the list till theres only one element left
# then we compare them which each other and keep adding the lesser one into an empty list
# after running out of element in the list, just add them together