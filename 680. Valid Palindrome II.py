'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda s: s ==s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] != s[high]:
                return isPalindrome(strPart(s, low)) or isPalindrome(strPart(s, high))
            low += 1
            high -= 1
        return True
