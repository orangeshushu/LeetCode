'''
User Accepted: 1447
User Tried: 1750
Total Accepted: 1480
Total Submissions: 4970
Difficulty: Medium
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation:
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
'''

class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        al = 'abcdefghijklmnopqrstuvwxyz'
        answer = ''
        number = sum(shifts)
        dic = {'a': 0, 'i': 8, 'd': 3, 't': 19, 'x': 23, 'o': 14, 'z': 25, 'k': 10, 'r': 17, 'j': 9, 'e': 4, 'q': 16, 'f': 5, 'y': 24, 'u': 20, 'b': 1, 's': 18, 'v': 21, 'c': 2, 'l': 11, 'n': 13, 'm': 12, 'p': 15, 'w': 22, 'h': 7, 'g': 6}
        for j, v in enumerate(S):
            after = (dic[v] + number) % 26
            answer = answer + al[after]
            number = number - shifts[j]
        return answer