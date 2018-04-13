'''
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
'''
class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        s =''
        res = 1
        c = 1337
        a = a % c
        for i in b:
            s = s + str(i)
        number = int(s)
        # 快速幂 ：积的取余等于取余的积的取余
        while number > 0:
            if number % 2 == 1:
                res = (res * a)%c
            a = (a * a)%c
            number = number // 2
        return res
