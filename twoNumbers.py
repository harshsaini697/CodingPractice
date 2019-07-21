class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    l_final:ListNode
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        while(l1.next!=None):
            l_final.next=l1.val+l2.val
            l1.next
            l2.next

