class StackArray():

    def __init__(self):
        self.array = {}
        self.length = 0

    def __repr__(self):
        return " ".join(str(self.array[i]) for i in range(self.length))

    def push(self, data):
        self.array[self.length] = data
        self.length += 1

    def pop(self):
        temp = self.array[self.length - 1]
        del self.array[self.length - 1]
        self.length -= 1
        return temp

    def peek(self):
        return self.array[self.length - 1]
