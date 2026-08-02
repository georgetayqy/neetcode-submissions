class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1

        if digits[-1] <= 9:
            return digits

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            carry, digits[i] = total // 10, total % 10
        
        if carry > 0:
            return [carry] + digits
        
        return digits