class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s =='' or s.rsplit() == []:
            return 0
        return len(s.rsplit()[-1])