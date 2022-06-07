class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consec_sequence = 0

        for i in nums:
            
            if i-1 not in set(nums):
                
                length = 0
                while (i+length) in set(nums):
                    length+=1
                    
                
                consec_sequence = max(length,consec_sequence)
        return consec_sequence


solution = Solution()

print(solution.longestConsecutive([99,100,4,200,1,3,5,2]))