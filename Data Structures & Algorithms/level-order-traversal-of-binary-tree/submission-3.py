# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # BFS
        q = deque([root])
        results = []

        while q:
            to_append = []

            for i in range(len(q)):
                current = q.popleft()
                
                if current.left:
                    q.append(current.left)
                
                if current.right:
                    q.append(current.right)
                
                to_append.append(current.val)
            
            results.append(to_append)

        return results
            