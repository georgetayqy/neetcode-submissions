# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2

        if l2 is None:
            return l1
        
        results = ListNode()
        start = results

        while l1 and l2:
            current_val = l1.val + l2.val

            value = current_val % 10
            carry = current_val // 10

            new_node = ListNode(val=value)
            results.next = new_node
            results = new_node

            if carry > 0:
                if l1.next:
                    l1.next.val += carry
                else:
                    l1.next = ListNode(val=carry)
            
            l1 = l1.next
            l2 = l2.next
        
        to_propagate = l1 if l1 else l2

        while to_propagate:
            value = to_propagate.val % 10
            carry = to_propagate.val // 10

            next = ListNode(val=value)
            results.next = next
            results = results.next

            if carry > 0:
                if to_propagate.next:
                    to_propagate.next.val += carry
                else:
                    to_propagate.next = ListNode(val=carry)
            
            to_propagate = to_propagate.next

        
        return start.next
