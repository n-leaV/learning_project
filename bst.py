#this file is used to develop a binary search tree framework to implement in future projects
#I am basing most of these concepts off of the my work in linkedlist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        if new_node.data == self.root.data:                     #not allowing duplicate values
            print("Data already entered")
            return
        current_node = self.root
        if new_node.data < current_node.data: next_node = current_node.left
        else: next_node = current_node.right
        while(next_node != None):
            if new_node.data == current_node.data:                     #not allowing duplicate values
                print("Data already entered")
                return
            if new_node.data < current_node.data: next_node = new_node.left
            else: next_node = new_node.right
            if next_node != None: current_node = next_node
            #if (data < current_node.data and current_node.left!=None): current_node = current_node.left
            #if (data > current_node.data and current_node.right!=None): current_node = current_node.right
  
        if (current_node.left is None and new_node.data < current_node.data): current_node.left = new_node
        if (current_node.right is None and new_node.data > current_node.data): current_node.right = new_node

    def inOrder(self):
        current_node = self.root
        while(current_node != None):
            if current_node is not None:
                print (current_node.data)

