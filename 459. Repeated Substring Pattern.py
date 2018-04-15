'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''
s = "aba"
a = ''
# stack = []
# for element in s:
#     if len(stack) == 0:
#         stack.insert(0, element)
#     elif stack[-1] == element:
#         stack.pop()
#     else:
#         stack.insert(0, element)
#         print('22222')
# if len(stack) == 0:
#     print('True')
# else:
#     print('False')
for i in s[:-1]:
    a = a + i
    print(a)
    if s.count(a) == len(s)/len(a):
        print(s.count(a), len(s), len(a))
        print('True')
print('False')