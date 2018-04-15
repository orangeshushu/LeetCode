'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.isspace():
            return ''
        res = ''
        answerlist = s.split()[::-1]
        for i in answerlist:
            res = res + i + ' '
        return res[:-1].strip()