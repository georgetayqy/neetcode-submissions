# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Start at the root, we say that the root must be between
        # left := -inf and right := inf
        # A node is a valid BST if its node value is between the left
        # and right boundary

        # When going down to the left subtree, we need to check that
        # all nodes in the left subtree are < node value
        # Where does the < condition come into play? THE `right` VARIABLE!
        # WHEN DESCENDING DOWN THE LEFT SUBTREE, UPDATE THE RIGHT BOUND

        # When going down the right subtree, we need tot check that all
        # nodes in the right subtree are > node value
        # THE `left` VARIABLE COMES INTO PLAY HERE
        # WHEN DESCENDING DOWN THE RIGHT SUBTREE, UPDATE THE LEFT BOUND
        def isValid(root, left_max, right_min):
            if not root:
                return True
            
            if root.val <= left_max or root.val >= right_min:
                return False
            
            return isValid(root.left, left_max, root.val) and \
                isValid(root.right, root.val, right_min)
        
        return isValid(root, float("-inf"), float("inf"))
