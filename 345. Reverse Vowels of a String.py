'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        order = ''
        res = ''
        for i in s :
            if i in 'aeiouAEIOU':
                order += i
        for j in s:
            if j in 'aeiouAEIOU':
                res += order[-1]
                order = order[:-1]
            else:
                res += j
        return res