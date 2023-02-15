class QStack():

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __repr__(self):
        return " -> ".join(str(self.s1[i]) for i in range(len(self.s1)))

    def enq(self, data):
        if len(self.s1) == 0:
            self.s1.append(data)
        else:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())
            self.s1.append(data)

            for _ in range(len(self.s2)):
                self.s1.append(self.s2.pop())

    def deq(self):
        return self.s1.pop()
