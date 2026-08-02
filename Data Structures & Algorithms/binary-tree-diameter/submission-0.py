# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # to track the longest diameter, we need to track
        # all possible diameters (height(head.left) + height(head.right))
        # of all nodes
        # we can do this using in-order traversal to compute all the heights
        # then use a global variable or some kind of max variable to track
        # the global max

        # this tracks the max diameter
        results = [0]
        
        # do in-order traversal
        def traverse(root, results):
            # once we reach the end, we 
            if root is None:
                return 0
            
            left = traverse(root.left, results)
            right = traverse(root.right, results)

            # current diameter is the sum of the left and right subtree heights
            results[0] = max(results[0], left + right)

            # need to return the height of the subtree (+1 for the current node)
            return 1 + max(left, right)
        
        traverse(root, results)
        return results[0]
