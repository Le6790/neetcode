class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_profit = 0
        lowest_price = prices[0]
        for i in range(len(prices)):

            best_profit = max(best_profit,prices[i] - lowest_price)
            lowest_price = min(prices[i], lowest_price)

        return best_profit

    def maxProfitOther(self, prices):
        l, r = 0, 1 # left=buy, right=sell

        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit,profit)
            elif prices[l] > prices[r]:
                l = r
            r+=1
        
        return(maxProfit)

solution = Solution()

print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfitOther([7,1,5,3,6,4]))
