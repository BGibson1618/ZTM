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

    def findHeight(self, inputArray, checkIndex = 0, currHeight = 0):
      if checkIndex == (len(inputArray) - 1) / 2:
        return currHeight
      else:
        if isInstance(inputArray[2 * checkIndex + 1], int): 
        
      

    def printTree(self):
        inputArray = self.traverse([self.root], [])
        levelSize = 1
        printArray = []
        evenCounter, oddCounter = 0, 0
        for i in range(2, len(inputArray), 2):
            if type(inputArray[i]) is int:
                evenCounter += 1
        for i in range(1, len(inputArray), 2):
            if type(inputArray[i]) is int:
                oddCounter += 1
        remLevels = max(evenCounter, oddCounter)
        while remLevels >= 0: 
          tempArray = []
          nextLine = []
          for i in range(levelSize):
            tempArray.append(inputArray.pop(0))
          