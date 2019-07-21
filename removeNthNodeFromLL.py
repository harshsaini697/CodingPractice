class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
def removeNthFromEnd( head, n: int):
    count = 0
    dummy = head
    while (head.next != None):
        head = head.next
        count += 1
    if n == count + 1:
        return dummy.next.val
    head=dummy
    i = 0
    if n == 1:
        while (head.next!= None):
            if i == n-1 :
                head.next = None
                i += 1
        return head.val
    i = 0
    head = dummy
    if n > 1 and n != count:
        while (i != count - n):
            i += 1
            head = head.next
        head.next = head.next.next
    return dummy.val


head=ListNode(1)
head.next=ListNode(2)
print(removeNthFromEnd(head,1))