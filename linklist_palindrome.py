class Node:
    def __init__(self,data):
        self.head=data
        self.next=None

def isPalinDrome(self,head):
    fast=slow=head

    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next

    node=None
    while slow:
        nxt=slow.next
        slow.next=node
        node=slow
        slow=nxt

    while node: #while
        if node:




