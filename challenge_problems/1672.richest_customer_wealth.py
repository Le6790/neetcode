class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(map(sum,accounts))

        max_wealth = 0

        for account in accounts:
            total_wealth = 0
            for wealth in account:
                total_wealth += wealth

            max_wealth = total_wealth if total_wealth > max_wealth else max_wealth


        return max_wealth

sol = Solution()

print(sol.maximumWealth([[1,2,3],[4,5,6]]))
