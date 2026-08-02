# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = None

        for ls in lists:
            answer = self.merge(answer, ls)
        
        return answer
    
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
