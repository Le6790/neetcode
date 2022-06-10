class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        nums = sorted(nums)
        used_nums = set()
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    used_nums.add(nums[i])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        continue
            
        return result


solution = Solution()

print(solution.threeSum([-1,0,1,2,-1,-4]))