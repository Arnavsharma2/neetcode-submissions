class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        minBuy = float('inf')
        for price in prices:
            minBuy = min(price, minBuy)
            profit = max(price-minBuy, profit)
        
        return profit