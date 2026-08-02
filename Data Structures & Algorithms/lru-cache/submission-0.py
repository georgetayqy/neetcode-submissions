"""
We need a node class to form the doubly linked list
"""

class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # need a hashmap to store the key to point to the node
        self.cache = {}

        # store the capacity here also
        self.capacity = capacity

        # use 2 dummy nodes here to prevent out of bounds
        self.head_lru, self.tail_lru = Node(val=None), Node(val=None)
        
        # link up the dummy nodes to allow addition of nodes between
        # the 2 nodes
        self.head_lru.next, self.tail_lru.prev = self.tail_lru, self.head_lru

    def get(self, key: int) -> int:
        value = -1

        # if the key is in the cache, we can return it directly
        if key in self.cache:
            value = self.cache[key].val

            # but we need to push it to the top
            self.put(key, value)

        return value
    
    def remove(self, node):
        """
        Removes a node from the doubly linked list
        """
        
        # SAFE SINCE THE ENDS ARE DUMMY NODES
        # WORKS EVEN WHEN THERE IS ONLY 1 ITEM TO DELETE IN THE LIST
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self, node):
        """
        Insert a node at the end (the right) of the list
        """

        # add this to the front of the linked list
        # head of LL <-> dummy node
        # reassign dummy node <- to the new node
        # reassign LL -> to the new node
        # reassign node -> dummy node
        # reassign LL <- node
        # get LL <-> node <-> dummy node
        previous, next = self.tail_lru.prev, self.tail_lru
        previous.next, node.prev = node, previous
        node.next, next.prev = next, node

    def put(self, key: int, value: int) -> None:
        # if it is in the cache, we remove it
        # since a node already exists with the same key value
        # so we need to remove it from our list to make it unique
        if key in self.cache:
            self.remove(self.cache[key])
        
        # re-add it back to the cache
        self.cache[key] = Node(key, value)

        # insert the node into the end of the LL
        self.add(self.cache[key])

        # need to make sure that we do not exceed the capacity here
        if len(self.cache) > self.capacity:
            # note that the head and tail LRU nodes are dummy nodes
            # so we should reference head_lru.next
            lru = self.head_lru.next

            # remove the LRU item from the list
            self.remove(lru)

            # delete it from the hashmap
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)