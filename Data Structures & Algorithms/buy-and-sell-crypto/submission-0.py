class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l = 0
        r = len(prices)-1
        while l < r and r < len(prices):
            maxProfit = max(maxProfit, prices[r]-prices[l])
            if prices[r] >= prices[l]:
                r -= 1
            else:
                l += 1
        return maxProfit
        