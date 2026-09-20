class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        copy = [row[:] for row in matrix]

        mLen = len(matrix)
        nLen = len(matrix[0])

        for r in range(mLen):
            for c in range(nLen):
                if copy[r][c] == 0:
                    for i in range(mLen):
                        matrix[i][c] = 0
                    for j in range(nLen):
                        matrix[r][j] = 0
                    