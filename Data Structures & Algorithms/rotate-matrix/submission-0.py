class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        for r in range(len(matrix)):
            for c in range(r+1, len(matrix)):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        
        






            

            