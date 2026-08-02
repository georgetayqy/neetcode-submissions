# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([[root, -101]])
        results = 0

        while q:
            for i in range(len(q)):
                node, max_so_far = q.popleft()

                if node.val >= max_so_far:
                    results += 1
                
                max_so_far = max(max_so_far, node.val)

                if node.left:
                    q.append([node.left, max_so_far])

                if node.right:
                    q.append([node.right, max_so_far])

        return results
