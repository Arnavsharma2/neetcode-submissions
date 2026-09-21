class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                num = board[r][c]
                if num != '.':
                    if num in row[r] or num in col[c] or num in square[(r//3, c//3)]:
                        return False
                
                row[r].add(num)
                col[c].add(num)
                square[(r//3, c//3)].add(num)
        
        return True

