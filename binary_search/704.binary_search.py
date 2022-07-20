class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)-1 # left and rightmost indexes of the array

        while l<=r:
            mid = (r+l)//2

            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
            elif target == nums[mid]:
                return mid
        
        return -1
