class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        visited = {}
        def paths(i, holding):
            if i >= len(prices):
                return 0
            elif (i, holding) in visited:
                return visited[(i, holding)]

            if holding:
                sell = max(paths(i + 1, True), prices[i] + paths(i + 2, False))
                visited[(i, holding)] = sell
                return sell
            else:
                buy = max(paths(i + 1, True) - prices[i], paths(i + 1, False))
                visited[(i, holding)] = buy
                return buy
        
        return paths(0, 0)