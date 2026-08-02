# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we only find the lowest common ancestor when there is
        # a split in where we search
        # O(log n), since we only explore 1 node in each level of the tree

        if root.val < p.val and root.val < q.val:
            # if both p and q are larger than the root, 
            # we explore the right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            # if both p and q are smaller than the root,
            # we explore the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # if we end up splitting or if we have found
            # a node that is equal to either p or q, then we just
            # return the root as the LCA
            
            # for equality, e.g. p=6, q=7, 5 <- 6 -> 7
            # no matter which branch we take, we will end up such that
            # p can no longer be found in either of the branches
            # if this is the case, then we need to return the root itself
            # as the LCA
            return root