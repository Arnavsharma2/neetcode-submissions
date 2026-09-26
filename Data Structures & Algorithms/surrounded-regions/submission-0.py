class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()

        DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]
        def infect(r, c):
            visited.add((r, c))
            if not(0 <= r < len(board)) or not(0 <= c < len(board[0])):
                return

            for d in DIRECTIONS:
                tempR, tempC = r + d[0], c + d[1]
                if not(0 <= tempR < len(board)) or not(0 <= tempC < len(board[0])):
                    continue
                if board[tempR][tempC] == 'O':
                    infect(tempR, tempC)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1:
                    if board[r][c] == "O":
                        infect(r, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = 'X'