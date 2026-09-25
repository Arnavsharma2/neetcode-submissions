class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        self.visited = set()
        def dfs(i, j):
            best = 2147483647
            if grid[i][j] == -1:
                return 2147483647
            elif grid[i][j] == 0:
                return 0

            DIRECTIONS = [[0,-1], [0,1], [1,0], [-1,0]]

            for d in DIRECTIONS:
                tempI, tempJ = i + d[0], j + d[1]
                if (tempI, tempJ) not in self.visited:
                    if 0 <= tempI < len(grid) and 0 <= tempJ < len(grid[0]):
                        self.visited.add((tempI, tempJ))
                        best = min(best, 1 + dfs(tempI, tempJ))
                        self.visited.remove((tempI, tempJ))

            return best
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2147483647:
                    grid[r][c] = dfs(r, c)
                 