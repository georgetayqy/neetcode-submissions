# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, alpha, beta):
            # alpha-beta
            # if left branch, we need to update the beta boundary
            # if right branch, we need to update the alpha boundary
            # ensure that alpha < node.val < beta

            if root is None:
                return True
            
            if not (root.val < beta and root.val > alpha):
                # broken
                return False
            
            # alpha remains the same since we are going left
            # update beta boundary to the node's value
            left_valid = dfs(root.left, alpha, root.val)

            # beta remainds the same since we are going right
            # update alpha boundary to the node's value
            right_valid = dfs(root.right, root.val, beta)

            # return logical and of both conditions
            return left_valid and right_valid

        return dfs(root, float("-inf"), float("inf"))
