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
        queue = deque([root])

        while queue:
            # for each level, we take the right most element
            rightmost = None
            # elements.append(queue[-1].val)

            # remove all nodes in the queue and append its children
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr:
                    # rightmost will have the last node in the queue
                    rightmost = curr

                    # we know it must be a valid node
                    queue.append(curr.left)
                    queue.append(curr.right)

            if rightmost:
                elements.append(rightmost.val)

        # return list of elements
        return elements
