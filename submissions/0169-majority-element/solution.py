class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = {}
        max_freq = 0
        majority_elem = 0
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
            if freq_map[num] > max_freq:
                max_freq = freq_map[num]
                majority_elem = num

        return majority_elem
        

        
