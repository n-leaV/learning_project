#this file is used to develop a binary search tree framework to implement in future projects
#I am basing most of these concepts off of the my work in linkedlist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
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
        if new_node.data < self.root.data: next_node = new_node.left
        while(next_node != None):
            if (data < current_node.data and current_node.left!=None): current_node = current_node.left
            if (data > current_node.data and current_node.right!=None): current_node = current_node.right

           
