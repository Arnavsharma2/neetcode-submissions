from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        visited = set()

        freshfruit = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshfruit += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        
        if freshfruit == 0:
            return 0
                

        DIRECTIONS = [[0,1], [0,-1],[1,0],[-1,0]]
        mins = -1
        while queue:
            mins += 1
            layer = queue.copy()
            queue.clear()
            while layer:
                r, c = layer.popleft()

                for d in DIRECTIONS:
                    newR, newC = r + d[0], c + d[1]
                    if (newR, newC) in visited or not(0 <= newR < len(grid)) or not(0 <= newC < len(grid[0])):
                        continue
                    if grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        queue.append((newR, newC))
                    visited.add((newR, newC))
        
        if mins == 0 or len(visited) != len(grid)*len(grid[0]):
            return -1
        return mins

                
                
            
        

                
            
        