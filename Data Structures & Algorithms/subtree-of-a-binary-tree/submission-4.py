# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, startroot):
            if startroot is None:
                return True
            
            # no need to do redundant [and startroot is None]
            if root is None:
                return False
            
            if isEqual(root, startroot):
                return True
            
            # if they are not the same subtree, it is possible that the
            # children of the root might be the subtree we are looking for
            return dfs(root.left, startroot) or dfs(root.right, startroot)
        
        def isEqual(r1, r2):
            if r1 is None and r2 is None:
                return True
            
            if r1 is None or r2 is None or r1.val != r2.val:
                return False
        
            return isEqual(r1.left, r2.left) and isEqual(r1.right, r2.right)

        return dfs(root, subRoot)
