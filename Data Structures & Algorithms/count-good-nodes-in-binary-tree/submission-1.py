# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, value):
            if not node:
                return 0
            
            # check if the current node is good
            result = 1 if node.val >= value else 0
            
            # update max value so far
            value = max(value, node.val)

            # recurse on the left child and the right child
            result += dfs(node.left, value)
            result += dfs(node.right, value)

            # return the results
            return result
        
        # either -inf or the root's value is fine
        # since a root node is always good
        # return dfs(root, root.val)
        return dfs(root, -float("inf"))
