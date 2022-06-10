class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = -1

        l = 0
        r = len(height) -1

        while l < r:
            area = min(height[l],height[r]) * (r-l)
            result = max(area, result)
            
            if height[l] < height[r]:
                l += 1

            elif height[l] >= height[r]:
                r -= 1
            
        return result


solution = Solution()

print(solution.maxArea([1,8,6,2,5,4,8,3,7]))