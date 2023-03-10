class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


class BST():

    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        if data == self.root.data:
            print("Element already exists")
        else:
            inNode = Node(data)
            targetNode = self.target(self.root, data)
            if data < targetNode.data:
                if targetNode.left is not None:
                    print("Element already exists")
                else:
                    targetNode.left = inNode
            else:
                if targetNode.right is not None:
                    print("Element already exists")
                else:
                    targetNode.right = inNode

    def remove(self, data):
        targetNode = self.target(self.root, data)
        remNode = None
        if targetNode.data == data:
            if targetNode.left is None and targetNode.right is None:
                self.root = None
            elif targetNode.left is not None:
                remNode = targetNode
                targetNode = targetNode.left
                movNode = self.findRight(targetNode)
                movNode.right = remNode.right
                self.root = targetNode
            else:
                remNode = targetNode
                targetNode = targetNode.right
                movNode = self.findLeft(targetNode)
                movNode.left = remNode.left
                self.root = targetNode
        elif data < targetNode.data:
            if targetNode.left is None:
                print("Element not found")
            else:
                remNode = targetNode.left
                if remNode.left is None and remNode.right is None:
                    targetNode.left = None
                elif remNode.left is not None:
                    movNode = self.findRight(remNode.left)
                    movNode.right = remNode.right
                    targetNode.left = remNode.left
                else:
                    movNode = self.findLeft(remNode.right)
                    movNode.left = remNode.right
                    targetNode.left = remNode.left
        else:
            if targetNode.right is None:
                print("Element not found")
            else:
                remNode = targetNode.right
                if remNode.left is None and remNode.right is None:
                    targetNode.right = None
                elif remNode.left is not None:
                    movNode = self.findRight(remNode.left)
                    movNode.right = remNode.right
                    targetNode.right = remNode.left
                else:
                    movNode = self.findLeft(remNode.right)
                    movNode.left = remNode.right
                    targetNode.right = remNode.left

    def findRight(self, passNode):
        currNode = passNode
        if currNode.right is None:
            return currNode
        else:
            return self.findRight(currNode.right)

    def findLeft(self, passNode):
        currNode = passNode
        if currNode.left is None:
            return currNode
        else:
            return self.findLeft(currNode.left)

    def target(self, passNode, data):
        currNode = passNode
        if (currNode.data
                == data) or (currNode.left is not None and currNode.left.data
                             == data) or (currNode.right is not None
                                          and currNode.right.data == data):
            return currNode
        elif data < currNode.data and currNode.left is not None:
            currNode = currNode.left
            return self.target(currNode, data)
        elif data > currNode.data and currNode.right is not None:
            currNode = currNode.right
            return self.target(currNode, data)
        else:
            return currNode

    def traverse(self, checkArray, doneArray):
        nodes = checkArray
        done = doneArray
        if len(nodes) == 0:
            return done
        else:
            if isinstance(nodes[0], Node):
                if nodes[0].left is not None:
                    nodes.append(nodes[0].left)
                if nodes[0].left is None:
                    nodes.append("x")
                if nodes[0].right is not None:
                    nodes.append(nodes[0].right)
                if nodes[0].right is None:
                    nodes.append("x")
                done.append(nodes.pop(0).data)
            else:
                done.append(nodes.pop(0))
        return self.traverse(nodes, done)

    def printTree(self):
        inputArray = self.traverse([self.root], [])
        levelSize = 1
        printArray = []
        while len(inputArray) > 0:
            tempArray = []
            for i in range(levelSize):
                tempArray.append(inputArray.pop(0))
            levelSize = 0
            for i in range(len(tempArray)):
                if isinstance(tempArray[i], int):
                    levelSize += 2
            printArray.extend([tempArray])
        for i in range(len(printArray) - 1):
            for j in range(len(printArray[i])):
                if not isinstance(printArray[i][j], int):
                    printArray[i + 1].insert(2 * j, " ")
                    printArray[i + 1].insert(2 * j, " ")
        numLevels = len(printArray)
        remLevels = numLevels - 1
        for i in range(numLevels):
            tempArray = []
            for j in range(len(printArray[i])):
                tempArray.append(printArray[i].pop(0))
                for k in range(int(2**(remLevels + 1) - 1)):
                    tempArray.append(" ")
            remLevels -= 1
            printArray[i].clear()
            printArray[i].extend(tempArray)
        remLevels = numLevels - 1
        for i in range(numLevels):
            for j in range(2**remLevels - 1):
                printArray[i].insert(0, " ")
            remLevels -= 1
        # print(*printArray)
        for i in range(len(printArray) - 1):
            j = 0
            while j < len(printArray[i]):
                if isinstance(printArray[i][j], int):
                    if len(str(printArray[i][j])) > 1:
                        offset = len(str(printArray[i][j])) - 1
                        for k in range(offset):
                            printArray[i].pop(j + 1)
                j += 1
        for i in range(len(printArray)):
            print(*printArray[i])

    def printSimple(self):
        inputArray = self.traverse([self.root], [])
        levelSize = 1
        printArray = [" "]
        while len(inputArray) > 0:
            tempArray = []
            for i in range(levelSize):
                tempArray.append(inputArray.pop(0))
            levelSize = 0
            for i in range(len(tempArray)):
                if isinstance(tempArray[i], int):
                    levelSize += 2
            printArray.extend(tempArray)
            printArray.append("\n")
        print(*printArray)
