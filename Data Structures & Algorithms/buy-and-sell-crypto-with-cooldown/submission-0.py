class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        def paths(i, holding):
            if i >= len(prices):
                return 0
            if holding:
                return max(paths(i + 1, True), prices[i] + paths(i + 2, False))
            else:
                return max(paths(i + 1, True) - prices[i], paths(i + 1, False))
        
        return paths(0, 0)