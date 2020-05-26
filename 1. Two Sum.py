'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return (dict[target - x], i)
            dict[x] = i
        # Method 2:
        # for i in range(len(nums)):
        #     if (target - nums[i]) in nums:
        #         if nums[i] == target - nums[i] and i == nums.index(target - nums[i]):
        #             continue
        #         return [i, nums.index(target - nums[i])]

        # Method  3
        # try to upadate