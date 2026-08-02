# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def traverse(root):
            nonlocal max_path

            if not root:
                return 0
            
            max_left = max(traverse(root.left), 0)
            max_right = max(traverse(root.right), 0)

            max_path = max(
                max_path,
                max_left + max_right + root.val
            )

            return max(max_left + root.val, max_right + root.val)
        
        traverse(root)
        return max_path