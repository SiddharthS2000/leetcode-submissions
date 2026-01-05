class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip().split(" ")
        s = [st.strip() for st in s]
        return len(s[-1])
        
