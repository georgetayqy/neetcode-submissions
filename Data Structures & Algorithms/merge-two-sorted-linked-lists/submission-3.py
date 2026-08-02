# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # this guards against the base case where list1 or list2 is exhausted and None is returned
        if list1 is None:
            return list2

        if list2 is None:
            return list1
        
        # we can exploit the fact that list1 and list2's order do not matter
        # we can always make the first argument of list1 the smaller element list
        # and we can do a 2 element assignment like this to make the process of finding
        # the smaller and bigger list faster
        current_node, next_node = (list1, list2) if list1.val < list2.val else (list2, list1)

        # we can now set the smaller element list's next element to the result of the merge
        # of the subsequent list, always making sure that list1 arg is the smaller element 
        # list while list2 arg is the larger element list
        current_node.next = self.mergeTwoLists(current_node.next, next_node)

        # return the current_node representing the start of the smaller list
        return current_node