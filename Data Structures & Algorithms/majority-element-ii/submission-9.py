from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return self.generalisedNkVoter(nums, 3)
    
    def generalisedNkVoter(self, nums: List[int], k: int) -> List[int]:
        voters = {}

        for num in nums:
            if num in voters:
                voters[num] += 1
            elif len(voters) < k - 1:
                voters[num] = 1
            else:
                # replace
                candidates = list(voters.keys())
                for candidate in candidates:
                    voters[candidate] -= 1

                    if voters[candidate] == 0:
                        voters.pop(candidate)
            
        return [
            candidate for candidate in voters
            if nums.count(candidate) > len(nums) // k
        ]