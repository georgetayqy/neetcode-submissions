class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        
        for i in range(len(temperatures)):
            total_num = 0
            
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    results.append(j - i)
                    break
            else:
                results.append(0)
        
        return results
        