class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0 for i in range(len(temperatures))]

        for idx, temp in enumerate(temperatures):
            if not stack:
                stack.append((idx, temp))
                continue
            
            while stack:
                print(stack)
                head_idx, head_temp = stack[-1]

                if head_temp >= temp:
                    break
                else:
                    head_idx, head_temp = stack.pop()
                    results[head_idx] = idx - head_idx
            
            stack.append((idx, temp))
        
        return results

