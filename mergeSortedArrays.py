def mergeArrays(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2

    mergedArray = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if (arr1[i] <= arr2[j]):
            mergedArray.append(arr1[i])
            i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1

    return mergedArray + arr1[i:] + arr2[j:]
