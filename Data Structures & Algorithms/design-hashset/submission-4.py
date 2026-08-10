class Node:
    def __init__(self, value, next: "Node" = None):
        self.value = value
        self.next = next

class MyHashSet:
    def __init__(self):
        self.prime_number = 1_000_001
        self.buckets = [None for i in range(self.prime_number)]
    
    def get_hash_bucket_and_value(self, key) -> Node:
        return self.buckets[key]

    def add(self, key: int) -> None:
        node_of_interest = self.get_hash_bucket_and_value(key)

        if node_of_interest is None:
            self.buckets[key] = Node(value=key)
        else:
            while node_of_interest is not None:
                if node_of_interest.value == key:
                    return
                
                if node_of_interest.next is None:
                    node_of_interest.next = Node(value=key)
                    return

                node_of_interest = node_of_interest.next

    def remove(self, key: int) -> None:
        node_of_interest = self.get_hash_bucket_and_value(key)

        if node_of_interest is None:
            return
        
        previous = None
        while node_of_interest:
            if node_of_interest.value == key:
                if previous:
                    previous.next = node_of_interest.next
                    return
                else:
                    self.buckets[key] = node_of_interest.next
                    return

            previous = node_of_interest
            node_of_interest = node_of_interest.next

    def contains(self, key: int) -> bool:
        node_of_interest = self.get_hash_bucket_and_value(key)

        while node_of_interest:
            if node_of_interest.value == key:
                return True
            node_of_interest = node_of_interest.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)