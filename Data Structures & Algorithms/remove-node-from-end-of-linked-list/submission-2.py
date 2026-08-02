# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverse(head)

        prev, current = None, head

        for i in range(n - 1):
            prev = current
            current = current.next
        
        if prev is None:
            # must be the only item in the list?
            return self.reverse(head.next)

        # prev links to the item we want to get rid of
        # current is the item to get rid of
        prev.next = current.next

        return self.reverse(head)

    
    def reverse(self, node):
        current = None

        while node:
            next_node = node.next
            node.next = current
            current = node
            node = next_node
        
        return current
