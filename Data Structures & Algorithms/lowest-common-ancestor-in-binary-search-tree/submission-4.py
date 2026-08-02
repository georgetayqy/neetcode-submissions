# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # LCA only occurs when the search paths diverge
        p, q = sorted([p, q], key=lambda x: x.val)

        if p.val <= root.val <= q.val:
            return root
        
        if p.left is q or p.right is q:
            return p
        
        if q.left is p or q.right is p:
            return q

        if p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val >= root.val and p.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        
