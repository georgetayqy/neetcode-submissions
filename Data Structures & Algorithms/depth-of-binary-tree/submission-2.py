from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque()
        q.append(root)
        num_depth = 0

        while q:
            to_append = []

            for node in q:
                if node.left:
                    to_append.append(node.left)
                
                if node.right:
                    to_append.append(node.right)

            q.clear()
            q.extend(to_append)
            num_depth += 1
        
        return num_depth
        
    