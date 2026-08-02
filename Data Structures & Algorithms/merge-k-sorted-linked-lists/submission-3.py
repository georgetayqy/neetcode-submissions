# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        starting_node = ListNode()
        start = starting_node

        heap = []

        for i in range(len(lists)):
            node = lists[i]

            while node is not None:
                heapq.heappush(heap, (node.val, i))
                node = node.next
        
        while heap:
            _, index = heapq.heappop(heap)
            starting_node.next = lists[index]
            starting_node = starting_node.next
            lists[index] = lists[index].next
        
        return start.next
    
    
    
        
