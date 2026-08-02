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

        levels = []
        queue = deque()
        queue.append(root)

        # do a BFS
        while queue:
            current_level = []

            for i in range(len(queue)):
                current_item = queue.popleft()
                current_level.append(current_item.val)

                if current_item.left:
                    queue.append(current_item.left)
                
                if current_item.right:
                    queue.append(current_item.right)
            
            levels.append(current_level)

        return levels
        