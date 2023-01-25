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
    inNode = Node(data)
    targetNode = self.target(self.root, data)
    if data < targetNode.data:
      targetNode.left = inNode
    else:
      targetNode.right = inNode 
      
  def target(self, passNode, data):
    currNode = passNode
    if (data < currNode.data and currNode.left is None) or (data > currNode.data and currNode.right is None):
      return currNode
    elif data < currNode.data:
      currNode = currNode.left
      self.target(currNode, data)
    else:
      currNode = currNode.right
      self.target(currNode, data)

  def traverse(self, checkArray, doneArray):
    nodes = checkArray
    outArray = doneArray
    if len(nodes) == 0:
      return outArray
    else:
      if nodes[0].left is not None:
        nodes.append(nodes[0].left)
      if nodes[0].right is not None:
        nodes.append(nodes[0].right)
      outArray.append(nodes.pop(0))  
      self.traverse(nodes, outArray)
  
  def print(self):
    nodeArray = [self.root]
    outArray = []
    printArray = self.traverse(nodeArray, outArray)
    for i in range(len(printArray)):
      print(printArray[i])