nums = [2, 11, 8, 15]
target = 9
for i in nums:
    if (target - i) in nums.remove(i):
        print(nums)
        print([nums.index(i), nums.index(target - i)])