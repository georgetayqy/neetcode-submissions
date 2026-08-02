class Node:
    def __init__(self, key, value, forward: "Node" = None, backward: "Node" = None):
        self.key = key
        self.value = value
        self.forward = forward
        self.backward = backward

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.head, self.tail = Node(None, None), Node(None, None)
        self.head.forward = self.tail
        self.tail.backward = self.head

    def get(self, key: int) -> int:
        value = self.key_to_node.get(key, Node(None, -1)).value
        self.bubble_up(key)
        return value

    def put(self, key: int, value: int) -> None:
        # updating the k-v pair
        if key in self.key_to_node:
            self.key_to_node[key].value = value
            self.bubble_up(key)
            self.traverse()
            return

        # add node to key-node set
        new_node = Node(key, value)

        # check if we need to evict the LRU
        while len(self.key_to_node) >= self.capacity:
            item_to_evict = self.evict()
            if item_to_evict is None:
                break

            del self.key_to_node[item_to_evict]

        self.key_to_node[key] = new_node

        # change the pointers
        # head <-> node <-> forward
        forward_from_head = self.head.forward
        
        self.head.forward = new_node
        new_node.backward = self.head
        
        new_node.forward = forward_from_head
        forward_from_head.backward = new_node
    
    def bubble_up(self, key: int) -> None:
        if key not in self.key_to_node:
            return

        node = self.key_to_node[key]
        if node.backward is self.head:
            # already at the top
            return
        
        # break away the node's dependencies
        prev = node.backward
        next = node.forward
        prev.forward = next
        next.backward = prev

        # take the current node, and shift to the front of the list
        next_in_line = self.head.forward
        node.backward = self.head
        self.head.forward = node
        node.forward = next_in_line
        next_in_line.backward = node
    
    def evict(self) -> int:
        # cannot evict if there is nothing in the list
        if self.tail.backward is self.head:
            return None

        victim = self.tail.backward
        preemptive = victim.backward

        preemptive.forward = self.tail
        self.tail.backward = preemptive

        return victim.key

    def traverse(self):
        head = self.head
        back = self.tail

        while head:
            print((head.key, head.value), end = " <-> ")
            head = head.forward

        print()

        while back:
            print((back.key, back.value), end = " <-> ")
            back = back.backward
        
        print()
        

