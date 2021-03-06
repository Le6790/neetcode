class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) -1

        while l < r:

            
            if numbers[l] + numbers[r] < target:
                l +=1
            elif numbers[l] + numbers[r] > target:
                r -=1
            if numbers[l] + numbers[r] == target:
                return l+1, r+1


solution = Solution()

print(solution.twoSum([1,3,4,5,7,11],9))