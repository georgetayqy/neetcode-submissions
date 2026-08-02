from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # level order traversal but we take the right most element?
        elements = []
        queue = deque()
        queue.append(root)

        while queue:
            print(queue)
            elements.append(queue[-1].val)

            for i in range(len(queue)):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
        
        return elements
