class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        res = []
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        DIR = [(0,1), (1, 0), (0,-1), (-1,0)]
        d = 0
        while len(res) != m*n:
            visited.add((i, j))
            res.append(matrix[i][j])
        
            di, dj = DIR[d]
            ni, nj = i + di, j + dj
            
            if (ni, nj) in visited or ni < 0 or nj < 0 or ni >= m or nj >= n:
                if d == 3:
                    d = 0
                else:
                    d += 1

            di, dj = DIR[d]
            i, j = i + di, j + dj
        
        return res
            
