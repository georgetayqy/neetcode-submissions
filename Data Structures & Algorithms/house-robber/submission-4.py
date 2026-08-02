class Solution:
    def rob(self, nums: List[int]) -> int:
        # max of the array
        # max amount robbed = max(
        #   rob the first house + rob the 3rd house onwards,
        #   rob all other houses skipping the first house
        # )
        # rob = max(arr[0] + rob(2, end), rob(1, end))

        # need to maintain the last 2 maxes that we can rob from
        # rob1 is the max amount including this current robbed house
        # rob2 is the max amount excluding this current robbed house
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n + 1, n + 2, ...]
        for num in nums:
            max_to_rob_until_now = max(
                num + rob1,
                rob2
            )

            # then update rob1 to be rob2
            rob1 = rob2
            rob2 = max_to_rob_until_now
        
        # once we get to the end, rob2 contains the most updated
        # max of the amount of money we can rob
        return rob2