class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        min_str = min(strs)
        max_str = max(strs)
        for idx, ch in enumerate(min_str):
            if min_str[idx] != max_str[idx]:
                return min_str[:idx]

        return min_str
