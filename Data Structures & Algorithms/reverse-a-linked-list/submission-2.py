# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3 -> None
# None <- 1 <- 2 <- 3 (new head)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = None
        while head:
            next_item = head.next
            head.next = dummy
            dummy = head
            head = next_item
        
        return dummy


        