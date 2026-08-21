class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        
        for num in freq_map:
            if freq_map[num] != 2:
                return num
        
