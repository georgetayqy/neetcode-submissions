class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        counts = defaultdict(int)
        return_list = []

        for num in nums:
            counts[num] += 1
        
        for number, frequency in counts.items():
            buckets[frequency].append(number)

        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]

            for item in bucket:
                if len(return_list) == k:
                    return return_list
                
                return_list.append(item)

        return return_list
