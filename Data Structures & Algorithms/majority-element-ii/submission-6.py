class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, count1, count2 = None, None, 0, 0

        for num in nums:
            # check if number match the candidates first
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            # before checking if count is 0 and we can evict
            # one of the candidates
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                # fair downvoting of both candidates
                # no need to worry about count1 < 0
                # count2 < 0 after deletion, since 
                # count1, count2 will be >= 1 due to
                # the initialisation checks above
                count1 -= 1
                count2 -= 1
        
        # due to the checking of matching candidate numbers
        # we don't have to worry about dedupe here
        # simply return candidates if their count is > len(list)
        return [
            cand for cand in (cand1, cand2)
            if nums.count(cand) > len(nums) // 3
        ]