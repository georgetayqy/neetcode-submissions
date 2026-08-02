# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first, second = head, slow.next
        slow.next = None

        # reverse the second list
        dummy = None
        second_clone = second

        while second_clone is not None:
            next_ref = second_clone.next
            second_clone.next = dummy
            dummy = second_clone
            second_clone = next_ref

        # merge the two lists
        first, second = head, dummy
        dummy2 = ListNode()

        while first and second:
            dummy2.next = first
            first = first.next
            dummy2 = dummy2.next

            dummy2.next = second
            second = second.next
            dummy2 = dummy2.next

        dummy2.next = first if first else second
