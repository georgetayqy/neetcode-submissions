# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_q, q_q = deque([p]), deque([q])

        while p_q and q_q:
            if len(p_q) != len(q_q):
                return False
            
            for i in range(len(p_q)):
                p_item, q_item = p_q.popleft(), q_q.popleft()

                if not p_item and not q_item:
                    continue

                if not p_item or not q_item or p_item.val != q_item.val:
                    return False
                
                p_q.append(p_item.left)
                p_q.append(p_item.right)
                q_q.append(q_item.left)
                q_q.append(q_item.right)

        return len(p_q) == len(q_q) == 0
