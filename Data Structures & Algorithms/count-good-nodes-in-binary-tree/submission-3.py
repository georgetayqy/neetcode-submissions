# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(root: TreeNode, max_so_far: int):
            nonlocal good

            if root is None:
                return

            good += (1 if root.val >= max_so_far else 0)
            max_so_far = max(max_so_far, root.val)
            
            dfs(root.left, max_so_far)
            dfs(root.right, max_so_far)
        
        dfs(root, -101)
        return good
