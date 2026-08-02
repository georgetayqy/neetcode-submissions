# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        first = dummy

        while l1 and l2:
            vals = l1.val + l2.val + carry
            vals, carry = vals % 10, vals // 10

            dummy.next = ListNode(val=vals)
            dummy = dummy.next
            l1, l2 = l1.next, l2.next
        
        while l1:
            vals = l1.val + carry
            vals, carry = vals % 10, vals // 10
            dummy.next = ListNode(val=vals)
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            vals = l2.val + carry
            vals, carry = vals % 10, vals // 10
            dummy.next = ListNode(val=vals)
            dummy = dummy.next
            l2 = l2.next
        
        if carry:
            dummy.next = ListNode(val=carry)
        
        return first.next
