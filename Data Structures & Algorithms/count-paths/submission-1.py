class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        self.MOVES = [[0,1], [1,0]]
        memo = {}
        def dfs(i, j):
            if (i, j) == (m-1, n-1):
                return 1
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            explore1 = dfs(i+1, j)
            explore2 = dfs(i, j+1)
            
            memo[(i, j)] = explore1 + explore2
            
            return explore1 + explore2

        return dfs(0, 0)
