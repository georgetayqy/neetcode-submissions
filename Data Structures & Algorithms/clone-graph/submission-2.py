"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node

        # map from old node to new node to find the new node
        old2new = {}

        def dfs(node):
            if node in old2new:
                return old2new[node]
            
            # if its not found in the map of existing nodes, we must
            # create a replica and set it to the old node
            new_node = Node(node.val)
            old2new[node] = new_node

            # check all of its neighbours, append the cloned neighbours to
            # the neighbour list
            for neighbour in node.neighbors:
                old2new[node].neighbors.append(dfs(neighbour))

            # at the end, return the current CLONED node
            return old2new[node]
        
        return dfs(node)