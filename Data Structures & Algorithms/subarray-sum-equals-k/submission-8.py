from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # subarray sums rely on prefix sums

        # create a map of the prefix sum and the count in which
        # the prefix sums appear
        prefixes = defaultdict(int)
        prefixSum = 0
        count = 0
        
        # populate prefixes[0] with 1
        # the number of subarrays such that the running prefixSum - k is 0
        # will be 1 initially
        # this DOES NOT mean that the empty subarray is counted
        # this value is only counted when there is a first hit on prefixSum
        prefixes[0] = 1

        for num in nums:
            # increment prefixSum first (impt for first iteration)
            prefixSum += num
            
            # if the difference between the prefixSum and k is
            # in the prefixes, add the count
            # why? a subarray sum with boundary [left, right] == k 
            # if the P[left] - P[right] == k
            # i.e.: P[j] - P[i] = k, P[i] = P[j] - k, where
            # P[i] is prefixes key, P[j] is running prefixSum
            # k is the number
            if prefixSum - k in prefixes:
                count += prefixes[prefixSum - k]
            
            # then update the prefixes with the new prefixSum
            # increment by 1 by default
            prefixes[prefixSum] += 1
        
        return count
