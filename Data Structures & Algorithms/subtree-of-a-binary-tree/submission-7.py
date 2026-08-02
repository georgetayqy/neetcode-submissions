# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)

    def isSameTree(self, source, dest):
        if not source and not dest:
            return True
        
        if not source or not dest or source.val != dest.val:
            return False
        
        return self.isSameTree(source.left, dest.left) \
            and self.isSameTree(source.right, dest.right)
