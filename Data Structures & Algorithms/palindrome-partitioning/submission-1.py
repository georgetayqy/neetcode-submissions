class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        current_partitions = []

        def dfs(current_index):
            if current_index >= len(s):
                results.append(current_partitions.copy())
                return
            
            # we can check through all character in the string
            for end_index in range(current_index, len(s)):
                # we have to generate ALL possible substrings starting
                # at current_index
                if self.isPalindrome(s, current_index, end_index):
                    # take note of the right boundary (must be inclusive)
                    current_partitions.append(s[current_index : end_index + 1])
                    
                    # only recurse further if we have a valid palindromic substring
                    # > recurse starting at the next offset from i
                    dfs(end_index + 1)
                    
                    # then remove the new partition
                    current_partitions.pop()

        dfs(0)
        return results

    
    def isPalindrome(self, string, left, right):
        while left < right:
            if string[left] != string[right]:
                return False
            
            left, right = left + 1, right - 1

        return True