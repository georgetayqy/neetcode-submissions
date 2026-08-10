class Node:
    def __init__(self, value, next: "Node" = None):
        self.value = value
        self.next = next

class MyHashSet:
    def __init__(self):
        self.prime_number = 43
        self.buckets = [None for i in range(self.prime_number)]

    def hash(self, value) -> int:
        return value % self.prime_number
    
    def get_hash_bucket_and_value(self, key) -> tuple[int, Node]:
        hash_value = self.hash(key)
        return hash_value, self.buckets[hash_value]

    def add(self, key: int) -> None:
        hash_value, node_of_interest = self.get_hash_bucket_and_value(key)

        if node_of_interest is None:
            self.buckets[hash_value] = Node(value=key)
        else:
            while node_of_interest is not None:
                if node_of_interest.value == key:
                    return
                
                if node_of_interest.next is None:
                    node_of_interest.next = Node(value=key)
                    return

                node_of_interest = node_of_interest.next

    def remove(self, key: int) -> None:
        hash_value, node_of_interest = self.get_hash_bucket_and_value(key)

        if node_of_interest is None:
            return

        # if node_of_interest.next is None and node_of_interest.value == key:
        #     self.buckets[hash_value] = node_of_interest.next
        #     return
        
        previous = None
        while node_of_interest:
            if node_of_interest.value == key:
                if previous:
                    previous.next = node_of_interest.next
                    return
                else:
                    self.buckets[hash_value] = node_of_interest.next
                    return

            previous = node_of_interest
            node_of_interest = node_of_interest.next

    def contains(self, key: int) -> bool:
        hash_value, node_of_interest = self.get_hash_bucket_and_value(key)

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