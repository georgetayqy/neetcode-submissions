# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if there is nothing at the subRoot, it is a subtree of the root
        if not subRoot:
            return True

        # if root is None, then cannot possibly be a subtree
        if not root:
            return False

        # check if they are subtrees
        # we cannot just check to find if the values are equal then terminate with True
        # cuz it is possible that the they are not subtrees at all
        # [1 <- 1], [1], if we terminate early, we won't get the correct ans
        # since [1] is not exactly a subtree of [1 <- 1], but it is a subtree of
        # [1 <- ]
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, left, right):
        # if both are None, then they are equal
        if not left and not right:
            return True

        # if both are present and the values are equal
        if left and right and left.val == right.val:
            return self.isSameTree(left.left, right.left) and self.isSameTree(left.right, right.right)

        return False
