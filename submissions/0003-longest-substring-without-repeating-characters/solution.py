class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first = last = 0
        found = set()
        substring_len = 0
        while last < len(s):
            if s[last] in found:
                first +=1
                last = first
                found = set()
            found.add(s[last])
            last += 1
            substring_len = max(len(s[first:last]), substring_len)
        return substring_len

        
