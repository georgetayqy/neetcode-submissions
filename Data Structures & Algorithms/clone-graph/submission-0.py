"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        if len(node.neighbors) == 0:
            # empty graph
            return Node(val=node.val)
        
        self.new_nodes = {}
        return self.clone(node)

    
    def clone(self, original):
        if len(original.neighbors) == 0:
            return Node(val=original.val, neighbors=[])
        
        head = Node(val=original.val, neighbors=[])
        self.new_nodes[original.val] = head

        for neighbor in original.neighbors:
            if neighbor.val in self.new_nodes:
                head.neighbors.append(self.new_nodes[neighbor.val])
            else:
                new_neighbor = self.clone(neighbor)
                self.new_nodes[neighbor.val] = new_neighbor
                head.neighbors.append(self.clone(neighbor))
        
        return head

        
        