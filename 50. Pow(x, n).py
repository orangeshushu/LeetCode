'''
Implement pow(x, n).


Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
'''


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # counter = 1
        # element  = x
        # if n == 0 and x != 0:
        #     return 1
        # else:
        #     while counter < abs(n):
        #         x = x*element
        #         counter += 1
        #     if n >0:return x
        #     else:return 1/x
        res = 1
        if n < 0:
            n = -n
            flag = 1
        else:
            flag = 0
        while n > 0:
            if n % 2 == 1:
                res = res * x
            x = x * x
            n = n // 2
        if flag == 1:
            return 1.0 / res
        else:
            return res
