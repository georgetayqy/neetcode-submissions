# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, -101)])
        results = 0
    
        while q:
            for i in range(len(q)):
                curr, step = q.popleft()
                if curr is None:
                    continue

                print(curr.val, step)

                if curr.val >= step:
                    print("curr is > step")
                    results += 1
                
                q.append((curr.left, max(curr.val, step)))
                q.append((curr.right, max(curr.val, step)))
        
        return results
