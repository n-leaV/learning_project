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
        self.branch = None
        self.branchdict = None                      #creating a dict for branch/head pairs. the branch is the key and the head will be the value
    def insertTop(self, data):
        new_node = Node(data)
        if self.head is None:                       #if there is no head, the head becomes the new node
            self.head = new_node
            self.branchdict['main'] = self.head     #updating the head stored in the branch dict. branchdict now holds the right pointer
            return
        else:                                       #else, this node now points to the old head and the new node becomes the head
            new_node.next = self.head
            self.head = new_node
            self.branchdict['main'] = self.head

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:                       #if there is no head, the head becomes the new node
            self.head = new_node
            return
        current_node = self.head                    #start loop at head
        while(current_node.next):                        #loops until current_node == None, ie: loops until linked list terminates
            current_node = current_node.next        #sets current node to the node its pointing to
        current_node.next = new_node                #points the current node towards the newly created node, because of the loop, this is at the end of the list

    def insertIndex(self, data, index):             #index is counted from the head. if there is a branch, two indexes starting from different heads could access the same node
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
        self.branchdict['main'] = self.head                     #update the head stored in branchdict

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

    def printBranch(self):                                          #iterates from head down, will only print the branch its on
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def newBranch(self, data, index, branchname):                   #branchname must be a string. will have to add error checking to ensure duplicate names are not entered
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
            self.branchdict[branchname] = new_node                 #stores branchname/new_node pair in branch dict. does NOT update head. branchChange method will swap head
        else:print("No index found")

    def branchChange(self, branchname):
        self.head = self.branchdict[branchname]
        self.branch = branchname

    def printHead(self):
        print(self.branch)

        #make a list for each head and allow for swapping???
        #allow naming heads? how best to deal with this?
        #a dict with the name as the key? each dict val is the head of a seperate branch
        #would have to implement nameing in each method, initialise first as 'main'