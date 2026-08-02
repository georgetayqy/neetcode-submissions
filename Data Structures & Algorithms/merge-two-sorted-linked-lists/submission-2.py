# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        current_node = list1 if list1.val < list2.val else list2
        if current_node is list1:
            list1 = list1.next
        else:
            list2 = list2.next
        
        current_node.next = self.mergeTwoLists(list1, list2)
        return current_node