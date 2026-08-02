# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            curr_sum = l1.val + l2.val + carry

            carry = curr_sum // 10
            curr_sum = curr_sum % 10

            dummy.next = ListNode(curr_sum)
            dummy = dummy.next

            l1 = l1.next
            l2 = l2.next
        
        to_add = l1 if l1 else l2

        while to_add:
            add_sum = carry + to_add.val

            carry = add_sum // 10
            add_sum = add_sum % 10
            dummy.next = ListNode(add_sum)
            dummy = dummy.next
            to_add = to_add.next

        if carry > 0:
            dummy.next = ListNode(val=carry)
        
        return head.next