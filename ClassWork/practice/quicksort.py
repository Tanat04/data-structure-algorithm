arr = [4,3,2,1]
n = len(arr)

def quicksort(arr, start, end):
    if start < end:
        pivot_pos = partition(arr, start, end)

        quicksort(arr, start, pivot_pos-1)
        quicksort(arr, pivot_pos+1, end)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[end], arr[i+1] = arr[i+1], arr[end] 
    return i + 1

quicksort(arr, 0, n-1)
print(arr)

# tbh i dodnt understand the fucking code that much but by wt i understand is that
# it hv a pivot elmenent as the right most one and try to arrange the lish such that
# element lesser than pivot are toward the right and vice versa. then it find the sort
# for the right side and left side respectively