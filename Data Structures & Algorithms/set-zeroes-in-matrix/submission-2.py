class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroes.add((r, c))
            

        for r, c in zeroes:
            for row in range(len(matrix)):
                matrix[row][c] = 0
            
            for col in range(len(matrix[0])):
                matrix[r][col] = 0
            
        



        