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
        # if iterative, then we need minimally 2 passes
        if not head:
            return None

        # hashmap to store the old to new mappings
        # we put None: None here to prevent the below indexing operations from
        # accessing a None value that maps to nothing
        past = {None: None}
        
        curr = head
        while curr:
            # clone the nodes first, DO NOT LINK IT YET
            copied = Node(x=curr.val)
            past[curr] = copied
            curr = curr.next

        curr = head
        while curr:
            # we link it here
            copied = past[curr]

            # we know that we created a copy of all nodes
            # no need to check that curr.next and curr.random is not None
            copied.next = past[curr.next]
            copied.random = past[curr.random]
            curr = curr.next
        
        return past[head]