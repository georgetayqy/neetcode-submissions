# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        if head.next is None:
            return False

        # tortoise and the hare
        slow, fast = head, head.next

        while fast is not None:
            if slow is fast:
                break

            slow = slow.next
            fast = fast.next
            
            if fast:
                fast = fast.next
        
        return fast is not None
