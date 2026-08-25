class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        slow = 0
        while slow < len(nums):
            fast = slow + 1
            while fast < len(nums) and nums[fast - 1] == nums[fast] - 1:
                fast += 1
            if fast - 1 == slow:
                res.append(str(nums[slow]))
            else:
                res.append(str(nums[slow])+"->"+str(nums[fast-1]))
            
            slow = fast

        return res
