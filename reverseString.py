def reverse(inputString):
    myList = []
    for i in range(len(inputString) - 1, -1, -1):
        myList.append(inputString[i])
    return ''.join(myList)


#or just inputString[::-1]