from collections import defaultdict

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(iterable, start, end):
            while start < end:
                if iterable[start] != iterable[end]:
                    return False
                
                start += 1
                end -= 1

            return True
        
        results = []
        curr = []

        def dfs(current_index):
            if current_index >= len(s):
                # if OOB, we have a valid partition
                # so we should clone the list
                results.append(curr.copy())
                return
            # we should iterate through the other chars
            for it in range(current_index, len(s)):
                if isPalindrome(s, current_index, it):
                    # s[i:it+1] is a palindrome
                    curr.append(s[current_index:it + 1])
                    dfs(it + 1)
                    
                    # remove the string we just added and remove it
                    curr.pop()
        
        dfs(0)

        return results

            
