
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

S = [1, 0, -1, 0, -2, 2]
S.sort()
list = []
for i in len(S)-3:
    for j in len(S)-2:
        if i + j == 0 and i != j:
            list.append([i, j])
print(list)
class Solution(object):
    def fourSum(self, nums, target):
        resultList = []
        nums.sort()
        for i in range(0,len(nums)-3):
            for j in range(i + 1, len(nums)-2):
                p = j + 1
                q = len(nums) -1
                while p != q:
                    summer = nums[i] + nums[j] + nums[p] + nums[q]
                    if summer == target:
                        listT = [nums[i],nums[j],nums[p],nums[q]]
                        if listT not in resultList:
                            resultList.append(listT)
                        p = p + 1
                    elif summer > target:
                        q = q - 1
                    else:
                        p = p + 1
        return resultList
