class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class myLinkedList():

    def __init__(self, data):
        if isinstance(data, list):
            self.head = Node(data.pop(0))
            self.tail = self.head
            self.length = 1
            for _ in range(len(data)):
                self.append(data.pop(0))
        else:
            self.head = Node(data)
            self.tail = self.head
            self.length = 1

    def __iter__(self):
        currNode = self.head
        while currNode is not None:
            yield currNode
            currNode = currNode.next

    def __repr__(self):
        nodeArray = []
        for node in self:
            nodeArray.append(node.data)
        return " -> ".join(str(nodeArray[i]) for i in range(len(nodeArray)))

    def __getitem__(self, index):
        if index == 0:
            return self.head.data
        if index < 0 or index >= self.length:
            print("Index out of range")
        else:
            counter = 1
            currNode = self.head.next
            while counter < index:
                currNode = currNode.next
                counter += 1
            return currNode.data

    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
        elif index > self.length or index < 0:
            print("Index out of range")
        else:
            counter = 1
            insertNode = Node(data)
            currentNode = self.head.next
            prevNode = self.head
            while counter < index:
                prevNode = currentNode
                currentNode = currentNode.next
                counter += 1
            prevNode.next = insertNode
            insertNode.next = currentNode
            self.length += 1
            return self

    def remove(self, index):
        if index >= self.length or index < 0:
            print("Index out of range")
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            counter = 1
            leftNode = self.head
            while counter < index:
                leftNode = leftNode.next
                counter += 1
            if leftNode.next is self.tail:
                leftNode.next = None
                self.tail = leftNode
                self.length -= 1
            else:
                rightNode = leftNode.next.next
                leftNode.next = rightNode
                self.length -= 1

    def reverse(self):
        revArray = []
        for node in self:
            revArray.insert(0, node.data)
        return myLinkedList(revArray)

    def reverse2(self):
        if self.length == 1:
            return self
        else:
            firstNode = self.head
            secondNode = firstNode.next
            self.head, self.tail = self.tail, self.head
            self.tail.next = None
            while secondNode:
                tempNode = secondNode.next
                secondNode.next = firstNode
                firstNode = secondNode
                secondNode = tempNode