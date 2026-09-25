class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        DIRECTIONS = [[0,-1], [0,1], [1,0], [-1,0]]

        visited = set()
        moves = 0
        while queue:
            r, c = queue.popleft()
            for d in DIRECTIONS:
                tempR = r + d[0]
                tempC = c + d[1]
                if 0 <= tempR < len(grid) and 0 <= tempC < len(grid[0]) and grid[tempR][tempC] > 0 and (tempR, tempC) not in visited:
                    visited.add((tempR, tempC))
                    grid[tempR][tempC] = 1 + grid[r][c]
                    queue.append((tempR, tempC))
                    


