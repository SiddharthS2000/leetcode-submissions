class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            if carry == 0:
                return digits
            i -= 1
        else:
            return [1] + digits
        
