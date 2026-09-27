class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def dfs(r, c):
            area = 1
            DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            for d in DIRECTIONS:
                tempR, tempC = r + d[0], c + d[1]
                if 0 <= tempR < len(grid) and 0 <= tempC < len(grid[0]):
                    if grid[tempR][tempC] == 1:
                        grid[tempR][tempC] = 0
                        area += dfs(tempR, tempC)
                    
            return area
        



        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    res = max(res, dfs(r, c))
        
        return res