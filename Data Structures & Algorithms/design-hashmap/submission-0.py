class MyHashMap:

    def __init__(self):
        self.prime_number = 43
        self.buckets = [[] for i in range(self.prime_number)]
    
    def hash(self, key):
        return key % self.prime_number

    def put(self, key: int, value: int) -> None:
        hash = self.hash(key)
        hash_bucket = self.buckets[hash]
        if not hash_bucket:
            self.buckets[hash].append([key, value])
            return
        
        for i in range(len(hash_bucket)):
            bucket_key, bucket_value = hash_bucket[i]

            if key == bucket_key:
                hash_bucket[i][-1] = value

    def get(self, key: int) -> int:
        hash = self.hash(key)

        for k, v in self.buckets[hash]:
            if key == k:
                return v
        
        return -1

    def remove(self, key: int) -> None:
        hash = self.hash(key)
        hash_bucket = self.buckets[hash]

        
        for idx, pair in enumerate(hash_bucket):
            if pair[0] == key:
                hash_bucket.remove(pair)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)