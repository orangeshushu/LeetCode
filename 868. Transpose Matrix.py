import math
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

    def checknum(self,num):
        start = 2
        while start <= math.sqrt(num):
            if num % start ==0:
                return False
            start += 1
        return True
    def checkPalindrome(self,num):
        if str(num) == str(num)[::-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    N = 1
    while N < 10e8:
        if s.checknum(N) == True and s.checkPalindrome(N) == True:
            print(N, end=',')
        N += 1