# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def recurseDeeply(root):
            if root is None:
                return 0
            
            left = recurseDeeply(root.left)
            right = recurseDeeply(root.right)

            if abs(left - right) > 1:
                self.isBalanced = False
            
            return 1 + max(left, right)

        recurseDeeply(root)
        return self.isBalanced
