class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        target = totalSum // 2

        if totalSum % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)

        for num in nums:
            temp_dp = set()

            for item in dp:
                temp_dp.add(num + item)
                temp_dp.add(item)

            dp = temp_dp
        
        return target in dp
