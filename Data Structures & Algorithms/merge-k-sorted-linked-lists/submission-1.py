# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        return self.mergeCoroutine(lists, 0, len(lists) - 1)
        
    def mergeCoroutine(self, ls, start, end):
        if start == end:
            return ls[start]
        elif start > end:
            return None
        else:
            mid = start + (end - start) // 2
            left = self.mergeCoroutine(ls, start, mid)
            right = self.mergeCoroutine(ls, mid + 1, end)

            return self.merge(left, right)
    
    def merge(self, ls1, ls2):
        if ls1 is None:
            return ls2
        
        if ls2 is None:
            return ls1
        
        if ls1.val <= ls2.val:
            ls1.next = self.merge(ls1.next, ls2)
            return ls1
        else:
            ls2.next = self.merge(ls1, ls2.next)
            return ls2
