class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = list()
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in nums and idx != nums.index(diff):
                return [idx, nums.index(diff)]
        
