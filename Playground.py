# import sys
# '''
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[:-1])
# print(a[::-1])
# t(a[::-2])
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#
#
# print(sys.maxsize)
# print(2**31)
# class Python:
#     def selfDemo():
#         print('Python,why self?')
# p = Python()
# p.selfDemo()
# '''
# # # letter = 'Abc Ick'
# # # print(letter.islower())
# # import bisect
# # data = [4, 2, 9, 7]
# # data.sort()
# # bisect.insort
#
# # s = 'abc'
# # print(s*3)
# N = 857
# ans = 0
# # a = map(int, '11')
# # print(a)
# # for i in a:
# #     print(i)
# # <map object at 0x105b07ba8>
# # <class 'int'>
# # <class 'int'>
#
# # print([0]*3)
# # class Solution:
# #     def climbStairs(self, n):
# #         """
# #         :type n: int
# #         :rtype: int
# #         """
# #         return self.d(n)
# #
# #     def d(self, a):
# #         if a ==1 or a ==2 or a == 0:
# #             return a
# #         else:
# #             return self.d(a - 1) +self.d(a - 2)
# # if __name__ == '__main__':
# #     s = Solution()
# #     print(s.climbStairs(9))
# #
# #
# # from collections import Counter
# #
# # s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()
# #
# # c = Counter(s)
# # # 获取出现频率最高的5个字符
# # print(c)
# # print(c['a'])
# #
# #
# # # Result:
# # [(' ', 54), ('e', 32), ('s', 25), ('a', 24), ('t', 24)]
# # 排列组合
# # from scipy.special import comb
# # res = 0
# # for i in range(1,26):
# #     res += comb(25,i)
# # print(res)
#
# #
# # num = 38
# # a = map(int,str(num))
# # print(sum(a))
#
# class Solution(object):
#     def longestWord(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         while len(words) > 0:
#             a = max(words)
#             print(a)
#             print(self.isright(a, words))
#             if self.isright(a, words):
#                 return a
#             else:
#                 words.remove(a)
#
#     def isright(self, w, s):
#         for i in range(len(w)):
#             if w[0:(i+1)] not in s:
#                 return False
#         return True
# if __name__ == '__main__':
#     s = Solution()
#     words = ["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]
#     answer = s.longestWord(words)
#     print(answer)


# theString = 'saaaay yes no yaaaass'
# print(theString.strip('yas'))
# class Solution:
#     def largestNumber(self, num):
#         num = sorted([str(x) for x in num], cmp=self.compare)
#         ans = ''.join(num).lstrip('0')
#         return ans or '0'
#
#
#     def compare(self, a, b):
#         return [1, -1][a + b > b + a]
#
# if __name__ == '__main__':
#     num = [3, 30, 34, 5, 9]
#     s =Solution()
#     answer =  s.largestNumber(num)
#     print(answer)
from collections import Counter
s= "cbaebabacd"
p= "abc"
res = []
pCounter = Counter(p)
sCounter = Counter(s[:len(p) - 1])
print(sCounter[s[3]])
for i in range(len(p) - 1, len(s)):
    sCounter[s[i]] += 1  # include a new char in the window
    if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
        res.append(i - len(p) + 1)  # append the starting index
    sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
    if sCounter[s[i - len(p) + 1]] == 0:
        del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
print(res)
