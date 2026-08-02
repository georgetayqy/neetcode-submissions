class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can do "bucket sort"
        # we know that the max frequency of each element is at most n, hence there must be a range of numbers
        # such that their frequencies are between [0 to n]
        # we must use a list for each frequency position as there may be > 1 term with the same frequency

        counter = {}
        # freq: [0, 1, 2, ..., n] (NOT N - 1)
        buckets = [None for i in range(len(nums) + 1)]
        
        # O(n) scan and add
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # O(n) scan and appending
        for num in counter:
            frequency = counter.get(num)

            if buckets[frequency]:
                buckets[frequency].append(num)
            else:
                buckets[frequency] = [num]

        values = []

        # O(n) scan and appending
        for freq in range(len(buckets) - 1, -1, -1):
            curr_bucket = buckets[freq]

            if curr_bucket:
                for value in curr_bucket:
                    if len(values) == k:
                        return values

                    values.append(value)

        return values