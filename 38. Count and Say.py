class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res


