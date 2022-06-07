class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []

        for i,k in enumerate(nums):
            nums1 = nums[:i]
            nums2 = nums[i+1:]

            val1 = 1
            val2 = 1
            for i in nums1:
                val1 *=i
            for i in nums2:
                val2 *=i
            result.append(val1*val2)
        
        return(result)
    
    def productExceptSelfOptimized(self, nums):

        res = [1]* (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1, -1):
            print(nums[i])
            res[i] *=postfix
            postfix *= nums[i]
        
        return res


solution = Solution()

print(solution.productExceptSelfOptimized([1,2,3,4]))