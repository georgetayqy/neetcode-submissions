from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        results = []
        left = right = 0

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)
            
            # if OOB, then we need to remove it
            if q and q[0] < left:
                q.popleft()
            
            # window must be at least size k
            if right + 1 >= k:
                results.append(nums[q[0]])
                left += 1  # left can only be incremented once win size >= k

            right += 1
            
        return results
