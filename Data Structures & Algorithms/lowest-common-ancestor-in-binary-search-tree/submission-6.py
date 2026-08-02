# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # LCA only occurs when the search paths diverge
        if not root or not p or not q:
            return None

        p, q = sorted([p, q], key=lambda x: x.val)

        head = root
        while head:
            if p.val <= head.val <= q.val:
                # if the root is between the p and q, then we have found the LCA
                return head
            elif p.val < head.val and q.val < head.val:
                # if all are smaller than p, then the LCA must be on the left
                head = head.left
            elif p.val > head.val and p.val > head.val:
                # if all are larget than p, then the LCA must be on the right
                head = head.right
