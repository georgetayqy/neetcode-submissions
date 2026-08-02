# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        # flip the roots
        q = [root]
        
        while q:
            current = q.pop()
            current.left, current.right = current.right, current.left

            if current.left:
                q.append(current.left)
            
            if current.right:
                q.append(current.right)
        
        return root
