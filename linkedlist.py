#DISCLAIMER     DISCLAIMER      DISCLAIMER
#most of the code in this file is not my own. This code was generally sourced from https://www.geeksforgeeks.org/python-linked-list/
#This code is here to help me learn and better understand the operations of linked lists within python.
#Node.__init__() and Node.insertTop() were taken directly from the above link as a framwork for my learning. The rest has been worked out by me.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertTop(self, data):
        new_node = Node(data)
        if self.head is None:                       #if there is no head, the head becomes the new node
            self.head = new_node
            return
        else:                                       #else, this node now points to the old head and the new node becomes the head
            new_node.next = self.head
            self.head = new_node

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:                       #if there is no head, the head becomes the new node
            self.head = new_node
            return
        current_node = self.head                    #start loop at head
        while(current_node.next):                        #loops until current_node == None, ie: loops until linked list terminates
            current_node = current_node.next        #sets current node to the node its pointing to
        current_node.next = new_node                #points the current node towards the newly created node, because of the loop, this is at the end of the list

    def insertIndex(self, data, index):
        if (index == 0):
            self.insertTop(data)
        current_node = self.head
        placeholder = 0
        while(placeholder+1 != index and current_node != None):
            current_node = current_node.next
            placeholder+=1
        if (current_node != None):
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
        else:print("No index found")
    
    def update(self, val, index):
        current_node = self.head
        placeholder = 0
        if index == placeholder: current_node.data = val
        else:
            while(placeholder != index and current_node != None):
                current_node = current_node.next
                placeholder+=1
            if (current_node != None):
                current_node.data = val
            else: print('No index found')

    def deleteStart(self):
        if(self.head == None): return
        self.head = self.head.next

    def deleteEnd(self):
        if(self.head == None ): return
        current_node = self.head
        while(current_node.next != None and current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    def deleteIndex(self, index):
        if(self.head == None): return
        current_node = self.head
        placeholder = 0
        while(placeholder+1 != index and current_node != None):
            current_node = current_node.next
            placeholder+=1
        if (current_node != None):
                current_node.next = current_node.next.next
        else:print("No index found")

    def printList(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next