class StackNode():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class StackLL():

    def __init__(self, data):
        self.top = StackNode(data)
        self.bottom = self.top
        self.length = 1

    def __iter__(self):
        currNode = self.top
        while currNode is not None:
            yield currNode
            currNode = currNode.next

    def __repr__(self):
        return " -> ".join(str(node.data) for node in self)

    def push(self, data):
        pushNode = StackNode(data)
        pushNode.next = self.top
        self.top = pushNode
        self.length += 1

    def peek(self):
        return self.top

    def pop(self):
        tempData = self.top.data
        self.top = self.top.next
        self.length -= 1
        return tempData
