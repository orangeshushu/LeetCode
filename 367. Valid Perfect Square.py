# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        low, high = 1, num
        while low < high:
            mid = (low + high)/2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = low + 1
            elif mid * mid > num:
                high = mid
        return False
if __name__ == '__main__':
    l = Solution()
    print(l.isPerfectSquare(5))


