'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        counter = 0

        while counter < n:
            if s[counter] =='(':
                if s[counter + 1] ==')':
                    counter = counter + 1
                else:
                    return False
            if s[counter] =='{':
                if s[counter + 1] =='}':
                    counter = counter + 1
                else:
                    return False
            if s[counter] == '[':
                if s[counter + 1] ==']':
                    counter = counter + 1
                else:
                    return False
        return True