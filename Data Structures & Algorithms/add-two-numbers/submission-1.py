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
        carry = 0

        # this condition perfectly account for unequal length list
        # and if we still have a final carry to add on to the result list as a carry
        while l1 or l2 or carry:
            # rather than adding the carry on to the next node, we abstract it out as a seperate variable
            # and use it to check if we still need to carry on
            current_val = carry
            
            # we only add if there are still things to check
            if l1:
                current_val += l1.val
            
            # we only add if there are still things to check
            if l2:
                current_val += l2.val

            # compute remainder and quotient
            value = current_val % 10
            carry = current_val // 10

            # add the resulting values to the result list
            new_node = ListNode(val=value)
            results.next = new_node
            results = new_node
            
            # advance l1 forward if l1 still has something
            if l1:
                l1 = l1.next
            
            # advance l2 forward if l2 still has something
            if l2:
                l2 = l2.next
        
        return start.next
