class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def createLinkListAppendAtLast(self,head,d):
        end=Node(d)

        if head is None:
            return
        while(head.next!=None):
            head.next=end
            end.next=None


    createLinkListAppendAtLast(2,3)