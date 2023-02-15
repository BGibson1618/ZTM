class Node():

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.data)


class MyDLinkList():

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
            nodeArray.append(str(node.data))
        return " -> ".join(nodeArray[i] for i in range(len(nodeArray)))

    def __getitem__(self, index):
        returnNode = self.traverse(index)
        if returnNode is not None:
            return returnNode.data

    def append(self, data):
        appNode = Node(data)
        appNode.prev = self.tail
        self.tail.next = appNode
        self.tail = appNode
        self.length += 1

    def prepend(self, data):
        preNode = Node(data)
        preNode.next = self.head
        self.head.prev = preNode
        self.head = preNode
        self.length += 1

    def traverse(self, index):
        if index == 0:
            return self.head
        elif index == self.length - 1:
            return self.tail
        elif index < 0 or index >= self.length:
            print("Index out of range")
        else:
            counter = 1
            currNode = self.head.next
            for _ in self:
                if counter == index:
                    break
                currNode = currNode.next
                counter += 1
            return currNode

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
        elif index == self.length:
            self.append(data)
        elif index < 0 or index > self.length:
            print("Index out of range")
        else:
            trailNode = self.traverse(index)
            leadNode = trailNode.prev
            inNode = Node(data)
            leadNode.next = inNode
            inNode.prev = leadNode
            trailNode.prev = inNode
            inNode.next = trailNode
            self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        else:
            remNode = self.traverse(index)
            if remNode is not None:
                leadNode = remNode.prev
                trailNode = remNode.next
                leadNode.next = trailNode
                trailNode.prev = leadNode
                self.length -= 1

    def reverse(self):
        revArray = []
        for node in self:
            revArray.insert(0, node.data)
        return MyDLinkList(revArray)