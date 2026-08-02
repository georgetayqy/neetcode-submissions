# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        iterator = head

        while iterator is not None:
            iterator = iterator.next
            length += 1

        if length == 1:
            return None
        
        iterations = length - n
        iterator = head

        if iterations == 0:
            return head.next

        for i in range(iterations - 1):
            iterator = iterator.next
        
        if iterator.next:
            iterator.next = iterator.next.next
        
        return head

