# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # BFS
        q = deque([root])
        results = []

        while q:
            length = len(q)
            for i in range(length):
                current = q.popleft()

                if i == length - 1:
                    results.append(current.val)
                
                if current.left:
                    q.append(current.left)
                
                if current.right:
                    q.append(current.right)
        
        return results
