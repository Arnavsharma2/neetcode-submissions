class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(i, total):
            if total == 0:
                return 0
            if total < 0:
                return float('inf')
            if i >= len(coins):
                return float('inf')
            if (i, total) in memo:
                return memo[(i, total)]
            
            pick = 1 + dfs(i, total - coins[i])
            skip = dfs(i + 1, total)
            memo[(i, total)] = min(pick, skip)

            return min(pick, skip)

        res = dfs(0,amount)
        if res == float('inf'):
            return -1
        return res
            

