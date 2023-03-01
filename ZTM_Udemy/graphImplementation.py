class Graph():

    def __init__(self):
        self.num_nodes = 0
        self.adj_list = dict()

    def addVertex(self, node):
        self.adj_list.update({node: None})
        self.num_nodes += 1

    def addEdge(self, node1, node2):
        temp_list = self.adj_list.get(node1)
        if temp_list is None:
            temp_list = [node2]
        else:
            temp_list.append(node2)
        temp_list.sort()
        self.adj_list.update({node1: temp_list})

        temp_list = self.adj_list.get(node2)
        if temp_list is None:
            temp_list = [node1]
        else:
            temp_list.append(node1)
        temp_list.sort()
        self.adj_list.update({node2: temp_list})

    def showEdges(self):
        for item in self.adj_list:
            print(str(item) + "-->" + str(self.adj_list[item]))
