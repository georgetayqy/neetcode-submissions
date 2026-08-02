class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        elif len(s1) + len(s2) == 0:
            return True
        
        results = {}
        iterator = []

        def interleave(idx1, idx2, idx3):
            if idx3 == len(s3):
                return idx1 == len(s1) and idx2 == len(s2)
            
            if (idx1, idx2) in results:
                return results[(idx1, idx2)]
            
            if idx1 < len(s1) and s1[idx1] == s3[idx3]:
                if interleave(idx1 + 1, idx2, idx3 + 1):
                    results[(idx1, idx2)] = True
                    return True
            
            if idx2 < len(s2) and s2[idx2] == s3[idx3]:
                if interleave(idx1, idx2 + 1, idx3 + 1):
                    results[(idx1, idx2)] = True
                    return True
            
            results[(idx1, idx2)] = False
            return False
        
        return interleave(0, 0, 0)
