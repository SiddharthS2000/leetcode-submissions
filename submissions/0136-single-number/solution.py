from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)

        for k, v in counter.items():
            if v == 1:
                return k
