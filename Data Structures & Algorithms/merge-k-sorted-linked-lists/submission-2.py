# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        starting_node = ListNode()
        start = starting_node
        
        while True:
            num_none = 0
            min_node, min_idx = ListNode(val=float("inf")), -1

            for i in range(len(lists)):
                node = lists[i]

                if node is None:
                    print("node is None")
                    num_none += 1
                    continue
                
                if node.val < min_node.val:
                    min_node, min_idx = node, i
            
            if num_none == len(lists):
                starting_node.next = None
                break

            starting_node.next = min_node
            starting_node = starting_node.next
            lists[min_idx] = lists[min_idx].next

        return start.next
    
    
        
