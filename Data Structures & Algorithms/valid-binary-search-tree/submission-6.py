# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def dfs(node, max_left, min_right):
            if not node:
                return True
            
            if not (max_left < node.val < min_right):
                return False
            
            return dfs(node.left, max_left, node.val) and dfs(node.right, node.val, min_right)
        
        return dfs(root, -float("inf"), float("inf"))
