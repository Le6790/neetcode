# https://leetcode.com/problems/two-sum/

from sqlite3 import complete_statement


class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            complement = target-nums[i]
            
            for j in range(i, len(nums)):

                if nums[j] == complement:
                    return [i,j]

    def twoSumOptimized(self, nums, target):
        used_nums = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in used_nums:
                return [i, used_nums[complement]]

            used_nums[nums[i]] = i

solution = Solution()

print(solution.twoSum([2,7,11,15],9))

print(solution.twoSumOptimized([2,7,11,15],9))