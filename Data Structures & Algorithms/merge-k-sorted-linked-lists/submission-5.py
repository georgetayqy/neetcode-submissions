# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
            return None
        
        def merge(l1, l2):
            starting_node = ListNode()
            start = starting_node

            while l1 and l2:
                if l1.val <= l2.val:
                    starting_node.next = l1
                    starting_node = starting_node.next
                    l1 = l1.next
                else:
                    starting_node.next = l2
                    starting_node = starting_node.next
                    l2 = l2.next

            if l1:
                starting_node.next = l1
            
            if l2:
                starting_node.next = l2
            
            return start.next
        
        def divide(lists, left, right):
            if left > right:
                return
            
            if left == right:
                return lists[left]
            
            middle = left + (right - left) // 2
            left_list = divide(lists, left, middle)
            right_list = divide(lists, middle + 1, right)

            return merge(left_list, right_list)
        
        return divide(lists, 0, len(lists) - 1)