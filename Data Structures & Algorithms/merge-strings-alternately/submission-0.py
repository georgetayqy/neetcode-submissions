class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_length, word2_length = len(word1), len(word2)
        merged = []

        for i in range(min(word1_length, word2_length)):
            merged.append(word1[i])
            merged.append(word2[i])
        
        if word1_length != min(word1_length, word2_length):
            merged.append(word1[min(word1_length, word2_length):])
        
        if word2_length != min(word1_length, word2_length):
            merged.append(word2[min(word1_length, word2_length):])
        
        return "".join(merged)
