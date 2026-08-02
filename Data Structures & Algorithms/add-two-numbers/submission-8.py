# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None
            
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            total = v1 + v2 + carry
            value, carry = total % 10, total // 10

            return ListNode(
                val=value,
                next=dfs(
                    l1.next if l1 else None,
                    l2.next if l2 else None,
                    carry
                )
            )
        
        return dfs(l1, l2, 0)
