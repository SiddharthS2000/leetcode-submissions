class Solution:
    def longestCommonPrefix(self, strs):
        """s = strs[0]
        for i in strs:
            if len(i) < len(s):
                s = i
        pre = ""
        for i in range(len(s)):
            c = s[i]
            common = True
            for j in strs:
                if j[i] != c:
                    common = False
            if common:
                pre += c
        return pre"""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        min_len = min(len(first),len(last))
        i = 0
        while i < min_len and first[i] == last[i]:
            i += 1
        return first[:i]
