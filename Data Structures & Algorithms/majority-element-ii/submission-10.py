class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return self.generalisedNkVoter(
            nums, 3
        )
    
    def generalisedNkVoter(self, nums: List[int], k: int) -> List[int]:
        # there can at most be k - 1 keys
        # there is less than that then we can add more
        # candidates, otherwise need to fair vote decrement
        # and evict
        candidates = {}

        for num in nums:
            if num in candidates:
                candidates[num] += 1
            elif len(candidates) < k - 1:
                candidates[num] = 1
            else:
                # we need to convert to list since
                # keys() will mutate during dict iteration
                candidates_key = list(candidates.keys())
                for candidate in candidates_key:
                    candidates[candidate] -= 1

                    # then evict if possible
                    if candidates[candidate] == 0:
                        candidates[num] = 1
        
        return [
            candidate for candidate in candidates
            if nums.count(candidate) > len(nums) // k
        ]
            