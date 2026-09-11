class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l = 0
        r = 1
        for r in range (len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r]-prices[l])
        return maxProfit
        