# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        curr = head

        while curr:
            next_in_line = curr.next
            curr.next = previous
            previous = curr
            curr = next_in_line
        
        return previous
