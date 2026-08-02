# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levels = []

        self.bfs(levels, root, 0)
        return levels
    
    def bfs(self, all_levels, node, level):
        if node is None:
            return
        
        if len(all_levels) == level:
            # if we are at the current level, we need to add a new level to
            # the all levels
            # if level is 0, we need to have a levels list of length 1
            # if level is 1, we need to have a levels list of length 2
            # ...
            # if we are at level n, we need to have a levels list of length n + 1
            # hence, we check if the all_levels length is equal to level,
            # and if so, we append it to the all_levels list
            all_levels.append([])
        
        all_levels[level].append(node.val)
        
        if node.left:
            self.bfs(all_levels, node.left, level + 1)
        
        if node.right:
            self.bfs(all_levels, node.right, level + 1)

