# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # LTE

        list = []
        balance = n
        counter = 1
        if n == 0 or n == 1:
            return n
        if n < 3:
            return 1
        while balance - counter >= 0:
            list.append(counter)
            balance = balance - counter
            counter = counter + 1
        if balance - counter < 0:
            list.append(balance)
        if list[-1] != list[-2] + 1:
            return len(list) - 1
        else:
            return len(list)


if __name__ == '__main__':
     l = Solution()
     answer = l.arrangeCoins(5)
     print(answer)


