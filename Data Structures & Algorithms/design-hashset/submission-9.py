class MyHashSet:

    def __init__(self):
        self.prime_number = 43
        self.buckets = [[] for i in range(self.prime_number)]

    def hash(self, key: int) -> int:
        return key % self.prime_number

    def add(self, key: int) -> None:
        hash = self.hash(key)

        if not self.buckets[hash] or not self.contains(key):
            self.buckets[hash].append(key)

    def remove(self, key: int) -> None:
        hash = self.hash(key)

        if not self.buckets[hash]:
            return
        
        try:
            self.buckets[hash].remove(key)
        except ValueError:
            return

    def contains(self, key: int) -> bool:
        hash = self.hash(key)

        for value in self.buckets[hash]:
            if value == key:
                return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)