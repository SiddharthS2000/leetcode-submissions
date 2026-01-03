class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in range(len(nums)):
            diff = target - nums[index1]
            if diff in nums:
                index2 = nums.index(diff)
                if index1 != index2:
                    return index1, index2

