"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        self.clonemap = {}
        return self.clone(node)
    
    def clone(self, node):
        # check if it is already cloned, if so, just reuse the cloned copy
        # when building the clone
        # this is necessary to prevent us from recloning a previously cloned
        # node to prevent recursive loops
        if node in self.clonemap:
            return self.clonemap[node]
        
        # if it is a new unseen node, then we add it to the clone map
        # and create a clone as well
        cloned = Node(val=node.val, neighbors=[])
        self.clonemap[node] = cloned

        # check each neighbour and recursively clone them as well
        for neighbour in node.neighbors:
            # add the clones of the neighbor to the current clone
            cloned.neighbors.append(self.clone(neighbour))

        # after are done, we return the cloned root of the graph
        return cloned
