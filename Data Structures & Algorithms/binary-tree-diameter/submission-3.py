# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def diam(node):
            nonlocal max_diam

            if node is None:
                return 0
            
            left_height = diam(node.left)
            right_height = diam(node.right)
            max_diam = max(max_diam, left_height + right_height)
            
            return 1 + max(left_height, right_height)

        diam(root)
        return max_diam