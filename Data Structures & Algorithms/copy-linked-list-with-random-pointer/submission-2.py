"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    old2new = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a map of old node to new node

        if head is None:
            return head
        
        return deepcopy(head)

    def deepcopy(self, node):
        if node is None:
            return None
        
        if node in old2new:
            return old2new[node]

        new = Node(node.x)
        old2new[node] = new

        new.next = self.deepcopy(node.next)
        new.random = self.deepcopy(node.random)

        return new
