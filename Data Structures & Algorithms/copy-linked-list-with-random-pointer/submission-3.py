"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}

        def dfs(node):
            if node is None:
                return node

            if node not in seen:
                new_node = Node(node.val)
                seen[node] = new_node

                new_node.val = node.val
                new_node.next = dfs(node.next)
                new_node.random = dfs(node.random)
                return new_node
            else:
                return seen[node]

        return dfs(head)
