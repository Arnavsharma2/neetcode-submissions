class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroes.add((r, c))
            
        visitedCol = set()
        visitedRow = set()
        for r, c in zeroes:
            if c not in visitedCol:
                for row in range(len(matrix)):
                    matrix[row][c] = 0
            
            if r not in visitedRow:
                for col in range(len(matrix[0])):
                    matrix[r][col] = 0
            
            visitedRow.add(r)
            visitedCol.add(c)
            
        



        