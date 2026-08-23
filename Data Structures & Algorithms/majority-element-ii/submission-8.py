class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return self.generalisedNkVoter(nums, 3)
    
    def generalisedNkVoter(self, nums: List[int], k: int) -> List[int]:
        """
        Generalised N/k voter algorithm
        """

        # create k - 1 candidates and k - 1 counts
        candidates = [None for i in range(k - 1)]
        counts = [0 for i in range(k - 1)]

        for num in nums:
            # if it breaks out then we don't have to do the count == 0 check
            for idx, candidate in enumerate(candidates):
                if num == candidate:
                    counts[idx] += 1
                    break
            else:
                # if we break out of the count loop, meaning
                # found a victim to evict, then we can skip
                # the fair vote decrement
                for idx, count in enumerate(counts):
                    if count == 0:
                        candidates[idx] = num
                        counts[idx] = 1
                        break
                else:
                    for i in range(k - 1):
                        counts[i] -= 1
        
        answer = []
        for candidate in candidates:
            if candidate is not None and nums.count(candidate) > len(nums) // k:
                answer.append(candidate)
                
        return answer

        