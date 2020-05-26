'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed
integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns
0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x: int) -> int:
        if (0 < x < 2147483648) and (0< int(str(x)[::-1]) < 2147483648):
            return int(str(x)[::-1])
        elif (-2147483648 < x < 0) and ( -2147483648 < int("-" + str(x)[::-1][:-1]) < 0):
            return int("-" + str(x)[::-1][:-1])
        return 0
