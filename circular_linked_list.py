class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularLinkList:
    def __init__(self):
        self.head=None

#function to insert a node
    def push(self,data):
        node1=Node(data)
        temp=self.head
        node1.next=self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp=temp.next
            temp.next=node1
        else:
            node1.next=node1

        self.head=node1


#fn to print the nodes:
    def printList(self,head):
        temp = self.head
        if self.head is not None:
            while (True):
                print("%d" % temp.data),
                temp = temp.next
                if (temp == self.head):
                    break




    def deleteNode(self,mydata):
        if self.head ==None:
            return
        temp=self.head
        prev=Node(0)
        while (temp.data != mydata):
            if(temp.next==self.head):
                print("Not in List")
                break
            prev=temp
            temp=temp.next
        if(temp==self.head):
            prev=self.head
            while(prev.next!=self.head):
                prev=prev.next
            self.head=temp.next
            prev.next=self.head
        elif(temp.next == self.head):
            prev.next=self.head
        else:
            prev.next=temp.next
        return self.head


if __name__ == '__main__':
    cc=circularLinkList()

    cc.push(1)
    cc.push(2)
    cc.push(3)
    cc.push(4)

    cc.printList(3)
    cc.deleteNode(4)
    cc.printList(3)
