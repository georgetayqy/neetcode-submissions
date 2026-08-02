class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[-1] = True
        
        for i in range(len(s) - 1, -1, -1):            
            for w in wordDict:
                current_word_shorter_than_s = (i + len(w)) <= len(s)
                current_word_matches_iterator = s[i:i + len(w)] == w
                
                if current_word_shorter_than_s and current_word_matches_iterator:
                    dp[i] = dp[i + len(w)]

                    if dp[i]:
                        break
                # break if we have found 
                
        
        return dp[0]
