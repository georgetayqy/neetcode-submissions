class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        results = []
        temp = []

        if len(digits) == 0:
            return results

        def iterate(idx):
            if idx > len(digits):
                return

            if len(temp) == len(digits):
                results.append("".join(temp))
                return

            for char in num_to_char[digits[idx]]:
                print(char)
                temp.append(char)
                iterate(idx + 1)
                temp.pop()

        iterate(0)
        return results           

            

        