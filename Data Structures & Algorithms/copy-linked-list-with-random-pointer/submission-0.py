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
        if not head:
            return head

        # maps old nodes to the new nodes
        self.mapping = {}
        
        copy_list = self.copy(head)

        # self.copy_random(head, copy_list)
        return copy_list
    
    def copy(self, node):
        if node is None:
            return None

        # idea is to hash the mapping
        if node in self.mapping:
            return self.mapping[node]

        # create a new node if it doesnt exist in the hashmap
        new_node = Node(node.val)

        # add it to the hashmap
        self.mapping[node] = new_node

        # set the next pointer (once this recursion runs completely,
        # the mapping is guaranteed to have all of the nodes ever created)
        new_node.next = self.copy(node.next)

        # this call merely retrieves the next random node for all nodes
        # in the list
        new_node.random = self.copy(node.random)

        return new_node
