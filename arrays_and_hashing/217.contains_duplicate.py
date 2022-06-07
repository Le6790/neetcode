
# https://leetcode.com/problems/contains-duplicate/

# sets in python - https://docs.python.org/2/library/sets.html
# unordered, unique elements
# under the hood is a hashmap which leads to fast lookup 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Create a set to track all the nums we have checked
        checked_nums = set()

        for val in nums:
            if val in checked_nums:
                return True
            
            checked_nums.add(val)
        
        return False

    def containsDuplicates_2(self,nums):

        return len(set(nums)) < len(nums)


solution = Solution()

assert solution.containsDuplicate([1,2,3,1]) == True # False
assert solution.containsDuplicate([1,2,3,4]) == False # False