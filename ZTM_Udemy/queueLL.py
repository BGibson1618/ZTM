class QNode():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class QLL():

    def __init__(self, data):
        self.head = QNode(data)
        self.tail = self.head
        self.length = 1

    def __iter__(self):
        currNode = self.head
        while currNode is not None:
            yield currNode
            currNode = currNode.next

    def __repr__(self):
        return " <- ".join(
            str(node.data) for node in self) + "\nHead is " + str(
                self.head.data) + " and Tail is " + str(
                    self.tail.data) + "\nLength is " + str(self.length) + "\n"

    def enq(self, data):
        pushNode = QNode(data)
        self.tail.next = pushNode
        self.tail = pushNode
        self.length += 1

    def deq(self):
        self.head = self.head.next
        self.length -= 1
