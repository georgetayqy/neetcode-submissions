# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return (0, True)
            
            left_height, left_bal = dfs(node.left)
            right_height, right_bal = dfs(node.right)

            return (max(left_height, right_height) + 1, 
            left_bal and right_bal and abs(left_height - right_height) <= 1)
        
        return dfs(root)[-1]
            
            