def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        right = []
        left = []
        for item in arr:
            if item > pivot:
                right.append(item)
            else:
                left.append(item)
        return quicksort(left) + [pivot] + quicksort(right)


def quick_inplace(arr):
    return _quick(arr, 0, len(arr) - 1)


def _quick(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        _quick(arr, left, pi - 1)
        _quick(arr, pi + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            swap(arr, i, j)
    if arr[i] > pivot:
        swap(arr, i, right)
    return i


def swap(arr, m, n):
    arr[m], arr[n] = arr[n], arr[m]
    return arr
