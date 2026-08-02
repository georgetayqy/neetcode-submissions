# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = [[root.val]]
        q = deque()
        q.append(root)

        while q:
            curr_vals = []

            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    curr_vals.append(node.left.val)
                    q.append(node.left)
                
                if node.right:
                    curr_vals.append(node.right.val)
                    q.append(node.right)

            if curr_vals:
                results.append(curr_vals)

        return results
        