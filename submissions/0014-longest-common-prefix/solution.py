class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_string = min(strs)
        max_string = max(strs)

        for i in range(len(min_string)):
            if min_string[i] != max_string[i]:
                return min_string[:i]
        return min_string
