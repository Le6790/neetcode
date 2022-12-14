class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in range(len(nums)):
            nums[i] = nums[i] + sum 
            sum=nums[i]
        return nums

sol = Solution()


print(sol.runningSum([1,2,3,4]))
