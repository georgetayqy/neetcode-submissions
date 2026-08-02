# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, max_so_far: int):
            if root is None:
                return 0

            result = 1 if root.val >= max_so_far else 0
            max_so_far = max(max_so_far, root.val)
            return result + dfs(root.left, max_so_far) + dfs(root.right, max_so_far)
        
        return dfs(root, -101)
