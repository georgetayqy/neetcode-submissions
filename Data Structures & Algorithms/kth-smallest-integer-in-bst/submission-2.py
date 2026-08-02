# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        num_element = 0
        stack = []
        current = root

        while current or stack:
            while current:
                # keep going left first to visit all left nodes
                stack.append(current)
                current = current.left

            # if we break out, it means that the current pointer is at the left most subtree
            # so we need to start popping, get the left most first and set it to current
            current = stack.pop()
            num_element += 1

            if num_element == k:  # guaranteed to always execute
                return current.val

            # attempt to visit the right subtree
            current = current.right
