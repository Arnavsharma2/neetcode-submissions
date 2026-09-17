class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    self.decay(i, j)
                    self.res += 1
        return self.res
        

    def decay(self, i, j):
        bounds = [[1,0],[-1,0],[0,1],[0,-1]]

        for bound in bounds:
            tempI = i + bound[0]
            tempJ = j + bound[1]
            if tempI >= 0 and tempI < len(self.grid) and tempJ >= 0 and tempJ < len(self.grid[0]):
                if self.grid[tempI][tempJ] == '1':
                    self.grid[tempI][tempJ] = '0'
                    self.decay(tempI, tempJ)

        

