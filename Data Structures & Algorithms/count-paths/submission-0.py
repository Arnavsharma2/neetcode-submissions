class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        self.MOVES = [[0,1], [1,0]]
        def dfs(i, j):
            if (i, j) == (m-1, n-1):
                return 1
            if i >= m or j >= n:
                return 0
            
            return dfs(i+1, j) + dfs(i, j+1)

        return dfs(0, 0)
