class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack:
            return 0
            
        start = -1
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i] != needle[0] or haystack[i+len(needle)-1] != needle[-1]:
                continue
            
            start = i
            for j in range(len(needle)):
                if haystack[j+i] != needle[j]:
                    start = -1
                    break

            if start != -1:
                return start
        return start
                


