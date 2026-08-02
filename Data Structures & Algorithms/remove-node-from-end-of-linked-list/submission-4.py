# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        actualNode = length - n

        prev, curr = None, head

        for i in range(actualNode):
            prev = curr
            curr = curr.next

        if prev is None:
            return head.next

        prev.next = curr.next
        return head

    def getLength(self, head):
        length = 0

        while head:
            head = head.next
            length += 1
        
        return length