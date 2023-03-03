def in_sort(arr):
    last_sorted = arr[0]
    for i in range(len(arr)):
        if arr[i] < last_sorted:
            temp = arr.pop(i)
            for j in range(0, i):
                if temp < arr[j]:
                    arr.insert(j, temp)
                    break
        last_sorted = arr[i]
    return arr