class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []
        for i in range(len(nums)):
            sum_entry = 0
            for j in range(0, i+1):
                sum_entry += nums[j]
            running_sum.append(sum_entry)
        return running_sum
