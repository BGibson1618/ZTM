def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = int(len(arr) / 2)
        left = arr[0:mid]
        right = arr[mid:]
        return merge(merge_sort(left), merge_sort(right))


def merge(arr1, arr2):
    new_arr = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
        elif arr2[0] < arr1[0]:
            new_arr.append(arr2.pop(0))
    if len(arr1) > 0:
        new_arr.extend(arr1)
    elif len(arr2) > 0:
        new_arr.extend(arr2)
    return new_arr
