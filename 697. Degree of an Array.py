'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
'''
import sys
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        starts = {}
        ends = {}
        max_count = -sys.maxsize
        for i, num in enumerate(nums):
            if num not in starts:
                starts[num] = i
                counts[num] = 0
            counts[num] += 1
            ends[num] = i
            max_count = max(max_count, counts[num])
        result = sys.maxsize
        for num, count in counts.items():
            if count == max_count:
                result = min(result, ends[num] - starts[num] + 1)
        return result