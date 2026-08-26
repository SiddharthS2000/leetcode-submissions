class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # hash_map = {}
        # res = set()
        # for n in nums:
        #     hash_map[n] = 1 + hash_map.get(n, 0)
        #     if hash_map[n] > len(nums) // 3:
        #         res.add(n)
        # return list(res)


        candidate_1, candidate_2 = None, None
        count_1, count_2 = 0, 0
        for num in nums:
            if candidate_1 == num:
                count_1 += 1
            elif candidate_2 == num:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = num
                count_1 = 1
            elif count_2 == 0:
                candidate_2 = num
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        
        res = []
        for c in [candidate_1, candidate_2]:
            if c is not None and nums.count(c) > len(nums) / 3:
                res.append(c)

        return res
