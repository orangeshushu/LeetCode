import sys
'''
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[:-1])
print(a[::-1])
t(a[::-2])

[0, 1, 2, 3, 4, 5, 6, 7, 8]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


print(sys.maxsize)
print(2**31)
class Python:
    def selfDemo():
        print('Python,why self?')
p = Python()
p.selfDemo()
'''
# # letter = 'Abc Ick'
# # print(letter.islower())
# import bisect
# data = [4, 2, 9, 7]
# data.sort()
# bisect.insort

# s = 'abc'
# print(s*3)
N = 857
ans = 0
# a = map(int, '11')
# print(a)
# for i in a:
#     print(i)
# <map object at 0x105b07ba8>
# <class 'int'>
# <class 'int'>
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        for n in range(1, N + 1):
            nset = set(map(int, str(n)))
            if any(x in nset for x in (2, 5, 6, 9)):
                if not any(x in nset for x in (3, 4, 7)):
                    ans += 1
        return ans