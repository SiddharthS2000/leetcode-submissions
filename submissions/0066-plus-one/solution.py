class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for ind in range(len(digits)-1, -1 , -1):
            if carry:
                digits[ind] += 1
                carry = digits[ind] / 10
                digits[ind] = digits[ind] % 10

        if carry:
            digits.insert(0,1)
        return digits




