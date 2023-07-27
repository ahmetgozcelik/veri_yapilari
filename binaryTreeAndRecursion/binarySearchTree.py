class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None

    #insert
    def insert(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return True
        
        tempNode = self.root

        while True:
            if newNode.value == tempNode.value:
                return False
            
            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left
            else:
                if tempNode.riht is None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self, value):
        tempNode = self.root

        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            else:
                return True
        return False
    
    def minOfNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode
    
    def maxOfNode(self, currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode


myTree = binarySearchTree()


print(myTree.insert(15))
print(myTree.contains(15))
print(myTree.insert(10))
print(myTree.contains(20))
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.minOfNode(myTree.root).value)
print(myTree.maxOfNode(myTree.root).value)