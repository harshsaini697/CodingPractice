class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


    def printList(head):
        while(head!=None):
            print(head.data,end=" ")
            head=head.next

    def insert(head,data):
        if head==None:# empty list
            head=Node(data)
            head.next=None

        elif head.next==None:  #last ndoe
            head.next=Node(data)
            head.next.next=None

        elif head.next!=None: #middle node
            while(head.next!=None):
                head=head.next
            head.next=Node(data)
            head.next.next=None


    def nodedelete(head,data):
        if head.data!=None and head.data!=data:
            while head.data!=data:
                prev=head
                head=head.next
            if(head.next==None): #last node
                    prev.next=None
            elif(head.next!=None):
                    prev.next=head.next
        elif head.data==data:
            temp=head
            del temp
            head=head.next
        else:
            return head
        return head

    # def sort(head):
        # nodes=[]
        # while (head != None):
        #     #print(head.data, end=" ")
        #     nodes.append(head)
        #     head = head.next
        #
        # nodes = sorted(nodes, key=lambda node: node.data)
        # return  nodes
    def mergeSorted( head):
        if not (head and head.next): return head
        mid=head
        tail=head.next
        while tail and tail.next:
            mid,tail=mid.next,tail.next.next
        mid.next,mid= None,mid.next
        return Node.merge(Node.mergeSorted(head),Node.mergeSorted(mid))

    def merge(l1,l2):
        head=node=Node(0)
        while l1 and l2:
            if l1.data<l2.data :
                node.next
                l1=l1
                l1.next
            else:
                node.next
                l2=l2
                l2.next

            node.next
        node.next=l1 or l2

        return head.next




if __name__ == '__main__':
    head=Node(1)
    Node.insert(head,2)
    Node.insert(head,3)
    Node.insert(head,32)
    #Node.printList(head)
    print()
    head=Node.nodedelete(head,1)

    #Node.printList(head)
    head=Node.mergeSorted(head)

    Node.printList(head)


