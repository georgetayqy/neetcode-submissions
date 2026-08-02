# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0
        current = root
        
        while current or stack:
            while current:
                # keep traversing left, but remember to append the current node
                # to stack for backtracking
                stack.append(current)
                current = current.left
            
            # process current
            current = stack.pop()
            count += 1

            # guaranteed to execute
            if count == k:
                # current node is the kth value
                return current.val

            # go to the right and process now
            current = current.right
