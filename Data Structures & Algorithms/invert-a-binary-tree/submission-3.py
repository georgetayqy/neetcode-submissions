# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        # flip the roots
        root.left, root.right = root.right, root.left
        
        # recurse deeper
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        # return the root of the tree
        return root
