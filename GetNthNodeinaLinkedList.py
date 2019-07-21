class Node:
    def __init__(self,val):
        self.val=val  #Assign Data
        self.next=None #Assign Next Node

class LinkedList:
    def __init__(self):
        self.head=None
    #Assign numbers at the front of the linkedlist
    def push(self,num):
        new_node=Node(num)
        new_node.next=self.head
        self.head=new_node

    def gNth(self,num):
        dummy=self.head
        count=0

        while(dummy):
            if(count==num):
                return dummy.val
            count+=1
            dummy=dummy.next
        return False


llist = LinkedList()

# Use push() to construct below list
# 1->12->1->4->1
llist.push(1)
llist.push(4)
llist.push(1)
llist.push(12)
llist.push(1)
n = 3
print ("Element at index 3 is :", llist.gNth(n))

